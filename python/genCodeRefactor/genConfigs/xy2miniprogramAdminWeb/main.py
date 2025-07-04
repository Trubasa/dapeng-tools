
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import asyncio

# sdk_source_dir = r'G:\code\lsdmxmp-client\node_modules\@everdev\lsdmxmp-client'
# --- 动态添加项目根目录到 sys.path ---
# 这使得我们可以从 genCore 目录导入模块
# 当前文件路径: .../genConfigs/g136Uni/main.py
# 项目根目录: .../
try:
    # 获取当前脚本的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 项目根目录是 genConfigs 目录的父目录
    project_root = os.path.dirname(os.path.dirname(current_dir))
    # 将项目根目录添加到 Python 解释器的模块搜索路径中
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    # --- 导入核心模块 ---
    # 导入配置加载函数，用于读取 config.yaml
    from genCore.loadYaml import load_config
    # 导入 c2m 的核心函数，用于将目录结构转换为 Markdown
    from genCore.c2m import generate_markdown
    # 导入核心处理流程函数
    from genCore.main import run_project_flow

except ImportError as e:
    print(f"无法导入依赖模块，请确保项目结构正确: {e}", file=sys.stderr)
    sys.exit(1)


# 新的主函数，用于自动准备 system prompt 并运行核心流程
async def main():
    """
    此脚本首先准备 'apiParams/system.txt' 文件，然后启动核心代码生成流程。
    它会自动执行以下步骤：
    1. 使用 c2m 读取 'G:\\code\\lsdmxmp-client\\node_modules' 的内容，并保存到 'temp/api_sdk.md'。
    2. 读取本项目的 config.yaml 中的 api_chat_system 内容。
    3. 将 api_chat_system 中的 '{api_sdk}' 占位符替换为 'temp/api_sdk.md' 的文件内容。
    4. 将最终结果保存到 'apiParams/system.txt'。
    5. 调用 run_project_flow 执行项目的主要逻辑。
    """
    # --- 动态获取项目名称 ---
    project_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
    print(f"--- 正在为项目 '{project_name}' 准备 System Prompt 并启动流程 ---")

    # --- 定义相关路径 ---
    project_config_dir = os.path.dirname(os.path.abspath(__file__))
    temp_dir = os.path.join(project_config_dir, 'temp')
    api_sdk_md_path = os.path.join(temp_dir, 'api_sdk.md')
    output_dir = os.path.join(project_config_dir, 'apiParams')
    system_txt_path = os.path.join(output_dir, 'system.txt')

    # --- 确保目录存在 ---
    os.makedirs(temp_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    try:
        # --- 步骤 1: 加载配置 ---
        print("\n[步骤 1/5] 正在加载项目配置...")
        config = load_config(project_name)
        api_chat_system_template = config.get('api', {}).get('api_chat_system', '')
        if not api_chat_system_template:
            print("错误: 在配置中未找到 'api_chat_system' 或其内容为空。", file=sys.stderr)
            sys.exit(1)
        print("配置加载完成。")

        # --- 步骤 2: 使用 c2m 生成 SDK 文档 ---
        """  print(f"\n[步骤 2/5] 正在扫描目录 '{sdk_source_dir}' 以生成SDK文档...")
        if not os.path.isdir(sdk_source_dir):
            print(f"\n错误: 指定的SDK源目录 '{sdk_source_dir}' 不是一个有效的目录。程序退出。", file=sys.stderr)
            sys.exit(1)
        generate_markdown(sdk_source_dir, api_sdk_md_path)
        print(f"SDK文档已成功生成到: {api_sdk_md_path}") """

        # --- 步骤 3: 读取生成的 SDK 文档内容 ---
        print("\n[步骤 3/5] 正在读取SDK文档内容...")
        with open(api_sdk_md_path, 'r', encoding='utf-8') as f:
            api_sdk_content = f.read()
        print("SDK文档内容读取完成。")

        # --- 步骤 4: 替换占位符并生成最终的 System Prompt ---
        print("\n[步骤 4/5] 正在生成最终的 System Prompt...")
        final_system_prompt = api_chat_system_template.replace('{api_sdk}', api_sdk_content)
        
        # 将最终内容保存到 'apiParams/system.txt'
        with open(system_txt_path, 'w', encoding='utf-8') as f:
            f.write(final_system_prompt)
        print(f"最终的 System Prompt 已成功保存到: {system_txt_path}")

        # --- 步骤 5: 运行核心流程 ---
        print("\n[步骤 5/5] System Prompt 准备就绪，正在启动核心代码生成流程...")
        await run_project_flow(project_name)

    except FileNotFoundError as e:
        print(f"\n错误: 文件未找到 - {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n处理过程中发生错误: {e}", file=sys.stderr)
        sys.exit(1)


# 程序的入口点
if __name__ == "__main__":
    try:
        # 使用 asyncio.run 来执行异步的 main 函数
        asyncio.run(main())
    except (KeyboardInterrupt, EOFError):
        # 优雅地处理用户中断 (Ctrl+C)
        print("\n\n操作已由用户取消。程序退出。")
        sys.exit(0)
    except Exception as e:
        print(f'应用程序执行过程中发生严重错误: {e}', file=sys.stderr)
        sys.exit(1)
