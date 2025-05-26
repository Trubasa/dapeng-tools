#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import tkinter as tk
from tkinter import filedialog

def select_file(title="选择文件", filetypes=None, initialdir=None):
    """
    打开文件选择对话框，让用户选择一个文件
    
    参数:
        title (str): 对话框标题
        filetypes (list): 文件类型列表，例如 [("文本文件", "*.txt"), ("所有文件", "*.*")]
        initialdir (str): 初始目录路径，默认为None将使用当前目录
        
    返回:
        str: 选择的文件路径，如果用户取消则返回空字符串
    """
    # 创建临时的根窗口并隐藏
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    
    # 默认文件类型如果没有指定
    if filetypes is None:
        filetypes = [("所有文件", "*.*")]
    
    # 设置初始目录
    if initialdir is None:
        initialdir = os.getcwd()
    
    # 打开文件选择对话框
    file_path = filedialog.askopenfilename(
        title=title,
        filetypes=filetypes,
        initialdir=initialdir
    )
    
    # 销毁临时根窗口
    root.destroy()
    
    return file_path

def select_directory(title="选择目录", initialdir=None):
    """
    打开目录选择对话框，让用户选择一个目录
    
    参数:
        title (str): 对话框标题
        initialdir (str): 初始目录路径，默认为None将使用当前目录
        
    返回:
        str: 选择的目录路径，如果用户取消则返回空字符串
    """
    # 创建临时的根窗口并隐藏
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    
    # 设置初始目录
    if initialdir is None:
        initialdir = os.getcwd()
    
    # 打开目录选择对话框
    dir_path = filedialog.askdirectory(
        title=title,
        initialdir=initialdir
    )
    
    # 销毁临时根窗口
    root.destroy()
    
    return dir_path

def save_file(title="保存文件", defaultextension=".txt", filetypes=None, initialdir=None, initialfile=""):
    """
    打开文件保存对话框，让用户选择保存文件的位置
    
    参数:
        title (str): 对话框标题
        defaultextension (str): 默认文件扩展名
        filetypes (list): 文件类型列表，例如 [("文本文件", "*.txt"), ("所有文件", "*.*")]
        initialdir (str): 初始目录路径，默认为None将使用当前目录
        initialfile (str): 初始文件名
        
    返回:
        str: 选择的保存文件路径，如果用户取消则返回空字符串
    """
    # 创建临时的根窗口并隐藏
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    
    # 默认文件类型如果没有指定
    if filetypes is None:
        filetypes = [("所有文件", "*.*")]
    
    # 设置初始目录
    if initialdir is None:
        initialdir = os.getcwd()
    
    # 打开文件保存对话框
    file_path = filedialog.asksaveasfilename(
        title=title,
        defaultextension=defaultextension,
        filetypes=filetypes,
        initialdir=initialdir,
        initialfile=initialfile
    )
    
    # 销毁临时根窗口
    root.destroy()
    
    return file_path

if __name__ == "__main__":
    # 测试函数
    print("选择文件测试:")
    file_path = select_file("请选择一个文件", [("文本文件", "*.txt"), ("Python文件", "*.py"), ("所有文件", "*.*")])
    print(f"选择的文件: {file_path}")
    
    print("\n选择目录测试:")
    dir_path = select_directory("请选择一个目录")
    print(f"选择的目录: {dir_path}")
    
    print("\n保存文件测试:")
    save_path = save_file("请选择保存位置", ".txt", [("文本文件", "*.txt"), ("所有文件", "*.*")])
    print(f"保存路径: {save_path}")