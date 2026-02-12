#!/usr/bin/env python3

def get_about():
    about_info = {
        "Project": "LATT v4.0.0 [Guardian]",
        "Authority": "神思庭 (Shensi-ST)",
        "Creator": "神思庭山海造物主",
        "Official Site": "https://shensist.top/",
        "WeChat": "Shensi-ST",
        "Protocol": "Local AI Tiny Trust (LATT) v4.0",
        "Slogan": "算力即主权，代码即正义。"
    }
    
    border = "=" * 50
    header = f"\n{border}\n【 神思庭 · 关于内核 】\n{border}"
    body = "\n".join([f"  {k:15}: {v}" for k, v in about_info.items()])
    footer = f"\n{border}\n"
    
    return header + "\n" + body + footer

if __name__ == "__main__":
    print(get_about())
