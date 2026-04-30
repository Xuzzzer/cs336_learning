# CS336 自学仓库

这个仓库用于记录我自学 Stanford CS336: Language Modeling from Scratch 的代码、作业实现和学习笔记。

参考资料：
- Stanford CS336: <https://stanford-cs336.github.io/spring2025/>
- CS336 官方作业：<https://github.com/stanford-cs336>
- 中文资料：[`diy-llm/`](./diy-llm/)

## 目录

```text
.
├── assignment1-basics/   # 官方 Assignment 1: tokenizer、Transformer、optimizer 等基础实现
├── diy-llm/              # 中文课程资料、笔记和各章节作业
├── TinyStories/          # TinyStories 数据
├── main.py
└── pyproject.toml
```

## 环境

安装 `uv`：

```bash
conda create -n cs336 python=3.11
conda activate cs336
pip install uv
```

进入具体作业目录后运行：

```bash
uv sync
uv run pytest
```

## 学习记录

### Assignment 1: Basics

| Day 1 | Day 2 | Day 3 | Day 4 | Day 5 |
|---|---|---|---|---|
| 4.26 lecture1 | 4.27 lecture2 | 4.30 BPE tokenizer | 日期：<br>内容： | 日期：<br>内容： |

### Assignment 2: Systems

| Day 1 | Day 2 | Day 3 | Day 4 | Day 5 |
|---|---|---|---|---|
| 日期：<br>内容： | 日期：<br>内容： | 日期：<br>内容： | 日期：<br>内容： | 日期：<br>内容： |

### Assignment 3: Scaling

| Day 1 | Day 2 | Day 3 | Day 4 | Day 5 |
|---|---|---|---|---|
| 日期：<br>内容： | 日期：<br>内容： | 日期：<br>内容： | 日期：<br>内容： | 日期：<br>内容： |

### Assignment 4: Data

| Day 1 | Day 2 | Day 3 | Day 4 | Day 5 |
|---|---|---|---|---|
| 日期：<br>内容： | 日期：<br>内容： | 日期：<br>内容： | 日期：<br>内容： | 日期：<br>内容： |

### Assignment 5: Alignment

| Day 1 | Day 2 | Day 3 | Day 4 | Day 5 |
|---|---|---|---|---|
| 日期：<br>内容： | 日期：<br>内容： | 日期：<br>内容： | 日期：<br>内容： | 日期：<br>内容： |

### Assignment 6: Evaluation

| Day 1 | Day 2 | Day 3 | Day 4 | Day 5 |
|---|---|---|---|---|
| 日期：<br>内容： | 日期：<br>内容： | 日期：<br>内容： | 日期：<br>内容： | 日期：<br>内容： |

## 思考问题整理

### Assignment 1
Problem (unicode2) -2:
```bash 
def decode_utf8_bytes_to_str_wrong(bytestring: bytes):
return "".join([bytes([b]).decode("utf-8") for b in bytestring])
>>> decode_utf8_bytes_to_str_wrong("hello".encode("utf-8"))
'hello'
```
bytes([b]) 会把一个 0~255 的整数变成单个字节；但 UTF-8 里一个字符可能由多个字节组成，所以不能每个字节单独 decode。