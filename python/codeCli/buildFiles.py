# -*- coding: utf-8 -*-
import os
import sys
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XMLParser

def ensure_directory_exists(file_path):
    """确保文件所在目录存在"""
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

def process_xml(xml_string):
    """处理XML字符串，提取消息和文件信息"""
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
                
                if filename_element is not None and content_element is not None:
                    filename = "gggggg/" + filename_element.text
                    content = content_element.text if content_element.text else ""
                    
                    # 确保目录存在
                    ensure_directory_exists(filename)
                    
                    # 写入文件内容
                    with open(filename, 'w', encoding='utf-8', errors="replace") as f:
                        f.write(content)
                    
                    print(f"文件已创建: {filename}")
        
    except Exception as e:
        print(f"处理XML时出错: {e}", file=sys.stderr)

def main():
    """主函数，从文件读取XML字符串并处理"""
    if len(sys.argv) < 2:
        print("用法: python script.py <xml文件路径>", file=sys.stderr)
        sys.exit(1)
    
    xml_file_path = sys.argv[1]
    
    try:
        with open(xml_file_path, 'r', encoding='utf-8', errors="replace") as file:
            xml_string = file.read()
        process_xml(xml_string)
    except FileNotFoundError:
        print(f"错误: 找不到文件 '{xml_file_path}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"读取文件时出错: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()