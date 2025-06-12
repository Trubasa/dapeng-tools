
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def dir_to_params(directory: str) -> dict:
    """
    扫描指定目录（非递归），并将该目录下的文件内容转换为一个字典。
    字典的键是文件名（不包含后缀），值是文件的文本内容。

    :param directory: 要扫描的目标目录路径。
    :return: 一个字典，格式为 { "filename_without_ext": "content...", ... }。
    """
    # 检查提供的路径是否是一个有效的目录
    if not os.path.isdir(directory):
        print(f"错误: 提供的路径不是一个有效的目录: {directory}", file=sys.stderr)
        return {}

    params_dict = {}
    
    # 遍历目录中的所有条目
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        
        # 确保当前条目是一个文件，而不是子目录
        if os.path.isfile(full_path):
            # 分离文件名和后缀，使用不带后缀的文件名作为key
            key_name, _ = os.path.splitext(filename)
            
            try:
                # 尝试使用 UTF-8 编码读取文件
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                params_dict[key_name] = content
            except UnicodeDecodeError:
                # 如果UTF-8解码失败，尝试使用latin-1，并记录一个警告
                try:
                    with open(full_path, 'r', encoding='latin-1') as f:
                        content = f.read()
                    params_dict[key_name] = content
                    print(f"警告: 文件 '{filename}' 使用 latin-1 编码读取。", file=sys.stderr)
                except Exception as e:
                    print(f"错误: 无法读取文件 '{filename}': {e}", file=sys.stderr)
            except Exception as e:
                print(f"错误: 处理文件 '{filename}' 时发生未知错误: {e}", file=sys.stderr)
            
    return params_dict

if __name__ == '__main__':
    # 为该模块添加一个简单的命令行测试接口
    import json
    
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
        print(f"--- 正在扫描目录: {target_dir} ---")
        result_dict = dir_to_params(target_dir)
        
        if result_dict:
            print(f"\n--- 成功转换 {len(result_dict)} 个文件 ---")
            # 为了可读性，只打印文件名（不含后缀）
            print("文件键名列表:")
            for key in result_dict.keys():
                print(f"  - {key}")
            
            # 可以选择将结果保存到文件以供检查
            output_filename = "dir_to_params_output.json"
            with open(output_filename, 'w', encoding='utf-8') as f:
                json.dump(result_dict, f, ensure_ascii=False, indent=2)
            print(f"\n详细内容已保存到: {output_filename}")
        else:
            print("--- 未找到或转换任何文件 ---")
    else:
        print("这是一个将目录内容转换为字典的模块。")
        print("用法: python genCore/dirToParams.py <要扫描的目录路径>")
        sys.exit(1)
