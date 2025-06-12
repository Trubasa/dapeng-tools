
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import sys
import os
import json

# --- 动态添加项目根目录到 sys.path ---
# 这使得我们可以从 genCode 和 genUtils 目录导入模块
# 当前文件路径: .../genConfigs/xy2miniprogram/main.py
# 项目根目录: .../
try:
    # 获取当前脚本的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 项目根目录是 genConfigs 目录的父目录
    project_root = os.path.dirname(os.path.dirname(current_dir))
    # 将项目根目录添加到 Python 解释器的模块搜索路径中
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    # --- 修改导入 ---
    # 从 genCore 导入所需模块
    from genCore.loadYaml import load_and_merge_yamls
    from genCore.splitContent import extract_content_from_last_single_hash
    from genUtils.fileWriter import FileWriter
    # 导入代码转Markdown的模块
    from genCore.c2m import generate_markdown
    # 导入重构后的API客户端
    from genCore.apiClient import get_api_response
    # 导入API响应内容提取函数
    from genCore.extractApiOutput import extract_tagged_content
    # 新增: 导入文件构建函数
    from genCore.buildFiles import buildFiles
    # 新增: 导入将目录转换为参数字典的函数
    from genCore.dirToParams import dir_to_params
except ImportError as e:
    print(f"无法导入依赖模块，请确保项目结构正确: {e}", file=sys.stderr)
    sys.exit(1)


