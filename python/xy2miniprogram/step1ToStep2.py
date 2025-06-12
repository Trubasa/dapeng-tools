#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re

def extract_output_content(input_file, output_file):
    """
    从输入文件中提取<output>...</output>标签之间的内容，并保存到输出文件
    
    参数:
        input_file (str): 输入文件路径 (step1)
        output_file (str): 输出文件路径 (step2)
    
    返回:
        bool: 是否成功提取内容
    """
    try:
        # 读取输入文件内容
        with open(input_file, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        # 查找<output>...</output>之间的内容
        pattern = r'<output>(.*?)</output>'
        # re.DOTALL 标志使 . 能匹配换行符，实现跨行匹配
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            # 提取匹配到的内容
            output_content = '<output>'
            output_content += match.group(1)
            output_content += '</output>'
            
            # 确保输出目录存在
            output_dir = os.path.dirname(output_file)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # 写入输出文件
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(output_content)
            
            print(f"成功提取内容并保存到 {output_file}")
            return True
        else:
            print("错误: 未找到<output>...</output>标签")
            return False
    
    except Exception as e:
        print(f"处理过程中出错: {str(e)}")
        return False

def main():
    """主函数"""
    # 默认使用 temp 目录下的 step1 和 step2 文件
    input_file = "temp/step1"
    output_file = "temp/step2"
    
    # 允许通过命令行参数指定文件
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    # 处理文件路径，如果是相对路径，则相对于脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.isabs(input_file):
        input_file = os.path.join(script_dir, input_file)
    if not os.path.isabs(output_file):
        output_file = os.path.join(script_dir, output_file)
    
    # 提取内容
    success = extract_output_content(input_file, output_file)
    
    # 根据结果设置退出码
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())