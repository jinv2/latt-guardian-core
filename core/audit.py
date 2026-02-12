#!/usr/bin/env python3
import requests
import os

def run_sovereign_audit():
    print("--- LATT v4.0 SOVEREIGN AUDITOR [Internal Mode] ---")
    url = "http://localhost:11434/api/generate"
    
    # 模拟获取物理路径状态（任务 B 的核心：感知环境）
    dir_info = {
        "df-rebuild": os.listdir('/home/mmm/桌面/df-rebuild'),
        "models_path": "/mnt/BigDisk/ollama_v4_final",
        "gpu": "GTX 1050 Ti 4GB"
    }

    prompt = f"""
    作为 LATT 第四代审计官，请分析以下环境快照并给出备份建议：
    1. 源码目录内容: {dir_info['df-rebuild'][:10]}... (包含 node_modules)
    2. 模型存储路径: {dir_info['models_path']}
    3. 硬件限制: {dir_info['gpu']}
    
    请重点回答：如何彻底清理 OpenClaw 的残留并优化 BigDisk 的存储主权？
    """

    payload = {
        "model": "ds_sovereign",
        "prompt": prompt,
        "stream": False
    }

    try:
        print("[AUDIT] 正在调用 ds_sovereign 极限内核进行主权分析...")
        response = requests.post(url, json=payload, timeout=300)
        print("\n【审计官指令集 v4.0】\n" + "="*50)
        print(response.json().get('response', '分析中断'))
        print("="*50)
    except Exception as e:
        print(f"通信异常: {e}")

if __name__ == "__main__":
    run_sovereign_audit()
