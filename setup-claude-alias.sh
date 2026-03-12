#!/bin/bash
# 在 Trae 终端中设置 claude 别名的脚本

echo "=== 在 Trae 终端中设置 claude 别名 ==="
echo ""

# 方法1：直接设置别名（推荐）
echo "方法1：直接在 Trae 终端中输入以下命令"
echo "-----------------------------------"
echo "alias claude='open /Applications/Trae\ CN.app'"
echo ""
echo "然后就可以使用 claude 命令了："
echo "claude"
echo ""

# 方法2：创建启动脚本
echo "方法2：创建启动脚本"
echo "-----------------------------------"
echo "cat > ~/claude-launch.sh << 'EOF'"
echo "#!/bin/bash"
echo "open /Applications/Trae\ CN.app"
echo "EOF"
echo ""
echo "chmod +x ~/claude-launch.sh"
echo ""
echo "然后可以使用："
echo "~/claude-launch.sh"
echo ""

# 方法3：使用完整路径
echo "方法3：使用完整路径（最简单）"
echo "-----------------------------------"
echo "open /Applications/Trae\ CN.app"
echo ""

echo "=== 完成 ==="
echo ""
echo "推荐使用方法1，因为它最简单直接"
echo "在新的 Trae 终端窗口中，只需要输入一次 alias 命令即可"