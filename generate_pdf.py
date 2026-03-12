#!/usr/bin/env python3
"""
生成Claude介绍PDF文档
"""

from reportlab.lib.pagesizes import A4, letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# 创建PDF文档
doc = SimpleDocTemplate(
    "claude_introduction.pdf",
    pagesize=A4,
    rightMargin=72,
    leftMargin=72,
    topMargin=72,
    bottomMargin=18
)

# 获取样式
styles = getSampleStyleSheet()

# 自定义样式
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=28,
    textColor=colors.HexColor('#1a1a2e'),
    spaceAfter=30,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

subtitle_style = ParagraphStyle(
    'Subtitle',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=colors.HexColor('#4a4a6a'),
    spaceAfter=12,
    alignment=TA_CENTER
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=colors.HexColor('#1a1a2e'),
    spaceBefore=20,
    spaceAfter=10,
    fontName='Helvetica-Bold'
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['BodyText'],
    fontSize=11,
    textColor=colors.HexColor('#333333'),
    spaceAfter=8,
    leading=16,
    alignment=TA_JUSTIFY
)

highlight_style = ParagraphStyle(
    'Highlight',
    parent=styles['BodyText'],
    fontSize=10,
    textColor=colors.HexColor('#555555'),
    spaceAfter=6,
    leading=14,
    leftIndent=20
)

case_style = ParagraphStyle(
    'CaseStudy',
    parent=styles['BodyText'],
    fontSize=10,
    textColor=colors.HexColor('#2d5a7d'),
    spaceAfter=8,
    leading=14
)

# 内容列表
story = []

# 封面
story.append(Spacer(1, 100))
story.append(Paragraph("Claude AI 助手", title_style))
story.append(Spacer(1, 20))
story.append(Paragraph("专业介绍文档", subtitle_style))
story.append(Spacer(1, 40))
story.append(Paragraph("Anthropic 公司 | 2026", subtitle_style))

story.append(PageBreak())

# 第1页：什么是Claude
story.append(Paragraph("1. 什么是 Claude", heading_style))
story.append(Spacer(1, 12))
story.append(Paragraph(
    "Claude 是 Anthropic 公司开发的大型语言模型 AI 助手，以其安全性、可靠性和对话能力而著称。"
    "Claude 旨在成为有用的、无害的、诚实的 AI 助手，能够帮助用户处理各种任务，包括文本分析、"
    "编程、创意写作、研究等。",
    body_style
))

story.append(Spacer(1, 20))
story.append(Paragraph("2. 核心特性", heading_style))
story.append(Spacer(1, 8))

# 特性列表
features = [
    ["<b>安全性优先</b>", "基于宪法 AI 原则设计，遵循严格的道德准则"],
    ["<b>拒绝不当请求</b>", "能够识别并拒绝生成有害、不道德或非法内容"],
    ["<b>长上下文窗口</b>", "支持超长文本输入和理解，最高可达 200K tokens"],
    ["<b>复杂推理能力</b>", "能够进行多步推理和复杂问题分析"],
    ["<b>多模态支持</b>", "支持文本、图像等多种输入格式"],
    ["<b>代码理解生成</b>", "精通多种编程语言，能够阅读、理解和生成代码"]
]

feature_table = Table(features, colWidths=[2*inch, 3.5*inch])
feature_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f0f4f8')),
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
]))
story.append(feature_table)

story.append(PageBreak())

# 第2页：典型应用案例
story.append(Paragraph("3. 典型应用案例", heading_style))
story.append(Spacer(1, 10))

# 软件开发案例
story.append(Paragraph("<b>软件开发</b>", body_style))
story.append(Paragraph(
    "某金融科技公司使用 Claude 辅助开发交易系统。自动生成 API 文档、单元测试和代码审查。"
    "应用结果：提高开发效率 40%，减少 Bug 率 35%。",
    case_style
))
story.append(Spacer(1, 10))

# 学术研究案例
story.append(Paragraph("<b>学术研究</b>", body_style))
story.append(Paragraph(
    "研究人员使用 Claude 快速整理相关领域文献，提取关键信息，识别研究趋势，"
    "协助撰写研究报告和论文。显著缩短文献综述时间。",
    case_style
))
story.append(Spacer(1, 10))

# 内容创作案例
story.append(Paragraph("<b>内容创作</b>", body_style))
story.append(Paragraph(
    "数字营销公司使用 Claude 生成广告文案。根据目标受众调整语言风格和内容重点，"
    "生成 A/B 测试方案，提升转化率达 25%。",
    case_style
))
story.append(Spacer(1, 10))

# 企业决策案例
story.append(Paragraph("<b>企业决策</b>", body_style))
story.append(Paragraph(
    "投资机构使用 Claude 分析公司财报和行业报告。识别关键风险点和机会，"
    "辅助投资决策，分析准确率达 85%。",
    case_style
))

story.append(PageBreak())

# 第3页：技术优势与使用建议
story.append(Paragraph("4. 技术优势", heading_style))
story.append(Spacer(1, 8))

tech_features = [
    ["<b>架构特点</b>", "基于先进的 Transformer 架构"],
    ["<b>持续优化</b>", "不断迭代改进，提升性能和安全性"],
    ["<b>多版本选择</b>", "提供不同规模的模型以适应不同需求"],
    ["<b>API 接口</b>", "支持 RESTful API，易于集成到现有系统"],
    ["<b>插件系统</b>", "支持第三方插件扩展功能"],
    ["<b>多平台支持</b>", "兼容 Web、移动端和桌面端"]
]

tech_table = Table(tech_features, colWidths=[2*inch, 3.5*inch])
tech_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e8f4f8')),
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
]))
story.append(tech_table)

story.append(Spacer(1, 20))
story.append(Paragraph("5. 使用建议", heading_style))
story.append(Spacer(1, 8))

suggestions = [
    "• 明确提示需求，提供充分上下文",
    "• 验证重要信息的准确性",
    "• 结合人工判断进行关键决策",
    "• 内容创作与编辑",
    "• 代码开发与调试",
    "• 数据分析与研究"
]

for suggestion in suggestions:
    story.append(Paragraph(suggestion, body_style))

story.append(Spacer(1, 20))
story.append(Paragraph("6. 限制注意事项", heading_style))
story.append(Spacer(1, 8))
story.append(Paragraph(
    "不保证 100% 准确性，需要人工验证；不适合处理高度敏感的个人信息；"
    "需要遵守相关法律法规和道德准则。",
    body_style
))

story.append(PageBreak())

# 第4页：未来发展
story.append(Paragraph("7. 未来发展", heading_style))
story.append(Spacer(1, 12))
story.append(Paragraph(
    "Claude 正在不断演进，未来发展方向包括：更强的推理能力、多模态交互的深化、"
    "个性化服务、行业专业化定制。",
    body_style
))

story.append(Spacer(1, 40))
story.append(Paragraph("结语", heading_style))
story.append(Spacer(1, 12))
story.append(Paragraph(
    "Claude 作为新一代 AI 助手，凭借其安全性、可靠性和强大的能力，"
    "正在帮助各行各业提升效率、创新业务模式。正确使用 Claude，"
    "将成为个人和企业的重要生产力工具。",
    body_style
))

story.append(Spacer(1, 30))
story.append(Paragraph(
    "<i>注：本文档基于 Claude 的一般特性编写，具体功能可能随版本更新而变化。</i>",
    highlight_style
))

# 生成PDF
doc.build(story)

print("PDF文档已生成: claude_introduction.pdf")
