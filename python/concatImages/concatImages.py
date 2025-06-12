#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from PIL import Image

def concat_images_horizontally(image_dir, output_path, spacing=2, bg_color=(255, 255, 255)):
    """
    将目录中的图片横向拼接成一张长图，图片之间添加指定间隔
    
    参数:
        image_dir (str): 图片目录路径
        output_path (str): 输出图片路径
        spacing (int): 图片间隔像素数（默认2px）
        bg_color (tuple): 背景颜色RGB值（默认白色）
    """
    try:
        # 获取目录中所有图片文件
        image_files = []
        valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp']
        
        for f in os.listdir(image_dir):
            if os.path.splitext(f)[1].lower() in valid_extensions:
                image_files.append(os.path.join(image_dir, f))
        
        if not image_files:
            print(f"错误：目录 '{image_dir}' 中没有找到图片文件")
            return False
        
        # 按文件名排序
        image_files.sort()
        
        # 打开所有图片并计算总尺寸
        images = []
        max_height = 0
        total_width = 0
        
        for img_path in image_files:
            img = Image.open(img_path)
            images.append(img)
            total_width += img.width
            if img.height > max_height:
                max_height = img.height
        
        # 计算总宽度（包括间隔）
        total_width += spacing * (len(images) - 1)
        
        # 创建新图片
        new_img = Image.new('RGB', (total_width, max_height), color=bg_color)
        
        # 拼接图片
        x_offset = 0
        for i, img in enumerate(images):
            new_img.paste(img, (x_offset, 0))
            x_offset += img.width + spacing
        
        # 保存结果
        new_img.save(output_path)
        print(f"成功创建拼接图片: {output_path}")
        print(f"原始图片数量: {len(images)}")
        print(f"最终尺寸: {total_width}x{max_height} 像素")
        return True
        
    except Exception as e:
        print(f"处理过程中出错: {str(e)}")
        return False

if __name__ == "__main__":
    # 命令行参数处理
    if len(sys.argv) < 2:
        print("使用方法: python concat_images.py <图片目录> [输出文件路径]")
        print("示例: python concat_images.py ./images output.jpg")
        sys.exit(1)
    
    image_dir = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "output.jpg"
    
    # 检查目录是否存在
    if not os.path.isdir(image_dir):
        print(f"错误: 目录 '{image_dir}' 不存在")
        sys.exit(1)
    
    # 执行拼接
    success = concat_images_horizontally(image_dir, output_path)
    sys.exit(0 if success else 1)