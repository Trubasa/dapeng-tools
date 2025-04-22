#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
翻译测试工具 - 测试 googletrans 库的翻译功能
用法: python testTranslate.py [文本] [源语言] [目标语言]
"""

import sys
import time
import argparse
import asyncio
from googletrans import Translator, LANGUAGES

async def translate_text_async(text, src='zh-cn', dest='en', show_details=False):
    """
    使用 googletrans 库异步翻译文本
    
    Args:
        text: 要翻译的文本
        src: 源语言 (默认: 'zh-cn')
        dest: 目标语言 (默认: 'en')
        show_details: 是否显示详细翻译信息
        
    Returns:
        str: 翻译结果
    """
    try:
        print(f"正在翻译: '{text}' (从 {src} 到 {dest})")
        translator = Translator()
        start_time = time.time()
        
        # 异步调用翻译
        result = await translator.translate(text, src=src, dest=dest)
        
        elapsed_time = time.time() - start_time
        print(f"翻译完成! 耗时: {elapsed_time:.2f}秒")
        
        if show_details:
            print("\n翻译详情:")
            print(f"源语言检测: {result.src}")
            print(f"翻译结果置信度: {result.confidence}")
            print(f"发音: {result.pronunciation}" if hasattr(result, 'pronunciation') else "无发音信息")
        
        return result.text
    
    except Exception as e:
        print(f"翻译失败: {e}")
        return None

# 非异步版本，供同步上下文使用
def translate_text(text, src='zh-cn', dest='en', show_details=False):
    """同步版本的翻译函数"""
    try:
        print(f"正在翻译: '{text}' (从 {src} 到 {dest})")
        translator = Translator()
        start_time = time.time()
        
        # 直接调用同步方法 (googletrans 原版可能没有这个方法，所以尝试两种方式)
        try:
            result = translator.translate(text, src=src, dest=dest, _fast=False)  # 尝试非异步调用
        except:
            # 如果上面失败，则通过运行事件循环来执行异步调用
            loop = asyncio.new_event_loop()
            result = loop.run_until_complete(translator.translate(text, src=src, dest=dest))
            loop.close()
        
        elapsed_time = time.time() - start_time
        print(f"翻译完成! 耗时: {elapsed_time:.2f}秒")
        
        if show_details:
            print("\n翻译详情:")
            print(f"源语言检测: {result.src}")
            print(f"翻译结果置信度: {result.confidence}")
            print(f"发音: {result.pronunciation}" if hasattr(result, 'pronunciation') else "无发音信息")
        
        return result.text
    
    except Exception as e:
        print(f"翻译失败: {e}")
        return None

def list_supported_languages():
    """列出所有支持的语言"""
    print("\n支持的语言:")
    for code, language in sorted(LANGUAGES.items()):
        print(f"  {code}: {language}")

async def batch_test_async():
    """异步测试一批中文词语的翻译效果"""
    test_words = [
        "攻略页面",
        "视频图",
        "搜索页",
        "头像边框",
        "播放按钮",
        "暂停按钮",
        "葫芦",
        "返回按钮",
        "进度条",
        "黑色遮罩",
        "文案底"
    ]
    
    print("开始批量翻译测试...\n")
    results = {}
    
    for word in test_words:
        print("-" * 50)
        result = await translate_text_async(word, 'zh-cn', 'en')
        if result:
            results[word] = result
            print(f"'{word}' -> '{result}'")
        await asyncio.sleep(1)  # 避免请求过于频繁
    
    print("\n批量翻译结果汇总:")
    print("-" * 50)
    for word, translation in results.items():
        print(f"'{word}' -> '{translation}'")
    
    return results

# 同步版本的批量测试
def batch_test():
    """同步测试一批中文词语的翻译效果"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        return loop.run_until_complete(batch_test_async())
    finally:
        loop.close()

async def main_async():
    """异步主函数"""
    parser = argparse.ArgumentParser(description='测试 googletrans 库的翻译功能')
    parser.add_argument('text', nargs='?', default='你好，世界!', 
                        help='要翻译的文本 (默认: "你好，世界!")')
    parser.add_argument('-s', '--source', default='zh-cn', 
                        help='源语言代码 (默认: zh-cn)')
    parser.add_argument('-d', '--dest', default='en', 
                        help='目标语言代码 (默认: en)')
    parser.add_argument('--details', action='store_true', 
                        help='显示详细翻译信息')
    parser.add_argument('--languages', action='store_true', 
                        help='列出所有支持的语言')
    parser.add_argument('-b', '--batch', action='store_true',
                        help='批量测试多个中文词语')
    
    args = parser.parse_args()
    
    if args.languages:
        list_supported_languages()
        return
    
    if args.batch:
        await batch_test_async()
        return
    
    result = await translate_text_async(args.text, args.source, args.dest, args.details)
    if result:
        print(f"\n翻译结果: {result}")

def main():
    """同步入口点"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main_async())
    finally:
        loop.close()

# 用于直接测试的简化函数
def quick_test(text="你好，世界"):
    """简单翻译测试函数，用于快速检查翻译功能"""
    try:
        # 创建一个新的事件循环
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        # 实例化翻译器
        translator = Translator()
        
        # 直接用新版API异步调用
        async def run_test():
            result = await translator.translate(text, src='zh-cn', dest='en')
            return result.text
            
        # 执行异步函数
        result = loop.run_until_complete(run_test())
        loop.close()
        
        print(f"'{text}' -> '{result}'")
        return result
    except Exception as e:
        print(f"测试翻译失败: {e}")
        return None

if __name__ == "__main__":
    print("Google 翻译测试工具")
    print("=" * 50)
    
    try:
        # 检查是否安装了googletrans库的正确版本
        translator_version = sys.modules['googletrans'].__version__
        print(f"已加载 googletrans 版本: {translator_version}")
        if translator_version != '4.0.0-rc1':
            print("警告: 推荐使用的版本是 4.0.0-rc1。")
            print("您可以使用以下命令安装推荐版本:")
            print("pip install googletrans==4.0.0-rc1")
    except (KeyError, AttributeError):
        print("无法确定 googletrans 版本")
    
    # 执行常规测试，还是提供简单的快速测试
    if len(sys.argv) > 1:
        main()  # 带参数运行完整程序
    else:
        # 执行快速测试
        print("\n执行快速测试...")
        quick_test()