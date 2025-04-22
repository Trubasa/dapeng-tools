# rename/rename_files.py
import os
import json
import argparse
import logging
from typing import Dict, List, Tuple

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_mapping(mapping_file: str) -> Dict[str, str]:
    """加载英文到中文的映射文件"""
    try:
        with open(mapping_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"映射文件 {mapping_file} 不存在")
        return {}
    except json.JSONDecodeError:
        logger.error(f"映射文件 {mapping_file} 格式错误，请确保是有效的JSON")
        return {}

def rename_file(file_path: str, mapping: Dict[str, str], dry_run: bool = False) -> bool:
    """重命名单个文件"""
    directory, filename = os.path.split(file_path)
    name, ext = os.path.splitext(filename)
    
    # 检查文件名是否存在于映射中
    if name in mapping:
        new_name = mapping[name] + ext
        new_path = os.path.join(directory, new_name)
        
        if dry_run:
            logger.info(f"将要重命名文件: {file_path} -> {new_path}")
            return True
            
        try:
            os.rename(file_path, new_path)
            logger.info(f"已重命名文件: {file_path} -> {new_path}")
            return True
        except OSError as e:
            logger.error(f"重命名文件失败 {file_path}: {e}")
            return False
    return False

def rename_directory(dir_path: str, mapping: Dict[str, str], dry_run: bool = False) -> bool:
    """重命名单个目录"""
    # 获取目录名（不包含父目录路径）
    parent_dir, dir_name = os.path.split(dir_path)
    
    # 检查目录名是否存在于映射中
    if dir_name in mapping:
        new_name = mapping[dir_name]
        new_path = os.path.join(parent_dir, new_name)
        
        if dry_run:
            logger.info(f"将要重命名目录: {dir_path} -> {new_path}")
            return True
            
        try:
            os.rename(dir_path, new_path)
            logger.info(f"已重命名目录: {dir_path} -> {new_path}")
            return True
        except OSError as e:
            logger.error(f"重命名目录失败 {dir_path}: {e}")
            return False
    return False

def process_directory(directory: str, mapping: Dict[str, str], dry_run: bool = False) -> Tuple[int, int, int, int]:
    """递归处理目录下的所有文件和目录"""
    if not os.path.exists(directory):
        logger.error(f"目录 {directory} 不存在")
        return 0, 0, 0, 0
    
    file_success_count = 0
    file_total_count = 0
    dir_success_count = 0
    dir_total_count = 0
    
    # 收集所有目录路径（从深到浅排序，确保先处理子目录）
    all_dirs = []
    # 处理所有文件
    for root, dirs, files in os.walk(directory):
        # 收集目录
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            all_dirs.append(dir_path)
        
        # 处理文件
        for file in files:
            file_path = os.path.join(root, file)
            file_total_count += 1
            if rename_file(file_path, mapping, dry_run):
                file_success_count += 1
    
    # 按路径长度降序排序目录（确保先处理深层目录）
    all_dirs.sort(key=lambda x: len(x.split(os.sep)), reverse=True)
    
    # 处理目录（从深到浅）
    for dir_path in all_dirs:
        dir_total_count += 1
        if rename_directory(dir_path, mapping, dry_run):
            dir_success_count += 1
    
    return file_success_count, file_total_count, dir_success_count, dir_total_count

def rename_files_and_dirs(directory: str, mapping_file: str, dry_run: bool = False) -> Tuple[int, int, int, int]:
    """
    根据映射替换文件名和目录名中的英文为中文
    
    Args:
        directory: 要处理的目录
        mapping_file: 包含英文到中文映射的JSON文件
        dry_run: 仅显示将要重命名的文件和目录，不执行重命名
    
    Returns:
        Tuple[int, int, int, int]: 成功重命名文件数量、总文件数量、成功重命名目录数量、总目录数量
    """
    mapping = load_mapping(mapping_file)
    if not mapping:
        logger.error("没有加载到有效的映射")
        return 0, 0, 0, 0
    
    logger.info(f"开始处理目录: {directory}")
    logger.info(f"加载了 {len(mapping)} 个映射规则")
    
    if dry_run:
        logger.info("执行演习模式，不会实际重命名文件和目录")
    
    return process_directory(directory, mapping, dry_run)

# 保留原函数名以保持兼容性
def rename_files(directory: str, mapping_file: str, dry_run: bool = False) -> Tuple[int, int]:
    """
    根据映射替换文件名中的英文为中文（兼容旧接口）
    
    Args:
        directory: 要处理的目录
        mapping_file: 包含英文到中文映射的JSON文件
        dry_run: 仅显示将要重命名的文件，不执行重命名
    
    Returns:
        Tuple[int, int]: 成功重命名文件数量和总文件数量
    """
    file_success, file_total, _, _ = rename_files_and_dirs(directory, mapping_file, dry_run)
    return file_success, file_total

def main():
    parser = argparse.ArgumentParser(description='根据映射替换文件名和目录名中的英文为中文')
    parser.add_argument('directory', help='要处理的目录')
    parser.add_argument('mapping_file', help='包含英文到中文映射的JSON文件')
    parser.add_argument('-d', '--dry-run', action='store_true', help='仅显示将要重命名的文件和目录，不执行重命名')
    parser.add_argument('--files-only', action='store_true', help='只重命名文件，不重命名目录')
    parser.add_argument('--dirs-only', action='store_true', help='只重命名目录，不重命名文件')
    
    args = parser.parse_args()
    
    if args.files_only and args.dirs_only:
        logger.error("--files-only 和 --dirs-only 不能同时使用")
        return
    
    if args.files_only:
        success, total = rename_files(args.directory, args.mapping_file, args.dry_run)
        logger.info(f"处理完成: 共 {total} 个文件，成功重命名 {success} 个文件")
    else:
        file_success, file_total, dir_success, dir_total = rename_files_and_dirs(
            args.directory, args.mapping_file, args.dry_run
        )
        
        if args.dirs_only:
            logger.info(f"处理完成: 共 {dir_total} 个目录，成功重命名 {dir_success} 个目录")
        else:
            logger.info(f"处理完成: 共 {file_total} 个文件，成功重命名 {file_success} 个文件")
            logger.info(f"处理完成: 共 {dir_total} 个目录，成功重命名 {dir_success} 个目录")

if __name__ == "__main__":
    main()