#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import os
from testApi5 import get_api_response
from buildFiles import buildFiles
from step1ToStep2 import main as step1ToStep2
from c2m import generate_markdown
from baseConfig import CONFIG

PROJECT_DIR = r"G:\code\g136-miniprogram-uni\src\apps"
CONFIG.file_url = 'https://echoes.devfp.ps.netease.com/file/6836c8acbb4b00c3b5e86a13lvIuMeAi02.png'
QUERY = """
根据设计图的内容描述，迭代 poster-test 这个文件中的 generate 方法

# 注意
* 还原这个布局使用到的一些图片已经在generate函数中有所声明和注释
* 头像需要有一个圆形的黄色边框框住，内容不要溢出这个边框
* 如果遇到需要图片素材的地方，但是目前generate函数中没有，你不需要实现，可以使用 text 类型的 element进行告知，后续我会进行替换
"""
INPUT_DIR = PROJECT_DIR

OUTPUT_DIR = PROJECT_DIR

def api_to_code(query=None, code_str=None):
    """
    从API获取响应并将结果转换为代码文件系统
    
    参数：
    query (str, optional): 发送给API的查询，默认为"给一个例子"
    code_str (str, optional): 要发送给API的代码字符串，默认为None
    """
    # 如果未提供查询，使用默认值
    if query is None:
        query = QUERY
    
    # 获取API响应
    
    print(f"开始BrainMaker API调用...")
    response = get_api_response(code_str, query)
    
    if response.status_code == 200:
        try:
            # 提取响应文本
            response_text = response.text
            response_json = json.loads(response_text)
            # 确保temp目录存在
            temp_dir = "temp"
            if not os.path.exists(temp_dir):
                os.makedirs(temp_dir)
                
            # 将响应文本保存到temp/step1文件中
            step1_file_path = os.path.join(temp_dir, "step1")
            with open(step1_file_path, 'w', encoding='utf-8') as f:
                f.write(response_json.get("output",""))
            print(f"API响应已保存到 {step1_file_path}")

            # 调用step1ToStep2函数
            step1ToStep2()
            print("step1ToStep2函数执行完成。")
            
            # 处理响应文本，创建文件系统
            buildFiles('./temp/step2', OUTPUT_DIR)
            print("文件系统创建成功！请在output目录中查看。")
        except Exception as e:
            print(f"处理API响应时出错: {str(e)}")
    else:
        print(f"API请求失败，状态码: {response.status_code}")
        print(f"响应内容: {response.text}")

if __name__ == "__main__":
    print("提取项目文件到step0.md")
    generate_markdown(INPUT_DIR, "./temp/step0.md")
    print("提取项目文件到step0.md完成")

    # 从命令行参数获取查询（如果有）
    query = sys.argv[1] if len(sys.argv) > 1 else None
    
    # 执行API调用并创建代码
    api_to_code(query)