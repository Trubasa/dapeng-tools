
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import argparse

def extract_tagged_content(content: str, tag_name: str = 'ai-api-output') -> str | None:
    """
    从输入字符串中提取指定XML/HTML标签及其完整内容。
    例如，使用默认tag_name 'ai-api-output'，它会寻找 <ai-api-output>...</ai-api-output>。

    :param content: 要搜索的源字符串。
    :param tag_name: 要查找的标签名，默认为 'ai-api-output'。
    :return: 找到的第一个匹配的完整标签内容（包括标签本身），如果未找到则返回 None。
    """
    # re.DOTALL 使 '.' 能匹配包括换行符在内的任意字符，实现跨行匹配
    pattern = f'<{tag_name}>(.*?)</{tag_name}>'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        # match.group(0) 返回整个匹配的字符串，包含外部标签
        return match.group(0)
    else:
        return None

def main():
    """
    主函数，作为命令行工具，用于从一个文件中提取指定标签内容并保存到另一个文件。
    主要用于解析API响应，并提取出可供后续处理的XML内容块。
    """
    parser = argparse.ArgumentParser(
        description="从输入文件中提取指定XML标签对之间的内容，并保存到输出文件。"
    )
    parser.add_argument(
        'input_file', 
        nargs='?', 
        default='temp/step1', 
        help="包含API原始响应的输入文件路径 (默认: temp/step1)"
    )
    parser.add_argument(
        'output_file', 
        nargs='?', 
        default='temp/step2', 
        help="保存提取后内容的输出文件路径 (默认: temp/step2)"
    )
    parser.add_argument(
        '--tag', 
        dest='tag_name', 
        default='ai-api-output', 
        help="要提取的XML标签名 (默认: ai-api-output)"
    )
    args = parser.parse_args()

    try:
        # 读取输入文件内容
        with open(args.input_file, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        # 使用核心函数提取内容
        tagged_content = extract_tagged_content(content, args.tag_name)
        
        if tagged_content:
            # 确保输出目录存在
            output_dir = os.path.dirname(args.output_file)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # 写入输出文件
            with open(args.output_file, 'w', encoding='utf-8') as f:
                f.write(tagged_content)
            
            print(f"成功提取内容并保存到 {args.output_file}")
            sys.exit(0) # 成功退出
        else:
            print(f"错误: 在文件 {args.input_file} 中未找到 <{args.tag_name}>...</{args.tag_name}> 标签", file=sys.stderr)
            sys.exit(1) # 失败退出
    
    except FileNotFoundError:
        print(f"错误: 输入文件未找到 - {args.input_file}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"处理过程中出错: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
