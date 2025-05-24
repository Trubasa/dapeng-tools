import requests
import json
from baseConfig import CONFIG

url = f'{CONFIG.api_url}/api/v1/apps/84542c17-6642-4eeb-ae86-25258f57cc89/chat'

headers = {
    'X-Auth-User':CONFIG.user_crop,
    'X-Access-Token':CONFIG.access_token,
    'Content-Type': 'application/json'
}

data = {
    'inputs': {
      "input": "说几句话夸夸我"
    },
    'input_files': {},
    'mode': 'workflow',
    "stream_response":False
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# 打印状态码
print(response.status_code)

# 打印响应头
print(response.headers)

# 打印响应内容
print(response.text)