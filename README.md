# Seedance 2.0 Prompt Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.2.0-blue.svg)](https://github.com/HiShineAi/seedance2-prompt-assistant/releases)

一个专业的 Claude Code Skill，用于帮助用户将创意想法转化为专业级的 Seedance 2.0 视频提示词。

## 🎯 功能特点

- **多模态支持**：支持文本、图片、视频、音频等多种输入方式
- **智能需求确认**：交互式确认视频参数，确保生成准确
- **结构化输出**：按照 6 大模块生成标准化提示词
- **参考图片分析**：自动分析分镜图，确保内容准确性
- **镜头设计**：专业的分秒镜头设计，包含运镜和景别

## 📋 快速开始

### 安装方法

1. 克隆此仓库
```bash
git clone https://github.com/HiShineAi/seedance2-prompt-assistant.git
```

2. 将 skill 文件复制到 Claude Code skills 目录
```bash
cp -r seedance2-prompt-assistant ~/.claude/skills/
```

### 使用方法

1. 在 Claude Code 中调用 `/seedance2-prompt-assistant`
2. 提供您的创意想法或参考素材
3. 按照交互式提示确认视频参数
4. 获得专业的 Seedance 2.0 提示词

## 📁 文件结构

```
seedance2-prompt-assistant/
├── SKILL.md              # Skill 定义文件
├── system.md            # 系统提示词（主要功能）
├── CHANGELOG.md         # 版本更新记录
├── examples/            # 使用示例（可选）
└── README.md           # 项目说明
```

## 🎬 核心功能

### 1. 多模态输入支持
- **文本提示词**：自然语言描述画面和动作
- **参考图片**：精准还原画面构图、角色细节
- **参考视频**：支持镜头语言、复杂动作节奏复刻
- **音频**：用于配乐和节奏控制

### 2. 交互式需求确认
- 视频时长选择（1-3秒到10秒以上）
- 影片风格定制（黑白胶片、动漫国漫、赛博朋克等）
- 情绪基调匹配（热闹欢快、优雅唯美、悬疑神秘等）
- 参考素材确认（图片/视频/音频）
- 运镜方式推荐（手持晃动、稳定镜头、慢镜头等）

### 3. 专业提示词生成

每个提示词包含以下 6 个模块：

#### 角色
- 主要角色/人物的数量
- 外观特征、服装
- 表情状态

#### 场景
- 地理位置、建筑风格
- 空间布局、天气光线

#### 动作/剧情
- 按时间顺序描述事件
- 角色的行为动作
- 情节推进

#### 镜头设计（分秒描述）
- 按时间分段，每1-2秒详细描述
- 镜头的运动方式、景别变化
- 焦点变化

#### 摄影风格
- 画面质感、色彩/黑白调性
- 光影效果、颗粒感

#### 音乐建议
- 音乐风格、节奏快慢
- 情绪配乐、卡点需求

## 🚀 使用示例

### 基础使用
```
/seedance2-prompt-assistant

我想要一个关于孩子们在海边奔跑的短视频，有参考图片。
```

### 高级使用
```
/seedance2-prompt-assistant

我想要一个古装武侠场景，使用这个分镜图@参考图片，配合传统配乐@参考音频。
```

## 🔧 技术要求

- Claude Code CLI（最新版本）
- 支持图像分析功能
- 支持交互式选择功能

## 📝 版本历史

### v1.2.0 (2026-02-24)
- ✅ 添加交互式选择机制
- ✅ 添加选项定制化机制
- ✅ 扩展触发关键词支持
- ✅ 优化用户体验

### v1.1.0 (2026-02-22)
- ✅ 实现两阶段工作流程
- ✅ 规范化提示词输出格式
- ✅ 添加镜头设计分秒描述指南
- ✅ 添加参考图片强制分析机制

## 🤝 贡献指南

1. Fork 此仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 支持

如果您在使用过程中遇到问题，请：

1. 查看 [CHANGELOG.md](CHANGELOG.md) 了解最新更新
2. 在 Issues 中提出您的问题
3. 或者直接联系作者

## 🙏 致谢

- [Anthropic](https://www.anthropic.com/) - 提供 Claude Code 平台
- Seedance 2.0 团队 - 提供专业的视频生成模型

---

> **提示**：此 Skill 需要配合 Seedance 2.0 平台使用，生成的提示词可直接用于该平台生成专业视频。