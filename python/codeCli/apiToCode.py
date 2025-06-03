#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import os
from testApi5 import get_api_response
from buildFiles import buildFiles
from step1ToStep2 import main as step1ToStep2
from c2m import generate_markdown

PROJECT_DIR = r"G:\code\g136-miniprogram-admin-web"
QUERY = """
# 问题描述
目前代码运行中有个报错，当页面处在  banner-management 后，如果切换其他路由，会有以下报错
请帮我修复该问题

## 报错内容
[Vue warn]: Unhandled error during execution of component update 
  at <RouterView> 
  at <Layout onVnodeUnmounted=fn<onVnodeUnmounted> ref=Ref< Proxy(Object) {__v_skip: true} > > 
  at <RouterView> 
  at <App>
warn$1 @ runtime-core.esm-bundler.js:51
logError @ runtime-core.esm-bundler.js:263
handleError @ runtime-core.esm-bundler.js:255
callWithErrorHandling @ runtime-core.esm-bundler.js:201
flushJobs @ runtime-core.esm-bundler.js:408
Promise.then
queueFlush @ runtime-core.esm-bundler.js:322
queuePostFlushCb @ runtime-core.esm-bundler.js:336
queueEffectWithSuspense @ runtime-core.esm-bundler.js:7350
baseWatchOptions.scheduler @ runtime-core.esm-bundler.js:6226
effect2.scheduler @ reactivity.esm-bundler.js:1842
trigger @ reactivity.esm-bundler.js:265
endBatch @ reactivity.esm-bundler.js:323
notify @ reactivity.esm-bundler.js:609
trigger @ reactivity.esm-bundler.js:583
set value @ reactivity.esm-bundler.js:1460
finalizeNavigation @ vue-router.mjs:3503
(anonymous) @ vue-router.mjs:3368
Promise.then
pushWithRedirect @ vue-router.mjs:3335
push @ vue-router.mjs:3260
navigate @ vue-router.mjs:2315
callWithErrorHandling @ runtime-core.esm-bundler.js:199
callWithAsyncErrorHandling @ runtime-core.esm-bundler.js:206
invoker @ runtime-dom.esm-bundler.js:729Understand this warning
18:11:56.789 runtime-core.esm-bundler.js:5937 Uncaught (in promise) TypeError: Cannot read properties of null (reading 'type')
    at unmountComponent (runtime-core.esm-bundler.js:5937:63)
    at unmount (runtime-core.esm-bundler.js:5844:7)
    at unmountChildren (runtime-core.esm-bundler.js:5984:7)
    at unmount (runtime-core.esm-bundler.js:5868:9)
    at unmountChildren (runtime-core.esm-bundler.js:5984:7)
    at unmount (runtime-core.esm-bundler.js:5868:9)
    at unmountChildren (runtime-core.esm-bundler.js:5984:7)
    at unmount (runtime-core.esm-bundler.js:5876:9)
    at unmountChildren (runtime-core.esm-bundler.js:5984:7)
    at unmount (runtime-core.esm-bundler.js:5868:9)

## 已知信息
* 定位到 BannerTable.vue 中，的 columns 的最后一项，如果h标签内渲染的不是Button，而是 div，则不会有这个报错
"""

QUERY = '修改 BannerTable 和 Table 组件的实现，BannerTable 使用插槽的方式渲染，Table 组件提供具名插槽'
INPUT_DIR = PROJECT_DIR
OUTPUT_DIR = PROJECT_DIR

def api_to_code(query=None, code_str=None):
    """
    从API获取响应并将结果转换为代码文件系统
    
    参数：
    query (str, optional): 发送给API的查询，默认为"给一个例子"
    code_str (str, optional): 要发送给API的代码字符串，默认为None
    """
    # 如果未提供查询，使用默认值
    if query is None:
        query = QUERY
    
    # 获取API响应
    
    print(f"开始BrainMaker API调用...")
    response = get_api_response(code_str, query)
    
    if response.status_code == 200:
        try:
            # 提取响应文本
            response_text = response.text
            response_json = json.loads(response_text)
            # 确保temp目录存在
            temp_dir = "temp"
            if not os.path.exists(temp_dir):
                os.makedirs(temp_dir)
                
            # 将响应文本保存到temp/step1文件中
            step1_file_path = os.path.join(temp_dir, "step1")
            with open(step1_file_path, 'w', encoding='utf-8') as f:
                f.write(response_json.get("output",""))
            print(f"API响应已保存到 {step1_file_path}")

            # 调用step1ToStep2函数
            step1ToStep2()
            print("step1ToStep2函数执行完成。")
            
            # 处理响应文本，创建文件系统
            buildFiles('./temp/step2', OUTPUT_DIR)
            print("文件系统创建成功！请在output目录中查看。")
        except Exception as e:
            print(f"处理API响应时出错: {str(e)}")
    else:
        print(f"API请求失败，状态码: {response.status_code}")
        print(f"响应内容: {response.text}")

if __name__ == "__main__":
    print("提取项目文件到step0.md")
    generate_markdown(INPUT_DIR, "./temp/step0.md")
    print("提取项目文件到step0.md完成")

    # 从命令行参数获取查询（如果有）
    query = sys.argv[1] if len(sys.argv) > 1 else None
    
    # 执行API调用并创建代码
    api_to_code(query)