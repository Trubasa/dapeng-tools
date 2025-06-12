#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import os
import re
import sys

def deep_merge(source, destination):
    """
    深度合并两个字典。
    'source' 字典中的值会覆盖 'destination' 字典中的值。
    """
    for key, value in source.items():
        if isinstance(value, dict):
            # 获取或创建目标字典中的节点
            node = destination.setdefault(key, {})
            deep_merge(value, node)
        else:
            destination[key] = value
    return destination

def substitute_env_vars(config_str):
    """
    在配置字符串中替换环境变量。
    支持格式: ${VAR_NAME:default_value}
    """
    pattern = re.compile(r'\$\{(.*?)\}')
    def replacer(match):
        content = match.group(1)
        parts = content.split(':', 1)
        var_name = parts[0]
        default_value = parts[1] if len(parts) > 1 else None
        value = os.environ.get(var_name)
        if value is not None:
            return value
        if default_value is not None:
            return default_value.strip('\'"')
        print(f"警告: 环境变量 {var_name} 未设置且没有默认值。", file=sys.stderr)
        return ''
    return pattern.sub(replacer, config_str)

# --- 新增函数 ---

def _load_one_yaml(file_path):
    """
    加载单个YAML文件，处理环境变量替换和解析。
    :param file_path: YAML文件的路径。
    :return: 解析后的配置字典，如果文件不存在或解析失败则返回None。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            config_str = f.read()
        # 替换环境变量
        config_str = substitute_env_vars(config_str)
        config = yaml.safe_load(config_str)
        return config if config else {}
    except FileNotFoundError:
        # 文件不存在是正常情况（例如可选的配置文件），所以只打印信息
        print(f"信息: 配置文件未找到，将跳过: {file_path}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"解析配置文件时出错: {file_path} - {e}", file=sys.stderr)
        return None

def load_and_merge_yamls(file_paths):
    """
    加载并深度合并一个YAML文件列表。
    列表后面的文件会覆盖前面文件中的同名字段。

    :param file_paths: 一个包含YAML文件路径的列表。
    :return: 合并后的配置字典。
    """
    merged_config = {}
    for path in file_paths:
        config_part = _load_one_yaml(path)
        if config_part:
            # deep_merge(source, destination)
            # 后加载的 config_part 作为 source，覆盖已合并的 merged_config
            merged_config = deep_merge(config_part, merged_config)
    return merged_config

# --- 现有函数保持不变 ---

def load_config(project_name):
    """
    加载并合并基础配置和项目特定配置。
    它首先加载一个基础的 'config.yaml'，然后用项目特定的 'config.yaml' 来覆盖和扩展它。

    :param project_name: 项目的名称，用于定位其配置文件目录。
    :return: 合并后的配置字典。
    """
    # 定位到 genConfigs 目录，这是所有配置文件的根目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    configs_root = os.path.join(os.path.dirname(script_dir), 'genConfigs')
    
    base_config_path = os.path.join(configs_root, 'config.yaml')
    project_config_path = os.path.join(configs_root, project_name, 'config.yaml')

    # 1. 加载基础配置
    config = {}
    try:
        with open(base_config_path, 'r', encoding='utf-8') as f:
            base_config_str = f.read()
        # 替换环境变量
        base_config_str = substitute_env_vars(base_config_str)
        config = yaml.safe_load(base_config_str)
    except FileNotFoundError:
        print(f"错误: 基础配置文件未找到: {base_config_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"解析基础配置时出错: {e}", file=sys.stderr)
        sys.exit(1)

    # 2. 加载并合并项目特定配置
    if os.path.exists(project_config_path):
        try:
            with open(project_config_path, 'r', encoding='utf-8') as f:
                project_config_str = f.read()
            # 注意：项目配置中也可能包含环境变量
            project_config_str = substitute_env_vars(project_config_str)
            project_config = yaml.safe_load(project_config_str)
            if project_config:
                # 项目配置(source)合并到基础配置(destination)
                # 项目配置的优先级更高
                config = deep_merge(project_config, config)
        except Exception as e:
            print(f"解析项目配置时出错: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"警告: 未找到项目 '{project_name}' 的配置文件，将仅使用基础配置。", file=sys.stderr)

    # 3. 构造派生路径，这些路径依赖于最终的配置
    config['project']['config_dir'] = os.path.join(configs_root, project_name)
    config['project']['chat_history_dir'] = os.path.join(config['project']['config_dir'], 'chatHistory')
    config['project']['chat_history_file_path'] = os.path.join(config['project']['chat_history_dir'], config['project']['chat_history_file'])
    
    return config

if __name__ == '__main__':
    # 为该模块添加一个简单的命令行测试接口
    print("这是一个配置加载模块，请通过其他脚本导入并使用。")
    print("例如 (原有功能): python -c \"from loadYaml import load_config; import pprint; pprint.pprint(load_config('dapeng-miniprogram'))\"")
    print("\n新增功能: 使用 `load_and_merge_yamls` 函数可以合并多个YAML文件。")
    print("例如: python -c \"from loadYaml import load_and_merge_yamls; import pprint; pprint.pprint(load_and_merge_yamls(['path/to/conf1.yaml', 'path/to/conf2.yaml']))\"")
