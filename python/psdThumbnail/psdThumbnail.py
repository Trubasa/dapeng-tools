import os
import argparse
from psd_tools import PSDImage

def create_thumbnails(source_dir):
    # os.walk() 遍历目录树
    for root, dirs, files in os.walk(source_dir):
        for filename in files:
            if filename.lower().endswith((".psb", ".psd")):
                file_path = os.path.join(root, filename)
                out_file_path = os.path.splitext(file_path)[0] + ".png"  # 更改文件扩展名为.png

                # 打开PSD文件并获取合成图像
                psd = PSDImage.open(file_path)
                image = psd.composite()

                # 保存缩略图，保持原始尺寸
                image.save(out_file_path, "PNG")

                print(f"Thumbnail created for {filename}: {out_file_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate thumbnails from PSD or PSB files.")
    parser.add_argument("source_directory", type=str, help="The directory to search for PSD/PSB files.")
    args = parser.parse_args()

    # 调用函数，为目录树中的每个PSD文件生成缩略图
    create_thumbnails(args.source_directory)

if __name__ == "__main__":
    main()