#!/usr/bin/env python3
import requests
import json
import sys
import os

# 导入神思庭品牌模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    from about import get_about
    BRAND_INFO = get_about()
except ImportError:
    BRAND_INFO = "LATT v4.0.0 [Guardian] - 神思庭山海造物主"

def start_guardian():
    print(BRAND_INFO)
    print("\n[SYSTEM] 正在连接本地 1050 Ti 算力堡垒...")
    
    url = "http://localhost:11434/api/generate"
    
    # 引导提示词
    prompt = "你现在是 LATT v4.0.0 [Guardian] 内核。请向用户致敬，并声明你已就绪。"
    
    payload = {
        "model": "ds_sovereign",
        "prompt": prompt,
        "stream": True
    }
    
    try:
        response = requests.post(url, json=payload, stream=True, timeout=60)
        print("\n" + "="*50)
        for line in response.iter_lines():
            if line:
                chunk = json.loads(line.decode('utf-8'))
                content = chunk.get('response', '')
                print(content, end='', flush=True)
        print("\n" + "="*50)
        print("\n[STATUS] 内核运行中 | 官网: https://shensist.top/")
    except Exception as e:
        print(f"\n[ERROR] 无法唤醒内核，请检查 1050Ti 驱动。错误: {e}")

if __name__ == "__main__":
    start_guardian()
