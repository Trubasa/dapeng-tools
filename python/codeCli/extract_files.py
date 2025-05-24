#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import re

def extract_files_from_json(input_file, output_file):
    """
    从JSON格式的输入文件中提取文件结构，并保存为纯文本格式
    
    参数:
    input_file (str): 包含JSON数据的输入文件路径
    output_file (str): 要保存提取文件结构的输出文件路径
    """
    # 确保输出目录存在
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        # 读取JSON数据
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 提取answer字段的值
        if 'answer' not in data:
            print(f"错误: 输入JSON中没有找到'answer'字段")
            return False
        
        answer_text = data['answer']
        
        # 使用正则表达式提取文件块
        file_pattern = r'```(?:.*?)\n(===FILE:.*?===ENDFILE===)'
        file_blocks = re.findall(file_pattern, answer_text, re.DOTALL)
        
        # 如果没有找到文件块，尝试直接查找文件标记
        if not file_blocks:
            file_pattern = r'(===FILE:.*?===ENDFILE===)'
            file_blocks = re.findall(file_pattern, answer_text, re.DOTALL)
        
        if not file_blocks:
            print("警告: 没有找到文件块，可能格式不匹配")
            return False
        
        # 将所有提取的文件块写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            for block in file_blocks:
                f.write(block + "\n")
        
        print(f"成功提取了 {len(file_blocks)} 个文件块并保存到 {output_file}")
        return True
        
    except Exception as e:
        print(f"处理过程中出错: {str(e)}")
        return False

def main():
 # 定义输入和输出文件路径
    input_file = "./temp/step1"
    output_file = "./temp/step2"
    
    # 执行提取
    success = extract_files_from_json(input_file, output_file)
    
    if success:
        print("文件结构提取完成!")
    else:
        print("文件结构提取失败!")

if __name__ == "__main__":
   main()