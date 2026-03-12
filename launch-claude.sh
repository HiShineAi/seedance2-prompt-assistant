#!/bin/bash
# 在 Trae 终端中启动 Claude/Trae CN 的脚本

echo "=== 在 Trae 终端中启动 Claude/Trae CN ==="
echo ""

# 检查应用是否存在
if [ ! -d "/Applications/Trae CN.app" ]; then
    echo "❌ 错误：找不到 Trae CN 应用"
    exit 1
fi

# 尝试启动应用
echo "正在启动 Trae CN 应用..."
open "/Applications/Trae CN.app"

# 等待应用启动
sleep 2

# 检查应用是否成功启动
if pgrep -fl "Trae CN" > /dev/null 2>&1; then
    echo "✅ 成功！Trae CN 应用正在运行"
    echo ""
    echo "您现在可以在 Trae 应用中使用 Claude 功能了"
else
    echo "⚠️  应用可能正在启动中，请稍等片刻"
    echo ""
    echo "如果应用没有启动，请尝试："
    echo "1. 手动在 Finder 中打开 Trae CN.app"
    echo "2. 检查应用是否有更新"
fi