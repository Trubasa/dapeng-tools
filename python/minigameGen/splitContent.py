def extract_content_from_last_single_hash(file_path):
    """
    读取文件内容，精确截取最后一个单独的 # 符号及其后的所有内容
    
    参数:
        file_path (str): 文件路径
        
    返回:
        str: 截取的内容（如果找到单独的#），否则返回空字符串
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
                return content[position:]
            else:
                return ""  # 没有找到单独的 #
                
    except FileNotFoundError:
        return f"错误：文件不存在 - {file_path}"
    except Exception as e:
        return f"读取文件时出错: {str(e)}"


# 使用示例
if __name__ == "__main__":
    file_path = input("请输入文件路径: ")
    result = extract_content_from_last_single_hash(file_path)
    print("\n截取结果:")
    print(result)