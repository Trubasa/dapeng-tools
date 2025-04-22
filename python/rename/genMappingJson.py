import os
import json
import re
import logging
import asyncio
import time
from pathlib import Path
from typing import Dict, Optional, List, Any

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 尝试导入googletrans
try:
    from googletrans import Translator
    TRANSLATOR_AVAILABLE = True
    logger.info("已加载 googletrans 模块")
except ImportError:
    TRANSLATOR_AVAILABLE = False
    logger.warning("未找到 googletrans 模块，请安装: pip install googletrans==4.0.0-rc1")

# 常用中文词汇到英文的映射字典 - 作为备用
COMMON_TERMS = {
    "页面": "page",
    "主页": "home",
    "首页": "index",
    "攻略": "guide",
    "搜索": "search",
    "视频": "video",
    "图片": "image",
    "图": "img",
    "按钮": "button",
    "头像": "avatar",
    "边框": "border",
    "展开": "expand",
    "播放": "play",
    "暂停": "pause",
    "返回": "back",
    "进度": "progress",
    "进度条": "progressbar",
    "遮罩": "mask",
    "底": "bottom",
    "文案": "text",
    "文档": "document",
    "项目": "project",
    "全部": "all",
    "二级": "secondary",
    "框": "frame",
    "黑色": "black",
    "葫芦": "gourd",
}

def is_contains_chinese(text: str) -> bool:
    """检查字符串是否包含中文字符"""
    chinese_pattern = re.compile(r'[\u4e00-\u9fff]+')
    return bool(chinese_pattern.search(text))

def to_camel_case(text: str) -> str:
    """将文本转换为驼峰命名"""
    # 移除所有非字母数字，并用空格替换
    s = re.sub(r'[^a-zA-Z0-9]', ' ', text.lower())
    # 分割成单词
    words = s.split()
    if not words:
        return ""
    
    # 首个单词小写开头，其余单词大写开头
    camel = words[0]
    for word in words[1:]:
        if word:
            camel += word[0].upper() + word[1:]
    
    return camel

async def google_translate_async(text: str, src='zh-cn', dest='en') -> str:
    """异步使用Google翻译"""
    if not TRANSLATOR_AVAILABLE:
        return None
    
    try:
        translator = Translator()
        result = await translator.translate(text, src=src, dest=dest)
        return result.text
    except Exception as e:
        logger.warning(f"Google翻译失败: {e}")
        return None

def google_translate_sync(text: str, src='zh-cn', dest='en') -> str:
    """同步包装器，运行异步翻译函数"""
    if not TRANSLATOR_AVAILABLE:
        return None
    
    try:
        # 创建并执行异步事件循环
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            result = loop.run_until_complete(google_translate_async(text, src, dest))
            return result
        finally:
            loop.close()
    except Exception as e:
        logger.warning(f"翻译执行失败: {e}")
        return None

def translate_text(text: str) -> str:
    """将中文文本转换为英文，使用Google翻译并转为驼峰命名"""
    # 检查是否含有中文
    if not is_contains_chinese(text):
        return text
    
    # 处理连字符分隔的复合词
    if '-' in text:
        parts = text.split('-')
        translated_parts = []
        
        for part in parts:
            if is_contains_chinese(part):
                translated = translate_part(part)
                translated_parts.append(translated)
            else:
                translated_parts.append(part)
        
        return '-'.join(translated_parts)
    
    return translate_part(text)

def translate_part(text: str) -> str:
    """翻译单个部分并转为驼峰命名"""
    # 首先尝试Google翻译
    translated = google_translate_sync(text)
    
    if translated:
        # 转为驼峰命名
        camel = to_camel_case(translated)
        if camel:
            return camel
    
    # 翻译失败时，尝试使用常用词汇映射
    if text in COMMON_TERMS:
        return COMMON_TERMS[text]
    
    # 分词尝试
    result_parts = []
    found = False
    
    for i in range(1, len(text) + 1):
        prefix = text[:i]
        if prefix in COMMON_TERMS:
            result_parts.append(COMMON_TERMS[prefix])
            if i < len(text):
                suffix_translated = translate_part(text[i:])
                if suffix_translated:
                    # 确保后续部分首字母大写，以保持驼峰格式
                    if suffix_translated[0].islower():
                        suffix_translated = suffix_translated[0].upper() + suffix_translated[1:]
                    result_parts.append(suffix_translated)
            found = True
            break
    
    if found:
        return ''.join(result_parts)
    
    # 最后的备用方案：生成字母代码
    return ''.join([f"x{ord(c)}" for c in text if is_contains_chinese(c)]) or "x"

