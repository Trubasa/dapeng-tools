import tkinter as tk
from tkinter import filedialog
import os
import chardet

def detect_encoding(file_path):
    """
    检测文件编码
    """
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def read_file(file_path):
    """
    读取文件内容，自动检测编码
    """
    try:
        # 首先尝试检测编码
        encoding = detect_encoding(file_path)
        
        # 如果检测失败，默认使用UTF-8
        if encoding is None:
            encoding = 'utf-8'
        
        with open(file_path, 'r', encoding=encoding, errors='replace') as f:
            content = f.read()
        return content, encoding
    except Exception as e:
        return f"无法读取文件: {str(e)}", None

def get_file_info(file_path):
    """
    获取文件的基本信息
    """
    try:
        file_size = os.path.getsize(file_path)
        
        # 格式化文件大小
        if file_size < 1024:
            size_str = f"{file_size} 字节"
        elif file_size < 1024 * 1024:
            size_str = f"{file_size/1024:.2f} KB"
        else:
            size_str = f"{file_size/(1024*1024):.2f} MB"
            
        modified_time = os.path.getmtime(file_path)
        modified_time_str = f"{modified_time}"
        
        return f"文件大小: {size_str}\n最后修改时间: {modified_time_str}"
    except Exception as e:
        return f"无法获取文件信息: {str(e)}"

def main():
    """
    模块主入口函数
    """
    # 创建临时的Tk实例来支持文件对话框
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    
    # 打开文件选择对话框
    file_path = filedialog.askopenfilename(
        title="选择要查看的文件",
        filetypes=[
            ("文本文件", "*.txt"),
            ("Python文件", "*.py"),
            ("所有文件", "*.*")
        ]
    )
    
    # 如果用户取消选择，直接返回
    if not file_path:
        return "操作已取消"
    
    # 读取文件内容
    content, encoding = read_file(file_path)
    
    # 获取文件信息
    file_info = get_file_info(file_path)
    
    # 构建返回结果
    result = f"文件路径: {file_path}\n"
    if encoding:
        result += f"文件编码: {encoding}\n"
    result += f"{file_info}\n\n"
    result += "文件内容:\n"
    
    # 对大文件进行截断处理
    """ max_display_chars = 20000
    if len(content) > max_display_chars:
        content = content[:max_display_chars] + "\n\n... [内容过长，已截断显示] ..." """
    
    result += content
    print(result)
    return content