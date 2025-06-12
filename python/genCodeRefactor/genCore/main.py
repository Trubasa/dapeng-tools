#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import sys
import os
import json

# --- 动态添加项目根目录到 sys.path ---
# 这使得我们可以从 genCore 和 genUtils 目录导入模块
# 当前文件路径: .../genCore/main.py
# 项目根目录: .../
try:
    # 获取当前脚本的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 项目根目录是 genCore 目录的父目录
    project_root = os.path.dirname(current_dir)
    # 将项目根目录添加到 Python 解释器的模块搜索路径中
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    # --- 模块导入 ---
    # 使用相对导入，因为这些模块都在 genCore 包内
    from .loadYaml import load_and_merge_yamls
    from .splitContent import extract_content_from_last_single_hash
    from .c2m import generate_markdown
    from .apiClient import get_api_response
    from .extractApiOutput import extract_tagged_content
    from .buildFiles import buildFiles
    from .dirToParams import dir_to_params
    # 从 genUtils 导入
    from genUtils.fileWriter import FileWriter
except ImportError as e:
    print(f"无法导入依赖模块，请确保项目结构正确: {e}", file=sys.stderr)
    sys.exit(1)


# 核心应用流程
async def run_project_flow(project_name: str):
    """
    应用程序的核心处理流程。
    :param project_name: 要处理的项目名称 (例如 'xy2miniprogram')
    """
    print(f'--- 欢迎使用代码生成器 ---')
    print(f'--- 正在处理项目: {project_name} ---')

    # --- 初始化 FileWriter ---
    # 临时文件目录现在位于 genConfigs/{project_name}/temp
    project_root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_base_dir = os.path.join(project_root_dir, 'genConfigs', project_name, 'temp')
    file_writer = FileWriter(base_dir=output_base_dir)
    
    # --- 步骤 1: 初始化应用程序并使用装饰器写入文件 ---
    print('\n步骤 1: 初始化应用程序...')
    
    @file_writer.write('config_output.json')
    async def get_and_save_config(proj_name: str) -> dict:
        """
        初始化指定项目的配置。
        """
        print(f'执行初始化逻辑: 为项目 "{proj_name}" 加载YAML配置文件...')
        configs_root = os.path.join(project_root_dir, 'genConfigs')
        base_config_path = os.path.join(configs_root, 'config.yaml')
        project_config_path = os.path.join(configs_root, proj_name, 'config.yaml')
        config_files = [base_config_path, project_config_path]
        print(f"将要加载的配置文件: {config_files}")
        config = load_and_merge_yamls(config_files)
        config['project']['config_dir'] = os.path.join(configs_root, proj_name)
        config['project']['chat_history_file_path'] = os.path.join(config['project']['config_dir'],config['project']['chat_history_file'])
        await asyncio.sleep(0.1)
        return config

    app_config = await get_and_save_config(project_name)
    print('初始化完成。')

    # --- 步骤 2: 获取聊天内容并使用装饰器写入文件 ---
    print('\n步骤 2: 获取最新的聊天内容...')

    @file_writer.write('chat_content_output.json')
    def get_and_save_chat_content(config: dict) -> dict:
        """
        根据配置读取指定的聊天记录文件，并提取最后一个'#'之后的内容。
        """
        chat_history_path = config.get('project', {}).get('chat_history_file_path')
        if not chat_history_path or not os.path.exists(chat_history_path):
            error_msg = f"聊天记录文件不存在或未配置: {chat_history_path}"
            print(f"错误: {error_msg}")
            return {"content": error_msg, "imgDict": {}}
        return extract_content_from_last_single_hash(chat_history_path)

    chat_content = get_and_save_chat_content(app_config)
    content_preview = str(chat_content.get('content', ''))[:50].replace('\n', ' ')
    print(f"获取到的聊天内容 (预览): '{content_preview}...'")
    print('获取聊天内容完成。')

    # --- 步骤 3: 将项目目录转换为Markdown并读取内容 ---
    print('\n步骤 3: 提取目标项目结构...')
    project_dir = app_config.get('project', {}).get('dir')
    project_structure_md_path = os.path.join(output_base_dir, 'project_structure.md')
    
    code_str_content = ""

    if project_dir and os.path.isdir(project_dir):
        print(f"正在将目录 '{project_dir}' 的内容转换为Markdown...")
        generate_markdown(directory=project_dir, output_file=project_structure_md_path)
        print(f"项目结构已成功提取到: {project_structure_md_path}")
        
        try:
            with open(project_structure_md_path, 'r', encoding='utf-8') as f:
                code_str_content = f.read()
            print("已成功读取项目结构内容用于API请求。")
        except FileNotFoundError:
            print(f"警告: 未找到生成的代码结构文件 {project_structure_md_path}，'codeStr' 参数将为空。")

    else:
        print(f"警告: 项目目录 '{project_dir}' 无效或未配置，跳过项目结构提取。")
    print('提取项目结构完成。')


    # --- 步骤 4: 调用 BrainMaker API ---
    print('\n步骤 4: 调用 BrainMaker API...')
    
    api_inputs = {}
    api_params_dir_name = app_config.get('api', {}).get('api_params_dir')
    project_config_dir = app_config.get('project', {}).get('config_dir')

    if api_params_dir_name and project_config_dir:
        api_params_path = os.path.join(project_config_dir, api_params_dir_name)
        if os.path.isdir(api_params_path):
            print(f"正在从 API 参数目录 '{api_params_path}' 加载初始输入...")
            api_inputs = dir_to_params(api_params_path)
            print(f"已成功加载 {len(api_inputs)} 个文件作为初始 API 输入。")
        else:
            print(f"信息: API 参数目录 '{api_params_path}' 未找到，'inputs' 初始为空。")
    else:
        print("信息: 配置中未指定 'api_params_dir'，'inputs' 初始为空。")

    api_inputs['codeStr'] = code_str_content
    api_inputs['query'] = chat_content.get('content', '')

    system_prompt = app_config.get('api', {}).get('api_chat_system', '')
    if not system_prompt:
        print("警告: 'api_chat_system' 在配置中为空或未定义，API可能无法按预期工作。")
    api_inputs["system"] = system_prompt

    chat_query = chat_content.get('content', '')
    
    api_call_successful = False

    if not chat_query or "错误:" in chat_query:
        print(f"错误: 无效的聊天查询内容，跳过API调用。 - {chat_query}")
    else:
        img_dict = chat_content.get("imgDict", {})
        api_input_files = img_dict
        
        print("正在将API请求参数保存到临时文件...")
        api_request_payload = {
            'query': chat_query,
            'inputs': api_inputs,
            'input_files': api_input_files
        }
        api_request_payload_path = os.path.join(output_base_dir, 'api_request_payload.json')
        try:
            with open(api_request_payload_path, 'w', encoding='utf-8') as f:
                json.dump(api_request_payload, f, ensure_ascii=False, indent=4)
            print(f"API 请求参数已成功保存到: {api_request_payload_path}")
        except Exception as e:
            print(f"警告: 保存API请求参数时发生错误: {e}", file=sys.stderr)

        try:
            api_response = await asyncio.to_thread(
                get_api_response,
                config=app_config,
                query=chat_query,
                inputs=api_inputs,
                input_files=api_input_files
            )

            if api_response.status_code == 200:
                response_json = api_response.json()
                
                api_response_path = os.path.join(output_base_dir, 'api_response.json')
                with open(api_response_path, 'w', encoding='utf-8') as f:
                    json.dump(response_json, f, ensure_ascii=False, indent=4)
                print(f"完整的 API 响应已保存到: {api_response_path}")

                api_output_text = response_json.get("output", "")
                
                tagged_content = extract_tagged_content(api_output_text)
                
                if tagged_content:
                    extracted_output_path = os.path.join(output_base_dir, 'api_extracted_output.xml')
                    with open(extracted_output_path, 'w', encoding='utf-8') as f:
                        f.write(tagged_content)
                    print(f"已成功提取 <ai-api-output> 内容并保存到: {extracted_output_path}")
                    api_call_successful = True
                else:
                    print("警告: 在API响应的 'output' 字段中未找到 <ai-api-output> 标签。后续步骤将被跳过。")
                
            else:
                print(f"API 请求失败，状态码: {api_response.status_code}\n响应内容: {api_response.text}")
        except Exception as e:
            print(f"API 调用或响应处理过程中发生严重错误: {e}", file=sys.stderr)

    print('API调用步骤完成。')

    if api_call_successful:
        print('\n步骤 5: 构建或更新项目文件...')
        extracted_output_path = os.path.join(output_base_dir, 'api_extracted_output.xml')
        target_project_dir = app_config.get('project', {}).get('dir')

        if os.path.exists(extracted_output_path) and target_project_dir:
            print(f"正在使用 '{extracted_output_path}' 的内容更新目标目录: '{target_project_dir}'")
            try:
                buildFiles(extracted_output_path, target_project_dir)
                print("项目文件构建成功！")
            except Exception as e:
                print(f"文件构建过程中发生错误: {e}", file=sys.stderr)
        elif not os.path.exists(extracted_output_path):
            print(f"警告: 未找到API提取的输出文件 '{extracted_output_path}'，跳过文件构建步骤。")
        else:
            print("警告: 未配置目标项目目录，跳过文件构建步骤。")
        print('文件构建步骤完成。')
    else:
        print('\n由于API调用失败或未返回有效数据，已跳过文件构建步骤。')


    print('\n--- 程序执行结束 ---')

# 程序的入口点，用于直接测试 genCore/main.py
if __name__ == "__main__":
    # 这是一个示例，展示如何直接运行核心流程
    # 在实际使用中，应该由 genConfigs/xxx/main.py 来调用
    import argparse
    parser = argparse.ArgumentParser(description='运行指定项目的代码生成流程。')
    parser.add_argument('project_name', help='要执行的项目名称 (例如: xy2miniprogram)')
    args = parser.parse_args()
    
    try:
        asyncio.run(run_project_flow(args.project_name))
    except Exception as e:
        print(f'应用程序执行过程中发生严重错误: {e}', file=sys.stderr)
        sys.exit(1)
