import pandas as pd
import os
import sys
from openpyxl.utils.exceptions import InvalidFileException

def analyze_workload(excel_path):
    """
    分析Excel工时表，统计各产品的工时分布
    
    参数:
        excel_path (str): Excel文件路径
    
    返回:
        None: 直接打印结果
    """
    try:
        # 检查文件是否存在
        if not os.path.exists(excel_path):
            print(f"错误: 文件 '{excel_path}' 不存在")
            return
        
        # 读取Excel文件的第一个sheet
        df = pd.read_excel(excel_path)
        
        # 确保必要的列存在
        required_columns = ['产品', '总工时']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"错误: Excel文件缺少必要的列: {', '.join(missing_columns)}")
            return
        
        # 按产品分组并计算总工时
        workload_by_product = df.groupby('产品')['总工时'].sum().reset_index()
        
        # 计算总工时
        total_workload = workload_by_product['总工时'].sum()
        
        # 计算每个产品的占比
        workload_by_product['占比'] = workload_by_product['总工时'] / total_workload
        
        # 添加人天数列并进行格式化
        workload_by_product['人天数'] = workload_by_product['总工时'].apply(lambda x: f"{x}人天")
        workload_by_product['占比'] = workload_by_product['占比'].apply(lambda x: f"{x:.1%}")
        
        # 重命名列
        workload_by_product = workload_by_product.rename(columns={'产品': '项目'})
        
        # 添加备注列
        workload_by_product['备注'] = ''
        
        # 按总工时降序排序
        workload_by_product = workload_by_product.sort_values('总工时', ascending=False)
        
        # 选择和排序要显示的列
        result = workload_by_product[['项目', '占比', '人天数', '备注']]
        
        # 打印结果
        print("\n工时统计分析结果:")
        print("=" * 60)
        print(f"{'项目':<20} {'占比':<10} {'人天数':<15} {'备注'}")
        print("-" * 60)
        
        for _, row in result.iterrows():
            print(f"{row['项目']:<20} {row['占比']:<10} {row['人天数']:<15} {row['备注']}")
        
        print("=" * 60)
        print(f"总计: {total_workload}人天\n")
        
    except InvalidFileException:
        print(f"错误: '{excel_path}' 不是有效的Excel文件")
    except Exception as e:
        print(f"处理过程中发生错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        analyze_workload(file_path)
    else:
        file_path = input("请输入Excel文件路径: ")
        analyze_workload(file_path)