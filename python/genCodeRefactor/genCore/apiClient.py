
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import time
import sys
from threading import Thread
from queue import Queue

def get_api_response(config: dict, query: str, inputs: dict, input_files: dict):
    """
    调用 BrainMaker API 获取响应。
    这是一个阻塞函数，它会等待API返回结果。

    :param config: 包含API和认证信息的配置字典。
    :param query: 用户的具体请求或问题。
    :param inputs: 一个字典，包含传递给API的文本输入，例如 { "file1.ts": "...", "file2.py": "..." }。
    :param input_files: 一个字典，包含传递给API的文件URL输入，例如 { "img": "http://..." }。
    :return: requests.Response 对象。
    """
    # --- 从配置中获取API和认证信息 ---
    api_config = config.get('api', {})
    auth_config = config.get('auth', {})
    app_id = api_config.get('app_id')
    api_url = api_config.get('url')
    user_crop = auth_config.get('user_crop')
    access_token = auth_config.get('access_token')

    if not all([app_id, api_url, user_crop, access_token]):
        # 抛出异常而不是直接退出，让调用方决定如何处理错误
        raise ValueError("配置中缺少必要的API或认证信息。")

    url = f'{api_url}/api/v1/apps/{app_id}/chat'

    headers = {
        'X-Auth-User': user_crop,
        'X-Access-Token': access_token,
        'Content-Type': 'application/json'
    }

    # --- 使用传入的参数构建请求体 ---
    data = {
        'inputs': inputs,
        'input_files': input_files,
        'query': query,
        'mode': 'workflow',
        "stream_response": False
    }

    print(f"API 请求参数 query (预览): \n {query[:200]}...")
    print(f"API 请求参数 inputs 包含 {len(inputs)} 个文件。")
    if input_files:
        print(f"API 请求参数 input_files: \n {json.dumps(input_files, indent=2)}")


    print("开始调用API...", flush=True)
    start_time = time.time()
    
    response_queue = Queue()
    exception_queue = Queue()
    
    def make_request():
        """在单独的线程中执行网络请求"""
        try:
            # 增加超时以防止无限期挂起
            resp = requests.post(url, headers=headers, data=json.dumps(data), timeout=300)
            response_queue.put(resp)
        except Exception as e:
            exception_queue.put(e)
    
    request_thread = Thread(target=make_request)
    request_thread.daemon = True
    request_thread.start()
    
    # 在主线程等待时显示进度
    while request_thread.is_alive():
        elapsed = time.time() - start_time
        print(f"API调用进行中... 已耗时 {elapsed:.1f} 秒", end='\r', flush=True)
        time.sleep(0.1)
    
    print(" " * 80, end='\r') # 清除进度行

    # --- 检查线程执行结果 ---
    if not exception_queue.empty():
        e = exception_queue.get()
        print(f"\nAPI调用期间发生异常: {str(e)}")
        raise e # 重新抛出异常
    
    if response_queue.empty():
        print("\nAPI调用超时或未返回任何响应。")
        raise requests.exceptions.Timeout("API call timed out or did not return a response.")

    response = response_queue.get()
    total_time = time.time() - start_time
    print(f"API调用完成! 总耗时: {total_time:.2f} 秒")
    
    return response

if __name__ == "__main__":
    print("这是一个API客户端模块，请通过其他脚本导入并使用 `get_api_response` 函数。")
    sys.exit(1)
