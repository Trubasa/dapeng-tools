import re

def extract_content_from_last_single_hash(file_path):
    """
    读取文件内容，精确截取最后一个单独的 # 符号及其后的所有内容
    
    参数:
        file_path (str): 文件路径
        
    返回:
        dict: 包含两个键的字典：
              - content: 截取的内容（如果找到单独的#），否则为空字符串
              - imgDict: 内容中图片的字典，键为图片名称，值为URL
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # 从后向前查找最后一个单独的 # 符号
            position = -1
            for i in range(len(content)-1, -1, -1):
                if content[i] == '#':
                    # 检查是否是单独的 # (前后都不是 #)
                    prev_char = content[i-1] if i > 0 else None
                    next_char = content[i+1] if i < len(content)-1 else None
                    
                    if prev_char != '#' and next_char != '#':
                        position = i
                        break
            
            if position != -1:
                extracted_content = content[position:]
                # 提取图片信息
                img_dict = extract_images(extracted_content)
                return {
                    "content": extracted_content,
                    "imgDict": img_dict
                }
            else:
                return {
                    "content": "",  # 没有找到单独的 #
                    "imgDict": {}
                }
                
    except FileNotFoundError:
        return {
            "content": f"错误：文件不存在 - {file_path}",
            "imgDict": {}
        }
    except Exception as e:
        return {
            "content": f"读取文件时出错: {str(e)}",
            "imgDict": {}
        }

def extract_images(text):
    """
    从文本中提取Markdown格式的图片引用
    
    参数:
        text (str): 包含Markdown图片引用的文本
        
    返回:
        dict: 图片字典，键为图片名称，值为URL
    """
    img_dict = {}
    # 正则表达式匹配 ![xxx](urlxxx) 格式的图片引用
    pattern = r'!\[(.*?)\]\((.*?)\)'
    matches = re.findall(pattern, text)
    
    for alt_text, url in matches:
        img_dict[alt_text] = url
    
    return img_dict


# 使用示例
if __name__ == "__main__":
    file_path = input("请输入文件路径: ")
    result = extract_content_from_last_single_hash(file_path)
    print("\n截取结果:")
    print(f"内容长度: {len(result['content'])} 字符")
    print(f"找到 {len(result['imgDict'])} 张图片:")
    for name, url in result['imgDict'].items():
        print(f"- {name}: {url}")