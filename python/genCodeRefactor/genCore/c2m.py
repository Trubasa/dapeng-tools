#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
from pathlib import Path

# 文件扩展名到Markdown代码块语言标识的映射
EXTENSIONS_MAP = {
    '.py': 'python',
    '.js': 'javascript',
    '.ts': 'typescript',
    '.tsx': 'tsx',
    '.jsx': 'jsx',
    '.java': 'java',
    '.c': 'c',
    '.cpp': 'cpp',
    '.cs': 'csharp',
    '.go': 'go',
    '.rb': 'ruby',
    '.php': 'php',
    '.swift': 'swift',
    '.kt': 'kotlin',
    '.rs': 'rust',
    '.sh': 'bash',
    '.html': 'html',
    '.css': 'css',
    '.scss': 'scss',
    '.json': 'json',
    '.yml': 'yaml',
    '.yaml': 'yaml',
    '.md': 'markdown',
    '.sql': 'sql',
    '.xml': 'xml',
    '.dart': 'dart',
    '.lua': 'lua',
    '.r': 'r',
    '.vue': 'vue',
    '.fs': 'fsharp',
    '.pl': 'perl',
    '.ps1': 'powershell',
    '.toml': 'toml',
    '.ini': 'ini',
    '.cfg': 'ini',
    '.dockerfile': 'dockerfile',
    '.tf': 'hcl',
    '.proto': 'protobuf',
    # 可以根据需要添加更多的扩展名映射
}

# 默认忽略的目录
DEFAULT_IGNORE_DIRS = [
    '.git', '.svn', '.idea', '.vscode', 
    'node_modules', '__pycache__', 
    'venv', 'env', '.env', 'build','public','scripts','.eslintrc-auto-import.json', 'dist','chatHistory','temp','apiParams','wxcomponents'
]

DEFAULT_IGNORE_FILES = ['.gitignore','package-lock.json', '.DS_Store', 'Thumbs.db', '.env.local', '.env.development.local', '.env.test.local', '.env.production.local', 'yarn.lock','area.ts','pnpm-lock.yaml']

def scan_code_files(directory, ignore_dirs=None, ignore_files=None):
    """
    扫描目录中的所有代码文件，忽略指定的目录和文件
    
    参数:
        directory (str): 要扫描的目录路径
        ignore_dirs (list): 要忽略的目录名列表
        ignore_files (list): 要忽略的文件名列表
        
    返回:
        list: 相对于输入目录的代码文件路径列表
    """
    code_files = []
    
    # 使用默认忽略目录和文件（如果未指定）
    if ignore_dirs is None:
        ignore_dirs = DEFAULT_IGNORE_DIRS
    
    if ignore_files is None:
        ignore_files = DEFAULT_IGNORE_FILES
    
    for root, dirs, files in os.walk(directory):
        # 从dirs中移除忽略的目录，这样os.walk不会递归进入它们
        # 必须原地修改dirs列表，而不是创建新列表
        dirs[:] = [d for d in dirs if d not in ignore_dirs and not any(
            os.path.join(root, d).startswith(os.path.join(directory, ignore_dir)) 
            for ignore_dir in ignore_dirs
        )]
        
        for file in files:
            # 检查文件是否在忽略列表中
            if file in ignore_files:
                continue
                
            file_path = os.path.join(root, file)
            # 获取相对路径
            rel_path = os.path.relpath(file_path, directory)
            # 检查文件扩展名是否在我们支持的列表中
            ext = os.path.splitext(file)[1].lower()
            if ext in EXTENSIONS_MAP:
                code_files.append(rel_path)
    
    # 按路径字母顺序排序
    code_files.sort()
    return code_files

def generate_toc(code_files):
    """生成目录部分"""
    toc = "## 目录\n\n"
    for file in code_files:
        toc += f"- [{file}](#{file.replace('/', '.').replace(' ', '-').replace('.', '')})\n"
    return toc

def generate_file_content(directory, file_path):
    """生成单个文件的Markdown内容"""
    full_path = os.path.join(directory, file_path)
    ext = os.path.splitext(file_path)[1].lower()
    language = EXTENSIONS_MAP.get(ext, '')
    
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            # 尝试其他编码
            with open(full_path, 'r', encoding='latin-1') as f:
                content = f.read()
        except Exception as e:
            content = f"无法读取文件内容: {str(e)}"
    
    return f"### {file_path}\n```{language}\n{content}\n```\n\n"

def generate_markdown(directory, output_file='./temp/step0.md', ignore_dirs=None, ignore_files=None, include_toc=True):
    """
    生成包含所有代码文件的Markdown文档
    
    参数:
        directory (str): 要扫描的目录路径
        output_file (str): 输出的Markdown文件名
        ignore_dirs (list): 要忽略的目录名列表
        ignore_files (list): 要忽略的文件名列表
        include_toc (bool): 是否包含目录(Table of Contents)
    """
    # 扫描代码文件，忽略指定的目录和文件
    code_files = scan_code_files(directory, ignore_dirs, ignore_files)
    
    if not code_files:
        print("警告: 未找到任何代码文件")
        return
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            # 写入标题
            f.write(f"# 代码文档: {os.path.basename(directory)}\n\n")
            
            # 写入生成信息
            f.write(f"*本文档由c2m工具自动生成于 {os.path.abspath(directory)}*\n\n")
            
            # 写入目录（如果需要）
            if include_toc:
                f.write(generate_toc(code_files))
                f.write("\n\n")
            
            # 写入每个文件的内容
            for file in code_files:
                print(f"添加文件: {file}")
                f.write(generate_file_content(directory, file))
                
        print(f"已成功生成Markdown文档: {os.path.abspath(output_file)}")
        print(f"共包含 {len(code_files)} 个代码文件")
        
    except Exception as e:
        print(f"生成文档时出错: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='将目录中的代码文件转换为Markdown文档')
    parser.add_argument('directory', help='要扫描的目录路径')
    parser.add_argument('-o', '--output', help='输出的Markdown文件名')
    parser.add_argument('-i', '--ignore-dirs', dest='ignore_dirs', nargs='+', default=DEFAULT_IGNORE_DIRS, 
                        help='要忽略的目录名列表（空格分隔，默认包含常见系统和配置目录）')
    parser.add_argument('-f', '--ignore-files', dest='ignore_files', nargs='+', default=DEFAULT_IGNORE_FILES,
                        help='要忽略的文件名列表（空格分隔，默认包含常见配置文件）')
    parser.add_argument('--no-toc', action='store_true', help='不生成目录(Table of Contents)')
    parser.add_argument('--list-extensions', action='store_true', help='列出支持的文件扩展名')
    parser.add_argument('--list-ignore', action='store_true', help='列出默认忽略的目录和文件')
    
    args = parser.parse_args()
    
    if args.list_extensions:
        print("支持的文件扩展名及对应语言:")
        for ext, lang in sorted(EXTENSIONS_MAP.items()):
            print(f"  {ext:8} -> {lang}")
        exit(0)
        
    if args.list_ignore:
        print("默认忽略的目录:")
        for dir_name in DEFAULT_IGNORE_DIRS:
            print(f"  {dir_name}")
        print("\n默认忽略的文件:")
        for file_name in DEFAULT_IGNORE_FILES:
            print(f"  {file_name}")
        exit(0)

    if not args.output:
        print("错误: 请指定输出文件名")
        exit(0)
    
    generate_markdown(args.directory, args.output, args.ignore_dirs, args.ignore_files, not args.no_toc)