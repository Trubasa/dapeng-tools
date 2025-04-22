from genMappingJson import generate_mapping_json

# 带额外映射
extra_mapping = {
    "项目": "project",
    "文档": "documentation"
}
generate_mapping_json(
    directory="D:/a部门合作文件/g136-灵兽大冒险/小程序/test/strategy", 
    output_path="./mappingFiles/mapping.json",
    extra_mapping=extra_mapping
)