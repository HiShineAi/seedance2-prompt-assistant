---
name: claude-code
description: Claude Code 技能，提供代码解释、代码生成和代码调试功能，支持切换到 GLM4.7 模型。
license: MIT
---

# Claude Code

Claude Code 是一个专门用于代码相关任务的技能，提供代码解释、代码生成、代码调试等功能，并支持切换到 GLM4.7 模型。

## 功能特性

- **代码解释**：分析代码的功能、结构和逻辑，提供详细的解释。
- **代码生成**：根据用户需求生成各种编程语言的代码。
- **代码调试**：帮助用户找出代码中的错误并提供修复建议。
- **代码优化**：分析代码性能，提供优化建议。
- **模型切换**：支持切换到 GLM4.7 模型以获得更好的代码处理能力。

## 快速开始

### 使用 Claude Code 解释代码

```python
# 示例：解释以下代码

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 调用函数
print(fibonacci(10))
```

### 使用 Claude Code 生成代码

```python
# 示例：生成一个计算阶乘的函数

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 调用函数
print(factorial(5))
```

### 切换到 GLM4.7 模型

要切换到 GLM4.7 模型，请使用以下命令：

```
/model switch glm4.7
```

切换后，所有代码相关的任务将使用 GLM4.7 模型处理，以获得更好的代码理解和生成能力。

## 支持的编程语言

Claude Code 支持多种编程语言，包括但不限于：

- Python
- JavaScript
- Java
- C++
- C#
- Go
- Rust
- PHP
- Ruby
- TypeScript
- HTML/CSS
- SQL

## 高级功能

### 代码审查

Claude Code 可以帮助您审查代码，找出潜在的问题和改进空间。

### 技术文档生成

Claude Code 可以根据代码生成技术文档，包括 API 文档、使用指南等。

### 框架特定代码

Claude Code 熟悉各种流行的框架和库，可以生成符合特定框架规范的代码。

## 注意事项

- 切换到 GLM4.7 模型后，某些功能可能会有所不同。
- 对于复杂的代码任务，可能需要提供更多的上下文信息。
- 生成的代码可能需要根据具体环境进行调整。
