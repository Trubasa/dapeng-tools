import os
import sys
import shutil

def clean_directory(directory):
    """清空目录中的所有内容"""
    if os.path.exists(directory):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception as e:
                print(f"无法删除 {item_path}. 原因: {e}")

def create_file_system(structure):
    """Parse the structure string and create the file system."""
    # 文件标记的开始和结束模式
    file_start = "===FILE:"
    file_end = "===ENDFILE==="
    
    # 处理状态
    collecting_content = False
    current_file = None
    file_content = []
    
    # 创建输出目录并清空其内容
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    else:
        print(f"清空 {output_dir} 目录...")
        clean_directory(output_dir)
    
    # 按行处理输入
    lines = structure.split('\n')
    for line in lines:
        # 检查文件开始标记
        if line.startswith(file_start) and line.endswith("==="):
            # 提取原始文件路径
            original_path = line[len(file_start):-3].strip()
            
            # 修改为输出到output目录
            file_path = os.path.join(output_dir, original_path)
            
            # 确保目录存在
            directory = os.path.dirname(file_path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
            
            # 设置当前处理的文件
            current_file = file_path
            collecting_content = True
            file_content = []
            print(f"创建文件: {file_path}")
            continue
            
        # 检查文件结束标记
        if line == file_end and collecting_content:
            # 写入文件
            with open(current_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(file_content))
                
            # 重置状态
            collecting_content = False
            current_file = None
            file_content = []
            continue
            
        # 如果正在收集内容，则添加当前行
        if collecting_content:
            file_content.append(line)

def main():
    # 示例使用
    if len(sys.argv) > 1:
        # 从文件读取
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            structure = f.read()
    else:
        # 示例结构
        structure = """===FILE:requirements.txt===
Flask==2.3.3
Werkzeug==2.3.7
Jinja2==3.1.2
===ENDFILE===
===FILE:app.py===
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
===ENDFILE===
===FILE:templates/index.html===
<!DOCTYPE html>
<html>
<head>
    <title>Flask App</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
===ENDFILE===
"""

    create_file_system(structure)
    print("File system created successfully in 'output' directory!")

if __name__ == "__main__":
    main()