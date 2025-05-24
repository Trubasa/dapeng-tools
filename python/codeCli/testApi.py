import requests
import json
import os
import sys
import subprocess

APP_ID = "84542c17-6642-4eeb-ae86-25258f57cc89"
USER_CROP = 'hezhipeng'
ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiIsImtpZCI6IjE2Nzg4NjMwODEiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE3NDgzMTI1MDIsImhvc3RpZCI6NDk2NCwiaXN0IjoxNzQ3NzA3NzAyLCJwcm9qZWN0IjoiZGVwMzA1IiwidXNlciI6ImhlemhpcGVuZyJ9.nfn5Ed1KgH08ssy8nIYf3lmnU-2d3tfGNzsotMQ1Ges'
QUERY = "请转为vue3项目"
CODE_FILE_URL = r"C:\Users\hezhipeng\Downloads\workplace\g136_admin_web.md"

# 检查codeCli.py是否存在
code_cli_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".", "codeCli.py")
if not os.path.exists(code_cli_path):
    print(f"错误: 无法找到codeCli.py，请确保它位于: {code_cli_path}")
    sys.exit(1)

def call_api():
    """调用API并获取响应"""
    url = f'https://ext-idc-ai.nie.netease.com/api/v1/apps/{APP_ID}/chat'
    
    # 从环境变量或配置文件获取认证信息更安全
    # 这里只是示例，实际使用时请替换为真实凭证
    # user_crop = input("请输入用户凭证 (X-Auth-User): ")
    user_crop = USER_CROP
    # access_token = input("请输入访问令牌 (X-Access-Token): ")
    access_token = ACCESS_TOKEN
    
    headers = {
        'X-Auth-User': user_crop,
        'X-Access-Token': access_token,
        'Content-Type': 'application/json'
    }
    
    # 允许用户自定义查询
    # query = input("请输入查询内容 (默认: '给一个例子'): ") or "给一个例子"
    query = QUERY
    
    # 允许用户提供代码文件URL
    # code_file_url = input("请输入代码文件URL (可选): ")
    code_file_url = CODE_FILE_URL
    
    data = {
        'inputs': {
            "input":"你好"
        },
        # 'query': query,
        'mode': 'advanced-chat'
    }
    
    """ if code_file_url:
        data['input_files'] = {"codeFile": code_file_url} """
    
    print("正在发送API请求...")
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    # 打印状态码
    print(f"状态码: {response.status_code}")
    
    if response.status_code != 200:
        print(f"API请求失败: {response.text}")
        sys.exit(1)
    
    return response.text

def save_response_to_file(response_content):
    """保存API响应到临时文件"""
    temp_file = "api_response_temp.txt"
    
    # 确保响应内容包含文件定义标记
    if "===FILE:" not in response_content:
        print("警告: API响应中没有找到文件定义标记(===FILE:)。")
        print("API返回的内容可能不是预期的文件定义格式。")
        print("以下是API返回的内容(前500字符):")
        print(response_content[:500] + "..." if len(response_content) > 500 else response_content)
        
        # 尝试提取可能的代码块
        process_response = input("是否尝试从响应中提取代码块并创建文件? (y/n): ")
        if process_response.lower() != 'y':
            print("操作已取消。")
            sys.exit(0)
        
        # 这里可以添加代码来解析常见的AI响应格式中的代码块
        # 简单示例: 尝试将markdown代码块转换为文件定义格式
        import re
        code_blocks = re.findall(r'```(\w+)\n(.*?)\n```', response_content, re.DOTALL)
        if code_blocks:
            print(f"发现 {len(code_blocks)} 个代码块。将它们转换为文件...")
            converted_content = ""
            for i, (lang, code) in enumerate(code_blocks):
                filename = f"code_block_{i+1}.{lang}" if lang != "" else f"code_block_{i+1}.txt"
                converted_content += f"===FILE:{filename}===\n{code.strip()}\n===ENDFILE===\n\n"
            response_content = converted_content
        else:
            print("未能找到代码块。将创建单个文本文件...")
            response_content = f"===FILE:api_response.txt===\n{response_content}\n===ENDFILE===\n"
    
    # 将处理后的内容保存到临时文件
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(response_content)
    
    return temp_file

def main():
    """主函数"""
    try:
        # 调用API获取响应
        response_content = call_api()
        
        # 保存响应内容到临时文件
        temp_file = save_response_to_file(response_content)
        
        # 调用codeCli.py处理临时文件
        print(f"\n正在调用codeCli.py生成文件系统...")
        result = subprocess.run([sys.executable, code_cli_path, temp_file], 
                               capture_output=True, text=True)
        
        # 显示codeCli.py的输出
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("错误:", result.stderr)
        
        # 清理临时文件
        try:
            os.remove(temp_file)
            print(f"临时文件 {temp_file} 已删除")
        except:
            print(f"无法删除临时文件 {temp_file}")
        
        print("\n处理完成! 请查看 'output' 目录获取生成的文件。")
        
    except Exception as e:
        print(f"发生错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()