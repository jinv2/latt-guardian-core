#!/bin/bash
echo "--- LATT v4.0.0 Guardian 部署程序 ---"

# 1. 获取当前绝对路径
DIST_PATH=$(pwd)
MODEL_STORAGE="$DIST_PATH/models"

# 2. 注入环境变量（主权锁定）
export OLLAMA_MODELS="$MODEL_STORAGE"
echo "export OLLAMA_MODELS=\"$MODEL_STORAGE\"" >> ~/.bashrc

# 3. 检查并启动 Ollama 服务
if ! pgrep -x "ollama" > /dev/null
then
    echo "[INFO] 正在后台唤醒本地算力引擎..."
    nohup ollama serve > /dev/null 2>&1 &
    sleep 5
fi

# 4. 验证模型状态
echo "[CHECK] 正在验证 ds_sovereign 极限内核..."
ollama list | grep "ds_sovereign"

echo "[SUCCESS] LATT v4.0.0 部署完成。算力主权已移交客户。"
echo "请执行: python3 core/main.py 进行首次审计。"
