#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import functools
import inspect
import asyncio
import sys

class FileWriter:
    """
    一个用于将函数返回值写入文件的工具类。
    在使用前，需要用一个基础目录来初始化它。
    然后，它的 `write` 方法可以作为装饰器使用，实现依赖注入，使代码更清晰、可维护。
    """
    def __init__(self, base_dir: str):
        """
        初始化 FileWriter。

        :param base_dir: 所有文件写入操作的基础目录。
        """
        # 获取基础目录的绝对路径，确保路径格式统一
        self.base_dir = os.path.abspath(base_dir)
        # 确保基础目录存在，如果不存在则自动创建
        os.makedirs(self.base_dir, exist_ok=True)
        print(f"--- [FileWriter] 已初始化，基础输出目录: {self.base_dir} ---")

    def write(self, relative_path: str):
        """
        一个装饰器工厂，创建的装饰器会将函数的返回值写入到相对于 base_dir 的指定路径。
        支持同步和异步函数。

        :param relative_path: 相对于初始化时 base_dir 的文件路径。
        """
        # 在装饰器定义时就计算好最终的绝对输出路径
        output_file_path = os.path.join(self.base_dir, relative_path)

        def decorator(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                # 1. 执行被装饰的异步函数
                result = await func(*args, **kwargs)
                
                # 2. 确保输出文件的目录存在
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                
                # 3. 将结果写入文件
                with open(output_file_path, 'w', encoding='utf-8') as f:
                    if isinstance(result, (dict, list)):
                        # 对于字典或列表，使用JSON格式化存储，美观易读
                        json.dump(result, f, ensure_ascii=False, indent=4)
                    else:
                        # 其他类型直接转为字符串存储
                        f.write(str(result))
                
                print(f"--- [FileWriter] 函数 '{func.__name__}' 的异步结果已写入: {output_file_path} ---")
                return result

            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                # 1. 执行被装饰的同步函数
                result = func(*args, **kwargs)
                
                # 2. 确保输出文件的目录存在
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                
                # 3. 将结果写入文件
                with open(output_file_path, 'w', encoding='utf-8') as f:
                    if isinstance(result, (dict, list)):
                        json.dump(result, f, ensure_ascii=False, indent=4)
                    else:
                        f.write(str(result))
                
                print(f"--- [FileWriter] 函数 '{func.__name__}' 的同步结果已写入: {output_file_path} ---")
                return result

            # 根据被装饰函数的类型（是否为协程函数）返回对应的 wrapper
            if inspect.iscoroutinefunction(func):
                return async_wrapper
            else:
                return sync_wrapper
                
        return decorator
