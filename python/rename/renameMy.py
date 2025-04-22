from rename import rename_files
from pathlib import Path

# 获取当前文件所在目录
current_dir = Path(__file__).parent

# 构建相对路径（更加简洁和直观）
file_path = current_dir / "mappingFiles" / "strategy.json"

rename_files("D:/a部门合作文件/g136-灵兽大冒险/小程序/test", file_path)