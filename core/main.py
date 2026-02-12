#!/usr/bin/env python3
import requests
import json

def publish_v4_stream():
    print("--- LATT v4.0.0 [Guardian] STREAMING LAUNCH ---")
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": "ds_sovereign",
        "prompt": "你现在是 LATT v4.0.0 (Guardian) 智能体内核。请发布版本说明：1. 脱离 OpenClaw 实现 100% 本地化。2. 在 1050 Ti 建立 ds_sovereign 内核。3. 清理 node_modules 确立 Tiny Trust 协议。用严谨、有主权感的语气。",
        "stream": True  # 开启流式传输，解决超时问题
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
        print("\n[V4_CORE] 状态：主权确立 | 模式：流式推理")
    except Exception as e:
        print(f"\n[ERROR] 推理中断: {e}")

if __name__ == "__main__":
    publish_v4_stream()
