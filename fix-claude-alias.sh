#!/bin/bash
# 修复 .zshrc 文件中的 claude 别名冲突

echo "=== 修复 .zshrc 文件中的 claude 别名冲突 ==="

# 备份当前的 .zshrc 文件
echo "1. 备份当前的 .zshrc 文件："
cp ~/.zshrc ~/.zshrc.backup.$(date +%Y%m%d_%H%M%S) 2>/dev/null && echo "   ✅ 备份完成" || echo "   ⚠️  备份失败"

# 创建新的 .zshrc 文件
echo "2. 创建新的 .zshrc 文件："
cat > ~/.zshrc << 'EOF'
# Claude Code CLI (installed via Homebrew)
# Use 'claude' command for Claude Code CLI
# Use 'trae' command to open Trae CN app
alias trae='open /Applications/Trae\ CN.app'
EOF

echo "   ✅ 新的 .zshrc 文件已创建"

# 显示新的 .zshrc 内容
echo "3. 新的 .zshrc 内容："
cat ~/.zshrc

echo ""
echo "✅ 修复完成！"
echo ""
echo "现在您可以使用以下命令："
echo "   claude    - 使用 Claude Code CLI"
echo "   trae      - 打开 Trae CN 应用"
echo ""
echo "请重新加载 .zshrc 或打开新的终端窗口以使更改生效："