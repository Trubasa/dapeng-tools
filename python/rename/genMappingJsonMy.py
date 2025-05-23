from genMappingJson import generate_mapping_json

# 带额外映射
extra_mapping = {
   
}
""" generate_mapping_json(
    directory="D:/a部门合作文件/g136-灵兽大冒险/小程序/transform/攻略页面", 
    output_path="./mappingFiles/strategy.json",
    extra_mapping=extra_mapping
)

generate_mapping_json(
    directory="D:/a部门合作文件/g136-灵兽大冒险/小程序/transform/我的页面", 
    output_path="./mappingFiles/mine.json",
    extra_mapping=extra_mapping
) """

""" generate_mapping_json(
    directory="G:/code/g136-miniprogram-uni/public/static/images/apps/appointment/home", 
    output_path="./mappingFiles/home.json",
    extra_mapping=extra_mapping
) """
generate_mapping_json(
    directory=r"D:\a部门合作文件\g136-灵兽大冒险\小程序\人拉人活动\invite", 
    output_path="./mappingFiles/invite.json",
    extra_mapping=extra_mapping
)