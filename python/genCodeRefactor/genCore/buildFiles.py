#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import argparse
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XMLParser

# 全局变量，默认输出目录
output_dir = "output/"
# 存储输出目录的基本名称（用于路径优化）
output_dir_base = "output"

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

def normalize_path(filename):
    """
    规范化文件路径，避免重复的目录名
    例如：如果output_dir是'G:/code/g136-miniprogram-uni/src/'，文件名是'src/apps/test.json'，
    则返回'G:/code/g136-miniprogram-uni/src/apps/test.json'而不是'G:/code/g136-miniprogram-uni/src/src/apps/test.json'
    """
    global output_dir, output_dir_base

    # 将所有斜杠统一成系统标准
    filename = filename.replace('/', os.sep).replace('\\', os.sep)
    
    # 拆分文件路径
    parts = filename.split(os.sep)
    
    # 如果第一部分与output_dir_base相同，则移除
    if parts and parts[0].lower() == output_dir_base.lower():
        # 移除第一部分，保留剩余部分
        parts = parts[1:]
        
    # 组合输出目录和处理后的文件名
    target_path = os.path.join(output_dir, *parts) if parts else output_dir
    
    # 输出调试信息
    print(f"DEBUG: 原始文件名: {filename}, 输出目录: {output_dir}, 基本名称: {output_dir_base}, 最终路径: {target_path}")
    
    return target_path

def process_xml(xml_string):
    """处理XML字符串，提取消息和文件信息"""
    global output_dir, output_dir_base
    
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
                    
                    # 获取原始文件名
                    original_filename = filename_element.text
                    
                    # 规范化路径
                    file_path = normalize_path(original_filename)
                    
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
                        print(f"警告: 文件 {original_filename} 缺少内容元素", file=sys.stderr)
                else:
                    print("警告: 文件元素缺少filename子元素", file=sys.stderr)
        
    except Exception as e:
        print(f"处理XML时出错: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()

def buildFiles(filePath, output):
    """构建文件系统"""
    global output_dir, output_dir_base
    
    if output:
        # 规范化输出目录路径
        output_dir = os.path.normpath(output).replace('\\', os.sep)
        if not output_dir.endswith(os.sep):
            output_dir += os.sep
        
        # 提取输出目录的基本名称 (最后一层目录名)
        output_dir_base = os.path.basename(os.path.normpath(output_dir))

    print(f"输出目录: {output_dir}")
    print(f"基本名称: {output_dir_base}")

    xml_string = ''
    with open(filePath, 'r', encoding='utf-8', errors="replace") as file:
        xml_string = file.read()
    process_xml(xml_string)
    
def main():
    """主函数，从文件读取XML字符串并处理"""
    global output_dir, output_dir_base
    
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
    
    # 更新输出目录的基本名称
    output_dir_base = os.path.basename(os.path.normpath(output_dir))
    
    print(f"使用输出目录: {output_dir} (基本名称: {output_dir_base})")
    
    try:
        buildFiles(args.xml_file, output_dir)
    except FileNotFoundError:
        print(f"错误: 找不到文件 '{args.xml_file}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"读取文件时出错: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()