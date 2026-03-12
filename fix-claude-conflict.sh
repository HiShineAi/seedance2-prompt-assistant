#!/bin/bash
# 修复 claude 命令冲突问题

echo "=== 修复 claude 命令冲突问题 ==="

# 检查是否有权限删除旧的 claude 命令
echo "1. 检查旧的 claude 命令："
ls -la /usr/local/bin/claude 2>/dev/null && echo "   找到旧的 claude 命令" || echo "   未找到旧的 claude 命令"

# 尝试删除旧的 claude 命令
echo "2. 尝试删除旧的 claude 命令："
sudo rm /usr/local/bin/claude 2>/dev/null && echo "   ✅ 成功删除旧的 claude 命令" || echo "   ⚠️  需要手动删除"

# 如果需要手动删除，提供说明
if [ -f /usr/local/bin/claude ]; then
    echo ""
    echo "⚠️  需要手动删除旧的 claude 命令"
    echo ""
    echo "请在系统终端中运行以下命令："
    echo "   sudo rm /usr/local/bin/claude"
    echo ""
    echo "或者在 Trae 终端中运行："
    echo "   sudo rm /usr/local/bin/claude"
fi

# 检查删除后的结果
echo ""
echo "3. 检查删除后的结果："
which claude 2>/dev/null && echo "   ✅ claude 命令现在指向: $(which claude)" || echo "   ❌ claude 命令未找到"

# 测试 claude 命令
echo ""
echo "4. 测试 claude 命令："
claude --version 2>&1 | head -5