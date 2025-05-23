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
    # 可以根据需要添加更多的扩展名映射
}

def scan_code_files(directory):
    """扫描目录中的所有代码文件"""
    code_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
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

def generate_markdown(directory, output_file='code_documentation.md'):
    """生成包含所有代码文件的Markdown文档"""
    code_files = scan_code_files(directory)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # 写入标题
        f.write(f"# 代码文档: {os.path.basename(directory)}\n\n")
        
        # 写入目录
        f.write(generate_toc(code_files))
        f.write("\n\n")
        
        # 写入每个文件的内容
        for file in code_files:
            f.write(generate_file_content(directory, file))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='将目录中的代码文件转换为Markdown文档')
    parser.add_argument('directory', help='要扫描的目录路径')
    parser.add_argument('-o', '--output', default='code_documentation.md', help='输出的Markdown文件名')
    
    args = parser.parse_args()
    
    generate_markdown(args.directory, args.output)
    print(f"已生成Markdown文档: {args.output}")