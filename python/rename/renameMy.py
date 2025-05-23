from rename import rename_files
from pathlib import Path

# 获取当前文件所在目录
current_dir = Path(__file__).parent

# 构建相对路径（更加简洁和直观）
""" file_path = current_dir / "mappingFiles" / "mine.json"
rename_files("D:/a部门合作文件/g136-灵兽大冒险/小程序/transform/我的页面", file_path)

file_path = current_dir / "mappingFiles" / "strategy.json"
rename_files("D:/a部门合作文件/g136-灵兽大冒险/小程序/transform/攻略页面", file_path) """

""" file_path = current_dir / "mappingFiles" / "home.json"
rename_files(r"G:\code\g136-miniprogram-uni\public\static\images\apps\appointment\home", file_path)  """

file_path = current_dir / "mappingFiles" / "invite.json"
rename_files(r"D:\a部门合作文件\g136-灵兽大冒险\小程序\人拉人活动\invite", file_path) 