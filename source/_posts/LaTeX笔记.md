---
title: LaTeX笔记
updated: '`r format(Sys.time(), ''%d %B, %Y'')`'
abbrlink: 4276076626
date: 2021-01-20 10:59:14
sticky:
tags: [LaTeX]
categories:
password:
abstract:
message:
wrong_pass_message:
wrong_hash_message:
keywords:
description:
top_img: https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/LaTeX_top.png
comments:
cover: https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/LaTeX_cover.png
toc:
toc_number:
auto_open:
copyright:
copyright_author:
copyright_author_href:
copyright_url:
copyright_info:
mathjax:
katex:
aplayer:
highlight_shrink:
---

# 字符

LaTeX中能够出现的字符:

- 26个英文字母，包括大小写；
- 0-9十个数字；
- 出现在input file的十六个标点符号：
	- `. , ; : ! ? ‘ ’ ( ) [ ] / - * @`
	- 注意单引号的输入方式：左边输入`，右边输入'；
- 出现在command中的十个特殊符号：
	- `~ # $ % ^ & _ \ { }`
	- 大多数LaTeX command会以 `\` 开头；
- 用于数学公式的五个符号：
	- `+ = | < >`
	- `+`和 `=` 也能用于原始文本；
- `"`极少使用；
- 不可见字符如空格和回车，统一视作空格；
	- 输入的多个空格只视作一个空格；
- 空行，只包括空格的行，会被LaTeX解译为一段的结束。

# 输入

大多数LaTeX命令描述了文档的逻辑结构。要了解这些命令，必须知道LaTeX是怎样感知逻辑结构的。一个文档包含了不同大小的逻辑结构，先从非常熟悉的中间大小的结构--句子和段落谈起。

## 句子和段落

简单的句子和段落对LaTeX来说是没有任何问题的：

```latex
\documentclass[UTF8]{ctexart} 
\begin{document}
The ends of words and setences are marked by spaces. It doesn't matter how many spaces     you
type; one is as good as 100.

One or more   blank lines denote the end of a paragraph.
\end{document}
```

![sentences](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210119151439436.png)

### 引号（Quotation Marks）

LaTeX中有四个引号：左右单引号，左右双引号。双引号可以由两个单引号得到。

左单引号可以使用 `得到；右单引号可以使用'得到；

左双引号可以使用``得到；右双引号可以使用''得到。

```latex
\documentclass[UTF8]{ctexart} 
\begin{document}
单引号： 左单引号`，右单引号'

双引号： 左双引号``，右双引号''
\end{document}
```

![引号示例](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210119152200905.png)

双引号后面跟着一个单引号，或者单引号后跟着一个双引号，碰到这种情况时，```，会让我们觉得模棱两可。解决的办法是，在两个符号之间添加一个命令 \,(反斜杠加一个逗号)。

```latex
\documentclass[UTF8]{ctexart} 
\begin{document}
``\,`十一'还是`十二'\,''他问道。
\end{document}
```

![单双引号同时出现](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210120093323050.png)

### 破折号（Dashes）

可以使用三种大小的破折号：

- 用于字母间的连字符，由一个 - 表示；
- 用于表示数字的范围，由两个 -- 表示；
- 用于标点的长破折号，由三个 --- 表示。

```latex
\documentclass[UTF8]{ctexart} 
\begin{document}
用于字母间的连字符：X-Ray

用于表示数字范围：1--2

用于表示标点的长破折号： 就像这样---
\end{document}
```

![三种破折号](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210120094516722.png)

注意：通常在破折号之前和之后都没有空格；破折号不是减号，减号只能用于数学公式中。

### 句点（Period）后的空格

排字工人通常会在一句话的结尾的句点（.）处添加一些额外的空格，来表示句子的结束。对于人类来说，这是很容易的，但是对于TeX来说，就不那么容易了。因为它无法判断一个句点是否位于句子的结尾。TeX简单的将一个未跟在大写字母后的句点当作句子的结尾。大多数情况下，这样是可行的。但是，当面对一些简写，例如"etc."，这样处理就会产生问题。你可以在句点后使用 \space（\后跟空格或者是一行的结尾）命令告诉TeX，这个句点不是句子的结尾。反斜杠之后无论多少个空格都是可行的，但是不能在句点和反斜杠之间添加空格。

```latex
\documentclass[UTF8]{ctexart} 
\begin{document}
This is a sentence.This another sentence. % 未跟在大写字母后，也没有使用\space命令，表示是一句话的结尾

This is a sentencE.you know.  % 跟在大写字母后，表示不是一句话的结尾

There just one sentence.\ not two. % 使用了\space 命令，表示不是一句话的结尾

There is another example.\
hahaha

test. \ oh
\end{document}
```

![image-20210120102310753](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210120102310753.png)

在某些情况下，即使句点是跟在大写字母后，也表示句子的结束。此情况下，你需要在句点前使用\@命令告诉TeX句点位于句子的结尾。

```latex
\documentclass[UTF8]{ctexart} 
\begin{document}
The Romans wrote I + I = II\@.Really!
\end{document}
```

![image-20210120104404943](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210120104404943.png)

如果表示句子结尾的句点后面跟了右圆括号，或者右引号（单、双），需要在圆括号或者引号后边添加多余的空格（使用\space命令)。

```latex
\documentclass[UTF8]{ctexart} 
\begin{document}
``Beans (lima,etc.)\  hava vitamin B\@.''
\end{document}
```

![image-20210120105509841](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210120105509841.png)

`? ! :`也需要在它们的后面添加额外的空格，除非它们跟在一个大写字母之后。\space和\@和在句点中的使用方法是一致的。