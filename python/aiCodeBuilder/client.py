#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import importlib
import tkinter as tk
from tkinter import ttk, scrolledtext

class ModuleUI:
    def __init__(self, root):
        self.root = root
        self.root.title("模块化工具箱")
        self.root.geometry("800x600")
        
        # 创建分割窗口
        self.paned = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
        self.paned.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 左侧模块列表框架
        self.modules_frame = ttk.LabelFrame(self.paned, text="可用模块")
        self.paned.add(self.modules_frame, weight=1)
        
        # 右侧模块详情和执行区域
        self.details_frame = ttk.LabelFrame(self.paned, text="模块详情")
        self.paned.add(self.details_frame, weight=2)
        
        # 模块列表
        self.modules_list = tk.Listbox(self.modules_frame, selectmode=tk.SINGLE)
        self.modules_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.modules_list.bind('<<ListboxSelect>>', self.on_module_select)
        
        # 模块详情组件
        self.module_name = ttk.Label(self.details_frame, text="", font=("", 14, "bold"))
        self.module_name.pack(anchor=tk.W, padx=10, pady=(10, 0))
        
        self.module_desc = ttk.Label(self.details_frame, text="", wraplength=400)
        self.module_desc.pack(anchor=tk.W, padx=10, pady=(5, 10))
        
        # 添加版本和作者信息
        self.module_version = ttk.Label(self.details_frame, text="")
        self.module_version.pack(anchor=tk.W, padx=10)
        
        self.module_author = ttk.Label(self.details_frame, text="")
        self.module_author.pack(anchor=tk.W, padx=10, pady=(0, 10))
        
        # 执行按钮
        self.run_button = ttk.Button(self.details_frame, text="运行模块", command=self.run_selected_module)
        self.run_button.pack(anchor=tk.W, padx=10, pady=10)
        self.run_button["state"] = "disabled"
        
        # 输出区域
        ttk.Label(self.details_frame, text="执行结果:").pack(anchor=tk.W, padx=10, pady=(10, 0))
        self.output_text = scrolledtext.ScrolledText(self.details_frame, height=10, wrap=tk.WORD)
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 加载模块
        self.modules = {}
        self.load_modules()
        
    def load_modules(self):
        """扫描modules目录并加载所有模块"""
        # 修改为直接使用当前文件所在目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        modules_dir = os.path.join(current_dir, "modules")
        
        # 如果目录不存在，自动创建
        if not os.path.exists(modules_dir):
            os.makedirs(modules_dir)
            self.output_text.insert(tk.END, f"已创建新的模块目录: '{modules_dir}'\n")
            self.output_text.insert(tk.END, "请在该目录下添加模块后重启程序。\n")
            return
            
        # 添加modules目录到Python路径
        sys.path.insert(0, os.path.dirname(modules_dir))
        
        # 检查是否有模块存在
        module_count = 0
        for item in os.listdir(modules_dir):
            module_path = os.path.join(modules_dir, item)
            if os.path.isdir(module_path) and not item.startswith('_'):
                module_count += 1
                
        if module_count == 0:
            self.output_text.insert(tk.END, f"模块目录 '{modules_dir}' 存在，但没有找到任何模块。\n")
            self.output_text.insert(tk.END, "请创建至少一个模块，结构如下:\n")
            self.output_text.insert(tk.END, "modules/\n")
            self.output_text.insert(tk.END, "└── hello/\n")
            self.output_text.insert(tk.END, "    ├── __init__.py    # 包含模块元数据\n")
            self.output_text.insert(tk.END, "    └── hello.py       # 包含run()函数\n")
            return
        
        # 扫描模块
        for item in os.listdir(modules_dir):
            module_path = os.path.join(modules_dir, item)
            if os.path.isdir(module_path) and not item.startswith('_'):
                try:
                    # 尝试导入模块
                    module = importlib.import_module(f"modules.{item}")
                    
                    # 检查是否有必要的模块信息
                    if hasattr(module, 'MODULE_INFO') and hasattr(module, 'main'):
                        info = module.MODULE_INFO
                        self.modules[item] = {
                            "module": module,
                            "info": info
                        }
                        self.modules_list.insert(tk.END, info.get("name", item))
                        print(f"已加载模块: {item}")
                    else:
                        print(f"警告: 模块 {item} 缺少必要的信息或入口点")
                        self.output_text.insert(tk.END, f"警告: 模块 {item} 缺少MODULE_INFO或run()函数\n")
                except Exception as e:
                    print(f"加载模块 {item} 时出错: {e}")
                    self.output_text.insert(tk.END, f"加载模块 {item} 时出错: {e}\n")
        
    def on_module_select(self, event):
        """处理模块选择事件"""
        if not self.modules_list.curselection():
            return
            
        index = self.modules_list.curselection()[0]
        selected_module_name = self.modules_list.get(index)
        
        # 查找对应的模块对象
        module_data = None
        for module_id, data in self.modules.items():
            if data["info"].get("name") == selected_module_name:
                module_data = data
                break
        
        if module_data:
            # 更新模块信息显示
            info = module_data["info"]
            self.module_name.config(text=info.get("name", "未命名模块"))
            self.module_desc.config(text=info.get("description", "无描述"))
            self.module_version.config(text=f"版本: {info.get('version', 'N/A')}")
            self.module_author.config(text=f"作者: {info.get('author', 'Unknown')}")
            self.run_button["state"] = "normal"
            
            # 清空上一次的输出
            self.output_text.delete(1.0, tk.END)
        else:
            self.run_button["state"] = "disabled"
    
    def run_selected_module(self):
        """执行选中的模块"""
        if not self.modules_list.curselection():
            return
            
        index = self.modules_list.curselection()[0]
        selected_module_name = self.modules_list.get(index)
        
        # 查找并执行模块
        for module_id, data in self.modules.items():
            if data["info"].get("name") == selected_module_name:
                try:
                    self.output_text.delete(1.0, tk.END)
                    self.output_text.insert(tk.END, f"正在执行 {selected_module_name}...\n\n")
                    self.root.update()
                    
                    # 执行模块
                    result = data["module"].main()
                    
                    # 显示结果
                    if result is not None:
                        self.output_text.insert(tk.END, f"{result}\n")
                    
                    self.output_text.insert(tk.END, "\n执行完成!")
                except Exception as e:
                    self.output_text.insert(tk.END, f"执行出错: {str(e)}\n")
                break

def main():
    root = tk.Tk()
    app = ModuleUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()