import requests
import json
import os
from baseConfig import CONFIG

APP_ID = "9b47f6bb-70b7-4eb8-bac6-ad5299ff43c9"

def read_markdown_file(file_path):
    """读取Markdown文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return ""

def get_api_response(code_str=None, query='给一个例子'):
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
        'input_files': {},
        'query': query,
        'mode': 'workflow',
        "stream_response": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response

if __name__ == "__main__":
    # 当作为脚本运行时，执行API调用并打印结果
    response = get_api_response()
    
    # 打印状态码
    print(f"状态码: {response.status_code}")

    # 打印响应头
    print(response.headers)

    # 打印响应内容
    print(response.text)