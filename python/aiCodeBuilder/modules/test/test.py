#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import time
from ...utils.getFilePath import select_file, select_directory, save_file


def run():
    """
    运行测试模块，演示文件和目录选择对话框
    
    返回:
        str: 操作结果描述
    """
    results = []
    results.append("=== 文件选择测试模块 ===\n")
    
    # 测试选择文件
    results.append("1. 请选择一个文件")
    file_path = select_file(
        "请选择一个文件", 
        [("文本文件", "*.txt"), ("Python文件", "*.py"), ("所有文件", "*.*")]
    )
    
    if file_path:
        results.append(f"您选择了文件: {file_path}")
        
        # 获取文件信息
        file_size = os.path.getsize(file_path) if os.path.exists(file_path) else 0
        file_mtime = time.ctime(os.path.getmtime(file_path)) if os.path.exists(file_path) else "未知"
        
        results.append(f"文件大小: {file_size} 字节")
        results.append(f"修改时间: {file_mtime}")
    else:
        results.append("您取消了文件选择")
    
    results.append("\n")
    
    # 测试选择目录
    results.append("2. 请选择一个目录")
    dir_path = select_directory("请选择一个目录")
    
    if dir_path:
        results.append(f"您选择了目录: {dir_path}")
        
        # 列出目录中的文件
        try:
            files = os.listdir(dir_path)
            results.append(f"目录中包含 {len(files)} 个项目:")
            for i, item in enumerate(files[:10]):  # 只显示前10个
                item_path = os.path.join(dir_path, item)
                item_type = "目录" if os.path.isdir(item_path) else "文件"
                results.append(f"  {i+1}. {item} ({item_type})")
            
            if len(files) > 10:
                results.append(f"  ... 等 {len(files)-10} 个项目未显示")
        except Exception as e:
            results.append(f"无法列出目录内容: {str(e)}")
    else:
        results.append("您取消了目录选择")
    
    results.append("\n")
    
    # 测试保存文件
    results.append("3. 请选择文件保存位置")
    save_path = save_file(
        "请选择文件保存位置", 
        ".txt", 
        [("文本文件", "*.txt"), ("所有文件", "*.*")],
        initialfile="测试文件.txt"
    )
    
    if save_path:
        results.append(f"您选择了保存路径: {save_path}")
        
        # 尝试写入一些内容到文件
        try:
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write("这是一个测试文件，由文件选择测试模块创建。\n")
                f.write(f"创建时间: {time.ctime()}\n")
            results.append("已成功写入测试内容到文件")
        except Exception as e:
            results.append(f"无法写入文件: {str(e)}")
    else:
        results.append("您取消了文件保存")
    
    # 返回所有结果
    return "\n".join(results)

def main():
    """模块入口点"""
    result = run()
    print(result)
    return result

if __name__ == "__main__":
    main()