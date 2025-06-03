import requests
import json
import os
import time
import sys
from baseConfig import CONFIG

APP_ID = CONFIG.app_id

def read_markdown_file(file_path):
    """读取Markdown文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return ""

def get_api_response(code_str=None, query='给一个例子'):
    print('file_url',CONFIG.file_url);
    """从API获取响应"""
    if code_str is None:
        # 获取temp/step0.md的路径
        current_dir = os.path.dirname(os.path.abspath(__file__))
        md_file_path = os.path.join(current_dir, 'temp', 'step0.md')
        
        # 读取Markdown文件内容
        code_str = read_markdown_file(md_file_path)
        print(f"已从 {md_file_path} 读取内容，长度: {len(code_str)} 字符")
        
    url = f'{CONFIG.api_url}/api/v1/apps/{APP_ID}/chat'

    headers = {
        'X-Auth-User': CONFIG.user_crop,
        'X-Access-Token': CONFIG.access_token,
        'Content-Type': 'application/json'
    }

    data = {
        'inputs': {
          "codeStr": code_str,
          "query": query
        },
        'input_files': {
        },
        'query': query,
        'mode': 'workflow',
        "stream_response": False
    }

    if CONFIG.file_url:
        data['input_files']['img'] = CONFIG.file_url
    
    # 显示API调用开始
    print("开始调用API...", flush=True)
    
    # 记录开始时间
    start_time = time.time()
    
    # 创建一个线程来更新时间显示
    try:
        # 发送请求，同时在等待响应的过程中显示经过的时间
        from threading import Thread
        from queue import Queue
        
        response_queue = Queue()
        exception_queue = Queue()
        
        def make_request():
            try:
                resp = requests.post(url, headers=headers, data=json.dumps(data))
                response_queue.put(resp)
            except Exception as e:
                exception_queue.put(e)
        
        # 启动请求线程
        request_thread = Thread(target=make_request)
        request_thread.daemon = True
        request_thread.start()
        
        # 主线程显示经过的时间
        while request_thread.is_alive():
            elapsed = time.time() - start_time
            # \r 使光标回到行首，输出内容会覆盖当前行
            # end='' 防止print自动换行
            # flush=True 确保即时显示
            print(f"API调用进行中... 已经过 {elapsed:.1f} 秒", end='\r', flush=True)
            time.sleep(0.1)  # 小的延迟，避免过于频繁的刷新
        
        # 检查是否有异常
        if not exception_queue.empty():
            raise exception_queue.get()
        
        # 获取响应
        response = response_queue.get()
        
    except KeyboardInterrupt:
        print("\nAPI调用被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\nAPI调用出错: {str(e)}")
        sys.exit(1)
        
    # 计算总耗时
    total_time = time.time() - start_time
    
    # 清除进度显示行并显示完成信息
    print(" " * 80, end='\r')  # 清除当前行
    print(f"API调用完成! 总耗时: {total_time:.2f} 秒")
    
    return response

if __name__ == "__main__":
    # 当作为脚本运行时，执行API调用并打印结果
    response = get_api_response()
    
    # 打印状态码
    print(f"状态码: {response.status_code}")

    # 打印响应信息
    print(f"响应类型: {response.headers.get('Content-Type', '未知')}")

    # 打印响应内容
    try:
        json_response = response.json()
        # 如果是JSON，则尝试格式化输出
        print("响应内容:")
        print(json.dumps(json_response, indent=2, ensure_ascii=False))
    except:
        # 如果不是JSON，则直接输出文本
        print("响应内容:")
        print(response.text)