#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import os
import argparse
# 导入重构后的API客户端
from genCore.apiClient import get_api_response
from buildFiles import buildFiles
# 重命名导入，使其更具可读性
from extractApiOutput import main as run_api_output_extraction
from c2m import generate_markdown
# 导入新的配置加载模块
from loadYaml import load_config
# 导入内容提取函数
from genCore.splitContent import extract_content_from_last_single_hash

# --- 主逻辑 ---

def api_to_code(config):
    """
    从API获取响应并将结果转换为代码文件系统
    """
    # 从配置文件中获取路径
    project_dir = config['project']['dir']
    
    # --- 提取需求内容和图片 ---
    chat_history_path = config.get('project', {}).get('chat_history_file_path')
    if not chat_history_path or not os.path.exists(chat_history_path):
        print(f"错误: 聊天记录文件不存在或未配置 - {chat_history_path}", file=sys.stderr)
        return

    input_obj = extract_content_from_last_single_hash(chat_history_path)
    query = input_obj.get("content")
    
    if not query or "错误:" in query:
        print(f"未能提取有效的查询内容: {query}", file=sys.stderr)
        return

    img_dict = input_obj.get("imgDict", {})
    file_url = next(iter(img_dict.values()), None)

    # --- 提取项目代码结构 ---
    print("提取项目文件到 temp/step0.md")
    step0_md_path = os.path.join("temp", "step0.md")
    generate_markdown(project_dir, step0_md_path)
    print("提取项目文件到 temp/step0.md 完成")

    # 读取生成的 markdown 文件内容以传递给API
    try:
        with open(step0_md_path, 'r', encoding='utf-8') as f:
            code_str = f.read()
    except FileNotFoundError:
        print(f"错误: 未找到生成的代码结构文件 {step0_md_path}", file=sys.stderr)
        return

    # --- 调用API ---
    # 将图片URL设置到配置中，以便API调用时使用
    config['api']['file_url'] = file_url if file_url else ''

    print(f"开始BrainMaker API调用...")
    try:
        # 调用重构后的函数，并传入所有必需的参数
        response = get_api_response(config, code_str, query)
    except Exception as e:
        print(f"API调用失败: {e}", file=sys.stderr)
        return
    
    # --- 处理API响应 ---
    if response.status_code == 200:
        try:
            response_json = response.json()
            temp_dir = "temp"
            os.makedirs(temp_dir, exist_ok=True)
                
            step1_file_path = os.path.join(temp_dir, "step1")
            with open(step1_file_path, 'w', encoding='utf-8') as f:
                f.write(response_json.get("output",""))
            print(f"API响应已保存到 {step1_file_path}")

            # 调用重命名后的模块主函数
            run_api_output_extraction()
            print("API 响应提取完成。")
            
            # 使用项目目录作为输出目录
            buildFiles('./temp/step2', project_dir)
            print(f"文件系统创建成功！请在 {project_dir} 目录中查看。")
        except Exception as e:
            print(f"处理API响应时出错: {str(e)}")
    else:
        print(f"API请求失败，状态码: {response.status_code}")
        print(f"响应内容: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='根据指定项目的配置，生成或重构代码。')
    parser.add_argument('project_name', help='要执行的项目名称 (例如: dapeng-miniprogram)')
    args = parser.parse_args()

    # 使用新的配置加载函数
    config = load_config(args.project_name)
    
    # 执行主流程
    api_to_code(config)
