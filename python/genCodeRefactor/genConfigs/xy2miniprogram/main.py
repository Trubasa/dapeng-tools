#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import sys
import os

# --- 动态添加项目根目录到 sys.path ---
# 这使得我们可以从 genCore 目录导入模块
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
    
    # 从 genCore 导入核心流程函数
    from genCore.main import run_project_flow

except ImportError as e:
    print(f"无法导入依赖模块，请确保项目结构正确且 genCore/main.py 存在: {e}", file=sys.stderr)
    sys.exit(1)


# xy2miniprogram 项目的启动入口
async def main():
    """
    此项目的特定启动函数。
    它调用通用的核心流程，并传入本项目的名称。
    """
    # --- 动态获取项目名称 ---
    # 通过获取当前文件所在目录的名称，自动确定项目名称。
    # 例如，如果文件在 '.../xy2miniprogram/main.py'，项目名称就是 'xy2miniprogram'。
    # 这样做可以避免硬编码，当复制项目目录以创建新项目时，无需手动修改此处的代码。
    project_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
    
    # 调用核心处理流程
    await run_project_flow(project_name)


# 程序的入口点
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f'应用程序执行过程中发生严重错误: {e}', file=sys.stderr)
        sys.exit(1)
