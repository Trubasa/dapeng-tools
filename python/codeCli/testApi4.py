import requests
import json
from baseConfig import CONFIG
from files.g123_admin_web import text

APP_ID = "9f8c6f26-6782-487e-b0b3-a1d1cecaff36"

def get_api_response(code_str=None, query='给一个例子'):
    """从API获取响应"""
    if code_str is None:
        code_str = text
        
    url = f'{CONFIG.api_url}/api/v1/apps/{APP_ID}/chat'

    headers = {
        'X-Auth-User': CONFIG.user_crop,
        'X-Access-Token': CONFIG.access_token,
        'Content-Type': 'application/json'
    }

    data = {
        'inputs': {
          "codeStr": code_str
        },
        'input_files': {},
        'query': query,
        'mode': 'advanced-chat',
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