# xy2miniprogram 主入口文件
async def main():
    """
    应用程序主函数
    """
    print('--- 欢迎使用 xy2miniprogram 启动程序 ---')

    # --- 初始化 FileWriter ---
    # 定义所有临时输出文件的基础目录。
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    output_base_dir = os.path.join(current_script_dir, 'temp')
    # 创建一个 FileWriter 实例，后续的装饰器都将使用这个实例
    file_writer = FileWriter(base_dir=output_base_dir)
    
    # --- 步骤 1: 初始化应用程序并使用装饰器写入文件 ---
    print('\n步骤 1: 初始化应用程序...')
    
    @file_writer.write('config_output.json')
    async def get_and_save_config(project_name: str) -> dict:
        """
        初始化指定项目的配置。
        """
        print(f'执行初始化逻辑: 为项目 "{project_name}" 加载YAML配置文件...')
        project_root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        configs_root = os.path.join(project_root_dir, 'genConfigs')
        base_config_path = os.path.join(configs_root, 'config.yaml')
        project_config_path = os.path.join(configs_root, project_name, 'config.yaml')
        config_files = [base_config_path, project_config_path]
        print(f"将要加载的配置文件: {config_files}")
        config = load_and_merge_yamls(config_files)
        config['project']['config_dir'] = os.path.join(configs_root, project_name)
        config['project']['chat_history_file_path'] = os.path.join(config['project']['config_dir'],config['project']['chat_history_file'])
        await asyncio.sleep(0.1)
        return config

    app_config = await get_and_save_config('xy2miniprogram')
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
    
    # 初始化 codeStr 内容变量，确保其有默认值
    code_str_content = ""

    if project_dir and os.path.isdir(project_dir):
        print(f"正在将目录 '{project_dir}' 的内容转换为Markdown...")
        generate_markdown(directory=project_dir, output_file=project_structure_md_path)
        print(f"项目结构已成功提取到: {project_structure_md_path}")
        
        # 读取生成的 markdown 文件内容以传递给API
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
    
    # 1. 准备 `inputs` 参数 (初始值来自 api_params_dir)
    api_inputs = {}
    # 从配置中获取 api_params_dir 的相对路径名
    api_params_dir_name = app_config.get('api', {}).get('api_params_dir')
    # 获取当前项目配置的根目录
    project_config_dir = app_config.get('project', {}).get('config_dir')

    if api_params_dir_name and project_config_dir:
        # 构造 api_params_dir 的绝对路径
        api_params_path = os.path.join(project_config_dir, api_params_dir_name)
        if os.path.isdir(api_params_path):
            print(f"正在从 API 参数目录 '{api_params_path}' 加载初始输入...")
            api_inputs = dir_to_params(api_params_path)
            print(f"已成功加载 {len(api_inputs)} 个文件作为初始 API 输入。")
        else:
            # 这是一个正常的流程，该目录可能不存在
            print(f"信息: API 参数目录 '{api_params_path}' 未找到，'inputs' 初始为空。")
    else:
        # 这也是一个正常的流程
        print("信息: 配置中未指定 'api_params_dir'，'inputs' 初始为空。")

    # 将项目结构Markdown内容作为 'codeStr' 参数传入
    api_inputs['codeStr'] = code_str_content
    api_inputs['query'] = chat_content.get('content', '')

    # --- 修改: 从配置中获取 system prompt ---
    # system prompt 现在直接从合并后的配置中读取，而不是从 apiParams 目录的文件中加载
    system_prompt = app_config.get('api', {}).get('api_chat_system', '')
    if not system_prompt:
        print("警告: 'api_chat_system' 在配置中为空或未定义，API可能无法按预期工作。")
    api_inputs["system"] = system_prompt

    # 2. 准备 `query` 参数 (来自聊天内容)
    chat_query = chat_content.get('content', '')
    
    # --- 新增: API调用成功标志，用于控制后续流程 ---
    api_call_successful = False

    if not chat_query or "错误:" in chat_query:
        print(f"错误: 无效的聊天查询内容，跳过API调用。 - {chat_query}")
    else:
        # 3. 准备 `input_files` 参数 (来自聊天内容中的图片)
        img_dict = chat_content.get("imgDict", {})
        api_input_files = img_dict
        
        # --- 新增: 保存API请求参数到文件，用于调试 ---
        print("正在将API请求参数保存到临时文件...")
        api_request_payload = {
            'query': chat_query,
            'inputs': api_inputs,
            'input_files': api_input_files
        }
        api_request_payload_path = os.path.join(output_base_dir, 'api_request_payload.json')
        try:
            with open(api_request_payload_path, 'w', encoding='utf-8') as f:
                # 使用 json.dump 保存字典，格式化输出以便阅读
                json.dump(api_request_payload, f, ensure_ascii=False, indent=4)
            print(f"API 请求参数已成功保存到: {api_request_payload_path}")
        except Exception as e:
            # 即使保存失败，也只打印警告，不中断主流程
            print(f"警告: 保存API请求参数时发生错误: {e}", file=sys.stderr)

        try:
            # 使用 asyncio.to_thread 在异步事件循环中运行同步的、阻塞的API调用
            api_response = await asyncio.to_thread(
                get_api_response,
                config=app_config,
                query=chat_query,
                inputs=api_inputs,
                input_files=api_input_files
            )

            # 4. 处理API响应
            if api_response.status_code == 200:
                response_json = api_response.json()
                
                # 将完整的API响应保存为JSON文件，以便调试和追溯
                api_response_path = os.path.join(output_base_dir, 'api_response.json')
                with open(api_response_path, 'w', encoding='utf-8') as f:
                    json.dump(response_json, f, ensure_ascii=False, indent=4)
                print(f"完整的 API 响应已保存到: {api_response_path}")

                # 从响应中获取包含待提取内容的文本
                api_output_text = response_json.get("output", "")
                
                # 提取 <ai-api-output> 标签内容
                tagged_content = extract_tagged_content(api_output_text) # 默认提取 <ai-api-output>
                
                if tagged_content:
                    # 将提取出的内容保存到新文件，以便后续处理
                    extracted_output_path = os.path.join(output_base_dir, 'api_extracted_output.xml')
                    with open(extracted_output_path, 'w', encoding='utf-8') as f:
                        f.write(tagged_content)
                    print(f"已成功提取 <ai-api-output> 内容并保存到: {extracted_output_path}")
                    # 仅在成功提取内容后，才将标志位置为 True
                    api_call_successful = True
                else:
                    # 即使找不到标签，也只是警告，不中断流程
                    print("警告: 在API响应的 'output' 字段中未找到 <ai-api-output> 标签。后续步骤将被跳过。")
                
            else:
                # API请求失败，打印错误信息，后续步骤将因 api_call_successful 为 False 而被跳过
                print(f"API 请求失败，状态码: {api_response.status_code}\n响应内容: {api_response.text}")
        except Exception as e:
            # API调用异常，打印错误信息，后续步骤将因 api_call_successful 为 False 而被跳过
            print(f"API 调用或响应处理过程中发生严重错误: {e}", file=sys.stderr)

    print('API调用步骤完成。')

    # --- 新增步骤 5: 根据API输出构建文件 (仅在API调用成功时执行) ---
    if api_call_successful:
        print('\n步骤 5: 构建或更新项目文件...')
        extracted_output_path = os.path.join(output_base_dir, 'api_extracted_output.xml')
        target_project_dir = app_config.get('project', {}).get('dir')

        if os.path.exists(extracted_output_path) and target_project_dir:
            print(f"正在使用 '{extracted_output_path}' 的内容更新目标目录: '{target_project_dir}'")
            try:
                # 调用 buildFiles 函数，它会处理文件的创建、修改和删除
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
        # 如果API调用不成功，则明确告知用户跳过文件构建
        print('\n由于API调用失败或未返回有效数据，已跳过文件构建步骤。')


    print('\n--- 程序执行结束 ---')

# 程序的入口点
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f'应用程序执行过程中发生严重错误: {e}', file=sys.stderr)
        sys.exit(1)
