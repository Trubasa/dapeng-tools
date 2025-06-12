#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import argparse
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XMLParser

# 全局变量，默认输出目录
output_dir = "output/"

def ensure_directory_exists(file_path):
    """确保文件所在目录存在"""
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

def delete_file(file_path):
    """删除文件，如果存在的话"""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"文件已删除: {file_path}")
        else:
            print(f"无需删除: 文件不存在 {file_path}")
        return True
    except Exception as e:
        print(f"删除文件时出错: {file_path} - {e}", file=sys.stderr)
        return False

def process_xml(xml_string):
    """处理XML字符串，提取消息和文件信息"""
    global output_dir
    
    try:
        # 解析XML
        root = ET.fromstring(xml_string)
        
        # 获取并打印消息
        message_element = root.find("message")
        if message_element is not None and message_element.text:
            print(message_element.text)
        
        # 处理文件
        files_element = root.find("files")
        if files_element is not None:
            for file_element in files_element.findall("file"):
                filename_element = file_element.find("filename")
                content_element = file_element.find("content")
                
                if filename_element is not None:
                    # 检查filename元素是否有action属性
                    action = filename_element.get("action", "").lower()
                    # 使用全局变量output_dir而不是硬编码的"output/"
                    file_path = os.path.join(output_dir, filename_element.text)
                    
                    if action == "delete":
                        # 删除文件
                        delete_file(file_path)
                    elif content_element is not None:
                        # 创建或更新文件
                        content = content_element.text if content_element.text else ""
                        
                        # 确保目录存在
                        ensure_directory_exists(file_path)
                        
                        # 写入文件内容
                        with open(file_path, 'w', encoding='utf-8', errors="replace") as f:
                            f.write(content)
                        
                        print(f"文件已创建: {file_path}")
                    else:
                        print(f"警告: 文件 {filename_element.text} 缺少内容元素", file=sys.stderr)
                else:
                    print("警告: 文件元素缺少filename子元素", file=sys.stderr)
        
    except Exception as e:
        print(f"处理XML时出错: {e}", file=sys.stderr)

def buildFiles(filePath,output):
    """构建文件系统"""
    if output:
       global output_dir 
       output_dir = output

    xml_string = ''
    with open(filePath, 'r', encoding='utf-8', errors="replace") as file:
        xml_string = file.read()
    process_xml(xml_string)
    
        

def main():
    """主函数，从文件读取XML字符串并处理"""
    global output_dir
    
    # 使用argparse处理命令行参数
    parser = argparse.ArgumentParser(description='处理XML文件并创建或删除指定的文件结构')
    parser.add_argument('xml_file', help='要处理的XML文件路径')
    parser.add_argument('-o', '--output-dir', dest='output_dir', default='output',
                      help='输出文件的基础目录 (默认: output)')
    
    args = parser.parse_args()
    
    # 设置输出目录
    output_dir = args.output_dir
    # 确保输出目录路径以分隔符结尾
    if not output_dir.endswith(os.sep):
        output_dir += os.sep
    
    print(f"使用输出目录: {output_dir}")
    
    try:
        buildFiles(args.xml_file,output_dir)
    except FileNotFoundError:
        print(f"错误: 找不到文件 '{args.xml_file}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"读取文件时出错: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()