def scan_directory(directory: str) -> Dict[str, str]:
    """扫描目录，提取中文名称并生成映射"""
    mapping = {}
    
    # 确保目录存在
    if not os.path.exists(directory):
        logger.error(f"目录不存在: {directory}")
        return mapping
    
    # 遍历目录
    for root, dirs, files in os.walk(directory):
        # 处理目录名
        for dir_name in dirs:
            if is_contains_chinese(dir_name):
                english_name = translate_text(dir_name)
                mapping[dir_name] = english_name
                logger.info(f"添加目录映射: {dir_name} -> {english_name}")
        
        # 处理文件名
        for file_name in files:
            name, ext = os.path.splitext(file_name)
            if is_contains_chinese(name):
                english_name = translate_text(name)
                mapping[name] = english_name
                logger.info(f"添加文件映射: {name} -> {english_name}")
    
    return mapping

def generate_mapping_json(
    directory: str, 
    output_path: str, 
    extra_mapping: Optional[Dict[str, str]] = None
) -> bool:
    """
    生成映射JSON文件
    
    Args:
        directory: 要扫描的目录路径
        output_path: 输出JSON文件的路径（包括文件名）
        extra_mapping: 要合并的额外映射
    
    Returns:
        bool: 操作是否成功
    """
    try:
        # 扫描目录获取映射
        mapping = scan_directory(directory)
        
        # 合并额外映射
        if extra_mapping:
            mapping.update(extra_mapping)
            logger.info(f"已合并 {len(extra_mapping)} 个额外映射")
        
        # 确保输出目录存在
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            logger.info(f"创建输出目录: {output_dir}")
        
        # 写入JSON文件
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(mapping, f, ensure_ascii=False, indent=4)
        
        logger.info(f"映射JSON已生成: {output_path} (共 {len(mapping)} 项)")
        return True
    
    except Exception as e:
        logger.error(f"生成映射JSON时出错: {e}")
        return False

def create_mapping_from_lists(
    chinese_list: List[str], 
    english_list: List[str]
) -> Dict[str, str]:
    """
    根据中文列表和英文列表创建映射
    
    Args:
        chinese_list: 中文名称列表
        english_list: 英文名称列表（顺序需要与中文列表对应）
    
    Returns:
        Dict[str, str]: 中文到英文的映射字典
    """
    if len(chinese_list) != len(english_list):
        logger.warning("中文列表和英文列表长度不一致")
    
    return dict(zip(chinese_list, english_list))

def test_translate():
    """测试翻译功能"""
    test_words = [
        "攻略页面",
        "视频图",
        "搜索页",
        "头像边框",
        "播放按钮",
        "暂停按钮",
        "葫芦",
        "返回按钮",
        "进度条",
        "黑色遮罩",
        "文案底",
        "攻略页面-视频图",
        "攻略页面1-攻略主页"
    ]
    
    print("测试翻译功能:")
    print("=" * 50)
    
    for word in test_words:
        translated = translate_text(word)
        print(f"'{word}' -> '{translated}'")
        # 短暂延迟避免API限制
        time.sleep(0.5)

def main():
    """命令行入口点"""
    import argparse
    
    parser = argparse.ArgumentParser(description='生成中文到英文的映射JSON文件')
    parser.add_argument('directory', nargs='?', help='要扫描的目录路径')
    parser.add_argument('output', nargs='?', help='输出JSON文件的路径（包括文件名）')
    parser.add_argument('--extra', help='额外映射的JSON文件路径')
    parser.add_argument('--append', action='store_true', help='如果输出文件已存在，合并而非覆盖')
    parser.add_argument('--test', action='store_true', help='执行翻译测试')
    
    args = parser.parse_args()
    
    # 执行翻译测试
    if args.test:
        test_translate()
        return
    
    # 确保必要参数存在
    if not args.directory or not args.output:
        parser.print_help()
        print("\n错误: directory 和 output 参数是必需的")
        return
    
    # 加载现有映射(如果需要合并)
    existing_mapping = {}
    if args.append and os.path.exists(args.output):
        try:
            with open(args.output, 'r', encoding='utf-8') as f:
                existing_mapping = json.load(f)
                logger.info(f"已加载现有映射: {args.output} (共 {len(existing_mapping)} 项)")
        except Exception as e:
            logger.error(f"加载现有映射文件失败: {e}")
    
    # 加载额外映射
    extra_mapping = None
    if args.extra:
        try:
            with open(args.extra, 'r', encoding='utf-8') as f:
                extra_mapping = json.load(f)
                logger.info(f"已加载额外映射: {args.extra} (共 {len(extra_mapping)} 项)")
        except Exception as e:
            logger.error(f"加载额外映射文件失败: {e}")
    
    # 合并现有映射
    if existing_mapping:
        if extra_mapping is None:
            extra_mapping = existing_mapping
        else:
            extra_mapping.update(existing_mapping)
    
    # 生成映射
    success = generate_mapping_json(args.directory, args.output, extra_mapping)
    
    if success:
        print(f"映射JSON生成成功: {args.output}")
    else:
        print("映射JSON生成失败")
        exit(1)

if __name__ == "__main__":
    main()