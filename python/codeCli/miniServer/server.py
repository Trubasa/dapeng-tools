from flask import Flask, request, Response
import os
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def handle_get():
    """处理GET请求，返回参数中的text或默认消息"""
    # 获取URL参数中的text，如果没有则返回"hello world"
    text = request.args.get("text", "hello world")
    return Response(text, mimetype="text/plain")

@app.route("/", methods=["POST"])
def handle_post():
    """处理POST请求，保存内容到Markdown文件"""
    # 获取POST请求的内容
    content = request.get_data(as_text=True)
    
    # 创建markdown目录（如果不存在）
    md_dir = os.path.join(os.path.dirname(__file__), "markdown")
    if not os.path.exists(md_dir):
        os.makedirs(md_dir)
    
    # 创建包含时间戳的文件名
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"post_content_{timestamp}.md"
    file_path = os.path.join(md_dir, file_name)
    
    # 将内容写入Markdown文件
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# POST请求内容 - {timestamp}\n\n")
        f.write(content)
    
    # 返回成功消息
    return Response(
        f"内容已保存到 {file_name}",
        mimetype="text/plain"
    )

@app.route("/status", methods=["GET"])
def status():
    """返回服务器状态信息"""
    return {
        "status": "running",
        "time": datetime.datetime.now().isoformat(),
        "usage": {
            "GET /": "接收text参数或返回hello world",
            "POST /": "将请求内容保存为Markdown文件",
            "GET /status": "获取服务器状态"
        }
    }

if __name__ == "__main__":
    print("微信服务器已启动，访问 http://127.0.0.1:5000")
    print("* GET /: 返回text参数或'hello world'")
    print("* POST /: 将请求内容保存为Markdown文件")
    print("* GET /status: 获取服务器状态")
    app.run(debug=True)