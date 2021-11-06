---
title: HTML复习
updated: '`r format(Sys.time(), ''%d %B, %Y'')`'
tags:
  - 网络基础
  - HTML
categories:
  - - 计算机网络
  - - Java Web
top_img: 'https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/000-Basic-HTML-Codes.jpg'
cover: >-
  https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/170427-637363828865101045-16x9.jpg
abbrlink: 3779978381
date: 2020-11-06 22:23:53
sticky:
password:
abstract:
message:
wrong_pass_message:
wrong_hash_message:
keywords:
description:
comments:
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

# 基本语法

HTML中基本的语法单位为**标签tag**。一般来说，标签用于指定内容的类别。对于每个类别，针对特定的内容，浏览器都有默认的显示方式。标签的语法是利用一对尖括号“<>”将标签名包围起来。大部分标签都是成对出现的，包括开始标签和结束标签。结束标签的名称就是在对应的开始标签名称前面添加一个斜杠“/”组成。开始标签和结束标签之间包含的信息称为标签的**内容content**。浏览器显示的HTML文档实际上就是显示了文档中所有标签的内容，**标签未必都包含内容**。

开始标签和结束标签就是为他们所包含的内容指定了一个**容器container**，容器及其内容一起称为**元素element**。

**属性Attribute**用于指定标签的含义，可以在开始标签名称及其右半边尖括号之间指定，它们是以键值的形式进行指定的：首先是属性的名称，接下来是一个等号，最后是属性值，属性值必须以双引号进行界定（数字可以不用双引号）。

注释格式：`<!--  -->`,可以用于单行或多行注释。

除注释外，还有一些其他类型的2文本可以出现在HTML文档中，但却会被浏览器忽略：无法识别的标签，空行（要使用空行，只能通过标签实现），多个空行或是制表符（也需要通过标签实现）。

# HTML文档的标准结构

每个HTML文档的第一行都是一个DOCTYPE，它指定了该文档所遵循的特定SGML文档类型定义（Document-Type Definition，DTD）。

```html
<!DOCTYPE html>
```

HTML文档必须包含以下四组标签：`<html>、<head>、<title>、<body>`。

标签`<html>`识别文档的根元素。因此在DOCTYPE命令之后，HTML文档中总是紧接着一个`<html>`标签，它包含一个属性，lang，用于指定编写文档所用的语言。

```html
<html lang="en">
```

一个HTML文档包含两部分：头(head)部分和主体(body)部分。

`<head>`元素包含了文档的头部分，该部分提供了文档的相关信息，而没有提供文档内容。他总是由两部分组成：一个标题元素和一个meta元素。meta元素用于提供关于文档的额外信息，他不包含任何内容，而是通过属性指定信息，meta标签至少要指定编写文档所用的字符集。

```html
<meta charset = "utf-8" />
```

标题元素的内容是在浏览器的顶部，通常是浏览器窗口的标题栏显示的。

文档的主体部分提供了文档的内容。

以下是HTML文档的基本结构

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>标题在这里</title>
    </head>
    <body>
        主体
    </body>
</html>
```

# 基本的文本标记

## 段落

一般情况下，文档主体中的文本采用多个段落的形式进行显示。段落元素是通过标签`<p>`指定的。嵌入文本中的换行符将被浏览器忽略，多个空格将被一个空格所替换。多个段落标签之间，将插入一个空白行。

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>标题在这里</title>
    </head>
    <body>
        <p> 多个空格会被忽略为一个，
    空格也会被忽略
    
    
        </p>
    </body>
</html>
```

![image-20201105160917282](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201105160917282.png)

## 换行

换行标签：`<br />`。

## 保留空白字符

有时希望在文本中保留空白字符，也就是阻止浏览器取消多个空格和忽略嵌入的换行符，可以使用`<pre>`标签来指定。

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>标题在这里</title>
    </head>
    <body>
        <pre> 
            原始格式      会  保  留
                 这样，
            
            
            再这样
        </pre>
    </body>
</html>
```

![image-20201105161238021](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201105161238021.png)

## 标题

HTML中，一共有六级标题，分别用以下标签表示：`<h1> <h2> <h3> <h4> <h5> <h6>`。绝大部分浏览器中 `<h1> <h2> <h3>`使用的字体要比默认文字大，`<h4>`使用默认文本字体大小，`<h5> <h6>`使用字体比默认小。

## 文本块引用

可以使用`<blockquote>`标签来表示引用文本。大部分情况下，这种引用文本块只是简单地双向缩进。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>标题在这里</title>
</head>
<body>
<p>
    这是正文部分
<blockquote>
        这是引用文本
</blockquote>
</p>
</body>
</html>
```

![image-20201105162134230](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201105162134230.png)

## 字体样式与大小

早先可以使用标签集来设置字体样式和大小，例如`<i>`指定斜体，`<b>`指定粗体。但有了层叠样式表，这些标签就变得过时了。但仍存在几个广泛使用的字体标签，称为基于内容的样式标签。之所以说基于内容，是因为标签指出了其内容中出现的文本的特定类型。下面描述三种最常用的基于内容的标签：强调标签 `<em> <strong>`和代码标签 `<code>`。

`<em>` 标签指定它的文本内容是特殊的，应该以能够表明这一点的某种方式来显示。大多数浏览器对这样的内容使用斜体。

`<strong>`标签类似于`<em>` 标签，但强调程度更强一些，经常被设置为粗体。

`<code>`用来指定等宽字体，通常用于程序代码。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>标题在这里</title>
</head>
<body>
<p>
    展示基于内容的标签：
    <br/>
    em标签:<em>强调，字体一般是斜体</em><br/>
    strong标签:<strong>强调，字体一般是粗体</strong><br/>
    code标签:
    <code>显示等宽字体，一般用于程序代码
    #include<stdio.h>
        int main(void){
        printf();
        }
    </code>
<br/>
</p>
</body>
</html>
```

![image-20201105163931465](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201105163931465.png)

可以使用 `<sub> <sup>`标签来指定下标和上标字符，这些标签不是基于内容的标签。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>标题在这里</title>
</head>
<body>
<p>
   x<sub>1</sub><sup>2</sup> + y<sub>1</sub><sup>2</sup> = x<sup>2</sup>
</p>
</body>
</html>
```

![image-20201105164238853](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201105164238853.png)

当基于内容的标签与块引用标签发生冲突时，块引用标签将会影响到这些标签的显示效果。

标签分为块标签和行内标签。行内标签的内容（如果能够放到当前行中）在当前行中进行显示，因此行内标签并不隐式包含一个换行，一个例外是换行标签。

## 字符实体

HTML提供了一组特殊字符，这些字符有时会出现在文档中，但不能以本身的样式进行拼写。这些特殊字符称为实体，是字符的代码。以下是最常用的字符实体。

| 字符    | 实体        | 含义       |
| ------- | ----------- | ---------- |
| &       | `&amp;`     | &的记号    |
| <       | `&lt;`      | 小于号     |
| >       | `&gt;`      | 大于号     |
| "       | `&quot;`    | 双引号     |
| '       | `&apos;`    | 单引号     |
| 1/4     | `&frac14;`  | 四分之一   |
| 1/2     | `&frac12;`  | 二分之一   |
| 3/4     | `&frace34;` | 四分之三   |
| °       | `&deg;`     | 度         |
| (space) | `&nbsp;`    | 非换行空格 |
| ©       | `&copy;`    | 版权符号   |
| €       | `&euro;`    | 欧元符号   |

## 水平线

`<hr />`标签可以用来绘制水平分割线。一般是3像素。它是一个块标签。

## meta元素的其他用法

meta元素用于提供文档的一些附加信息，主要供搜索引擎使用。除了前面用于指定字符集的charset属性，meta标签还可以使用：name属性，指定一个名称，最常用的名称是keywords；content属性，指定相关信息，与keywords相关系的content属性值被文档作者用来表示文档的特征，例如：

```html
<meta name = "keywords" content = "binary trees,linked lists,stacks" />
```

# 图片

图片元素的标签是 `<img />`,是一个行内元素，用于指定将要显示在文档中的图片。在最简单的情况下，该标签只包含两个属性：src和alt。通过src可以指定包含图片的文件；通过alt可以指定当图片无法显示时，提醒的文本内容。

img中还有两个可选属性，width和height，可以用来指定图片的宽度和高度。可以为图片的宽度或高度指定一个百分比值，表示图片将占据显示屏宽度或高度的百分之多少。

# 超链接

所有链接都通过锚元素`<a>`中的属性指定，它也是一个行内元素。锚标签也包含很多不同的属性，但为了创建链接，只有一个属性是必须的，即href(超文本引用，hypertext reference)。href的值指定了连接的目标文档。

如果某些元素包含一个id属性，可以使用锚标签来访问该目标元素。比如：

```html
<h2 id = "title2">Title 2 </h2>
```

我们可以使用

```html
<a href = "#title2">在id值前加一个#来访问同一文档中的元素</a>
```

访问其他文档的一个元素可以使用`URL#id值`得方式来访问。

# 列表

## 无序列表

HTML中可以使用块标签 `<ul>`来创建无序列表。列表中每个项目都是通过标签 `<li>` 指定的。所有标签都可以出现在列表项目中，包括嵌套的列表。在显示时，每个列表项目之前都对应着一个项目符号。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>标题在这里</title>
</head>
<body>
<h3>无序列表</h3>
<ul>
    <li>普通文字</li>
    <li><strong>嵌套强调</strong></li>
    <li>嵌套无序列表<ul>
        <li>嵌套内容1</li>
        <li>嵌套内容2</li>
        <li>嵌套内容3</li>
    </ul></li>
    <li>
        <a href="https://www.baidu.com">嵌套超链接</a>
    </li>
    <li><img src="404.png" width="50" height="50">嵌套图片</li>
</ul>
</body>
</html>
```

![image-20201105180805990](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201105180805990.png)

## 有序列表

有序列表可以通过块标签 `<ol>`创建。列表项目的指定与无序列表一样，有序列表项目前是一个顺序值。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>标题在这里</title>
</head>
<body>
<h3>有序列表</h3>
<ol>
    <li>普通文字</li>
    <li>嵌套无序列表
    <ul>
        <li>无序列表元素</li>
        <li>无序列表元素</li>
        <li>无序列表元素</li>
        <li>无序列表元素</li>
    </ul>
    </li>
    <li>
        嵌套有序列表
        <ol>
            <li>有序列表元素</li>
            <li>有序列表元素</li>
            <li>有序列表元素</li>
            <li>有序列表元素</li>
        </ol>
    </li>
</ol>
</body>
</html>
```

![image-20201105181304869](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201105181304869.png)

学习CSS之后可以指定不同级别的有序列表使用不同格式的数字。

## 定义列表

定义列表是指用于指定术语及其定义的列表。定义列表可以使用块标签 `<dl>` 来指定。定义列表中的每个术语是作为 `<dt>`元素的内容指定的，而定义本身是作为 `<dd>` 元素的内容指定的。一般，定义列表中定义的术语显示在左边缘，而定义通常成行的位于术语下方，并缩进显示。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>标题在这里</title>
</head>
<body>
<h3>定义列表</h3>
<dl>
    <dt>China</dt>
    <dd>中国</dd>
    <dt>America</dt>
    <dd>美国</dd>
    <dt>这里是术语内容</dt>
    <dd>这里是术语的定义内容</dd>
</dl>

</body>
</html>
```

![image-20201105213044170](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201105213044170.png)

# 表格

表格是单元格构成的矩阵。顶行单元格常常包含列标签，最左边列的单元格常常包含行标签，绝大部分其余的单元格包含表格数据。单元格中的信息几乎可以是任何形式的文档元素，如文本、标题、水平线、图片或嵌套的表格。表格用 `<table>`标签来创建。

## 基本的表格标签

绝大多数情况下，表格之前有标题，标题是在元素 `<caption>`的内容中指定的，他可以紧跟在开始标签 `<table>`之后。**表格的单元格是一行一行指定的**，表格中的每一行是通过行标签 `<tr>`指定的。在每一行，行标签是通过表头标签 `<th>`指定的。每一行的数据单元格是通过表格数据标签 `<td>`指定的。表格的首行通常指定了表格的列标签，例如，如果一个表格具有三个数据列，列标题分别为Apple、Orange、Screwdriver，那么可以按以下方式指定该表格的首行：

```html
<tr>
	<th> Apple </th>
	<th> Orange </th>
	<th> Screwdriver </th>
</tr>
```

表格中每一个数据行都是通过一个标题标签和针对每个数据列的数据标签指定的。对于那些既有行标签又有列标签的表格而言，表格的左上角单元格一般是空的。这个空的单元格是通过不含内容的表头标签指定的（`<th></th> 或 <th/>`。

下面是一个完整表格的示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>标题在这里</title>
</head>
<body>
<h3>定义表格</h3>
<table>
    <caption>学生信息表</caption>
    <tr>
        <!-- 第一行第一个为空 -->
        <th/>
        <th>姓名</th>
        <th>性别</th>
        <th>民族</th>
        <th>年龄</th>
        <th>住址</th>
    </tr>
    <tr>
        <th>1</th>
        <td>张三</td>
        <td>男</td>
        <td>汉</td>
        <td>20</td>
        <td>湖南</td>
    </tr>
    <tr>
        <th>2</th>
        <td>李四</td>
        <td>女</td>
        <td>汉</td>
        <td>18</td>
        <td>湖南</td>
    </tr>
    <tr>
        <th>3</th>
        <td>王五</td>
        <td>男</td>
        <td>汉</td>
        <td>21</td>
        <td>湖南</td>
    </tr>

</table>

</body>
</html>
```

![image-20201105220318174](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201105220318174.png)

## rowspan与colspan属性

很多情况下，表格具有多级行标签或者列标签。其中一个标签覆盖了两个或多个二级标签。可通过rowspan和colspan属性指定多级标签。

colspan属性是在表头或者表格数据标签中指定的，该属性命令浏览器将所在单元格的宽度扩展为等于下方行中指定数量的单元格宽度。

例如如下代码：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>标题在这里</title>
</head>
<body>
<h3>定义表格</h3>
<table>
    <tr>
        <th colspan="3">Fruit Juice Drinks</th>
    </tr>
    <tr>
        <th>Apple</th>
        <th>Orange</th>
        <th>Screwdriver</th>
    </tr>

</table>

</body>
</html>
```

![image-20201105221349290](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201105221349290.png)

Fruit Juice Drinks这一列包含了Apple、Orange、Screwdriver三列。

如果扩展单元格的上一行或下一行的单元格数目小于属性colspan指定的值，那么浏览器将把这些单元格的数目扩展到指定的数目，并为表格增加相应地列。表头标签和表格数据标签的属性rowspan表示跨越多行，其作用与colspan相似。

一个拥有两级列标签和行标签的表格，其左上角的单元格一定是空白，这个单元格既跨越了列中的多行标签，又跨越了多列。这种单元格是通过属性colspan和rowspan共同指定的。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>标题在这里</title>
</head>
<body>
<h3>定义表格</h3>
<table>
    <tr>
        <td rowspan="2"></td>
        <th colspan="3">果汁饮料</th>
    </tr>
    <tr>
        <th>苹果汁</th>
        <th>橘子汁</th>
        <th>草莓汁</th>
    </tr>
    <tr>
        <th>早餐</th>
        <td>0</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <th>中餐</th>
        <td>0</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <th>晚餐</th>
        <td>0</td>
        <td>1</td>
        <td>1</td>
    </tr>
</table>

</body>
</html>
```

![image-20201106093134190](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201106093134190.png)

## 表格分块

可以很自然的将表格分成两部分，有时候也可能是三部分：表头、主体以及表尾（不一定有表尾）。可以使用thead，tbody，tfoot元素来表示这三部分。表头包括列标签，而不管这些标签有多少级。主体包含了表格的数据部分，包含行标签。如果有表尾，表尾一般出现在主体之后，重复包含列标签。`<thead>` 元素内部必须包含一个或者多个 `<tr>` 标签。在 HTML 5 中，不再支持 HTML 4.01 中 `<thead>`> 标签的任何属性。`<thead>、<tbody> 和 <tfoot>`元素默认不会影响表格的布局。不过，您可以使用 CSS 来为这些元素定义样式，从而改变表格的外观。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>标题在这里</title>
</head>
<body>
<h3>定义表格</h3>
<table>
    <thead>
    <tr>
        <td rowspan="2"></td>
        <th colspan="3">
            Fruit Juice Drinks
        </th>
    </tr>
    <tr>
        <th>Orange juice</th>
        <th>Apple juice</th>
        <th>Screwdriver juice</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <th>
            Breakfast
        </th>
        <td>1</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <th>
            Lunch
        </th>
        <td>0</td>
        <td>1</td>
        <td>0</td>
    </tr><tr>
        <th>
            Dinner
        </th>
        <td>0</td>
        <td>0</td>
        <td>1</td>
    </tr>
    </tbody>
</table>

</body>
</html>
```

![image-20201106094745542](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201106094745542.png)

# 表单

用户通过Web浏览器与服务器之间进行通信的最常用手段是使用表单。HTML提供了一些标签以生成屏幕表单中最常用的对象。这些对象称为控件、小组件、组件。HTML中定义了多种控件：单行和多行的文本框、复选框、单选按钮以及菜单等。所有控件标签都是行内标签。绝大部分控件都是以文本或者按钮选择的形式来收集用户信息。每个控件都可以拥有一个值，通常是通过用户输入给定的。一个表单中所有控件的值合起来称为表单数据。每个表单都需要一个提交按钮。当用户单击提交按钮时，表单数据将被编码并发送到Web服务器进行处理。

## form元素

一个表单中所有控件都必须在标签form元素的内容中指定。 `<form>`是一个块标签，它有多个不同属性。属性action指定了Web服务器上一个应用程序的URL，当用户单击提交按钮，将调用这个应用程序。method属性的可选为get和post，这两种方法用于将表单数据发送给服务器；默认选择为get。**表单项数据若想提交，必须指定相应表单项标签的name属性**。

若使用get，浏览器会把查询字符串附加到HTTP请求的URL中。get方法可以在不使用表单的情况下传送参数给服务器，而post无法做到这一点。get方法的主要缺点是，服务器会对URL字符串长度进行限制，把超过长度的字符截去；会直接在地址中显示密码等敏感数据。

使用post方法，会有其他方法将查询字符串传递给表单处理程序。post方法对查询字符串长度没有限制，也不会暴露敏感信息。

- get：
	1. 请求参数会在地址栏中显示。
	2. 会封装到请求行中(HTTP协议后讲解)。请求参数大小是有限制的。
	3. 不太安全。

- post：
	1. 请求参数不会再地址栏中显示。会封装在请求体中(HTTP协议后讲解) 
	2. 请求参数的大小没有限制。
	3. 较为安全。

## input元素

许多常用控件都是利用行内标签 `<input>`指定的，这种标签可以指定文本框（text）、密码框（password）、复选框（checkbox）、单选按钮(radio)以及plain buttons、 ranges of numbers、 URLs、 electronic mailaddresses、reset、submit、image和button等动作按钮。

标签`<input>`必须使用的一个属性是type。这个属性用于指定控件的类型。除了submit和reset外，前述控件还需要name属性，其值将包含在表单数据中发送给服务器。复选框和单选按钮还需指定属性value，它用于初始化控件的值。当单击提交按钮时，这些控件的值作为表单数据发送给服务器。很多时候，客户端代码中也会引用控件，主要是为了进行客户端验证，客户端代码通过控件的id属性值引用它们，因此，常见做法时在表单控件元素中同时包含name和id属性。

通常文本控件称为文本框，该控件能创建一个水平框，用户可以在框中输入文本。文本框常用于收集用户信息。文本框默认长度一般为20个字符。我们可以通过 `<input>`标签的size属性来指定文本框的长度。如果用户输入的字符长度超出了文本框的空间，则文本框将可以滚动，如果不希望文本框滚动，可以在`<input>`标签中添加属性maxlength，该属性指定了浏览器允许该文本框能够接受的最大字符数目，将忽略多余数目。placehold属性可以添加提示信息，当输入信息时，该提示信息会自动清空。

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>表单演示</title>
    <meta charset="utf-8">
</head>
<body>
<p>
    <h2>表单演示</h2>
</p>
    <form action="404.html" method="get">
        <input type="text" name="text_field">
    </form>
</body>
</html>
```

![默认](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201106154040557.png)

> 未添加size属性和maxsize属性，文本框大小，此时文本框可以无限制输入任意文本。

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>表单演示</title>
    <meta charset="utf-8">
</head>
<body>
<p>
    <h2>表单演示</h2>
</p>
    <form action="404.html" method="get">
        <input type="text" name="text_field" size="50">
    </form>
</body>
</html>
```

![添加size属性](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201106154226323.png)

> 添加size属性后，文本框宽度便化，此时依旧可以无限制输入文本。

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>表单演示</title>
    <meta charset="utf-8">
</head>
<body>
<p>
    <h2>表单演示</h2>
</p>
    <form action="404.html" method="get">
        <input type="text" name="text_field" size="50" maxlength="25">
    </form>
</body>
</html>
```

![添加maxsize属性](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201106154427484.png)

> 添加maxsize属性后，其值大小后面的字符都不会再显示。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>表单标签</title>
</head>
<body>
<!--  表单要想提交必须指定name属性  -->
<form action="" method="get" name="login" >
     <label>用户名：<input type="text" name="username" placeholder="请输入用户名"></label><br/>
     <label>密  码：<input type="password" name="username" placeholder="请输入密码"></label>
</form>
</body>
</html>
```

![image-20201114204737915](D:%5CGitHub%5Chexo%5Csource%5C_posts%5CHTML%E5%A4%8D%E4%B9%A0.assets%5Cimage-20201114204737915.png)

> placehold属性用于显示提示信息。value属性可指定该字段的默认值，但是输入时不会自动清空。

如果想让用户在为文本框输入内容时隐藏输入的内容，就需要用到密码控件。

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>表单演示</title>
    <meta charset="utf-8">
</head>
<body>
<p>
    <h2>表单演示</h2>
</p>
    <form action="404.html" method="get">
        <input type="password" name="password" size="25">
    </form>
</body>
</html>
```

![密码表单](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201106154752019.png)

文本框以及其他大多数控件元素都应该有标签。只需将文本插入到表单中适当的位置，就可以完成添加标签任务，如

```html
phone:<input type="text" name="thePhone"/>
```

另外可以通过将控件及其标签放置到标签元素的内容中，将控件和他的标签联系起来：

```html
<label>Phone:<input type="text" name="thePhone"/></label>
```

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>表单演示</title>
    <meta charset="utf-8">
</head>
<body>
<p>
    <h2>表单演示</h2>
</p>
    <form action="404.html" method="get">
        <label>姓名:<input type="text" name="name" size="25"></label><br>
        <label>年龄:<input type="text" name="age" size="25"></label>
    </form>
</body>
</html>
```

![标签元素](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201106155032264.png)

复选框和单选按钮控件用来收集用户的多重选择输入。复选框控件是一个按钮，表示开或者关，即选中与否。每个复选框对应的input标签必须具有属性name和value。如果一个复选框处于选中状态，该按钮name的值就是指派给value的字符串。如果未选中，则表单中没有其信息。如果存在属性checked，且checked的值为checked，那么表示这个复选框默认选中。通常多个复选框以列表形式显示，每个按钮的name都是相同的。复选框也应该出现在标签元素中。

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>表单演示</title>
    <meta charset="utf-8">
</head>
<body>
<p>
    <h2>表单演示</h2>
</p>
    <form action="404.html" method="get">
        <p>爱好：
            <label><input type="checkbox" name="hobby" value="play_game" checked="checked">玩游戏</label><br>
            <label><input type="checkbox" name="hobby" value="reading">阅读</label><br>
            <label><input type="checkbox" name="hobby" value="watch_movie">看电影</label><br>
            <input type="submit" value="提交表单">
        </p>
    </form>
</body>
</html>
```

![复选框](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201106162233997.png)

单选按钮与复选按钮类似。

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>表单演示</title>
    <meta charset="utf-8">
</head>
<body>
<p>
    <h2>表单演示</h2>
</p>
    <form action="404.html" method="get">
        <p>性别：<br>
            <label><input type="radio" name="sex" value="male" checked="checked">男</label><br>
            <label><input type="radio" name="sex" value="female">女</label><br>
            <input type="submit" value="提交表单">
        </p>
    </form>
</body>
</html>
```

![单选按钮](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201106162529577.png)

* radio:单选框
  注意：
  	1. 要想让多个单选框实现单选的效果，则多个单选框的name属性值必须一样。
  	2. 一般会给每一个单选框提供value属性，指定其被选中后提交的值
  	3. checked属性，可以指定默认值

  - checkbox：复选框
  	注意：
  	1. 一般会给每一个单选框提供value属性，指定其被选中后提交的值
  	2. checked属性，可以指定默认值

label标签可用于指定输入项的文字描述信息，它的for属性一般与input的id属性值对应。如果对应了，则点击label区域，会让input输入框获取焦点。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>表单标签</title>
</head>
<body>
<!--  表单要想提交必须指定name属性  -->
<form action="" method="get" name="login" >
     <label for="username">用户名：<input type="text" name="username" placeholder="请输入用户名" id="username"></label><br/>
     <label for="password">密  码：<input type="password" name="username" placeholder="请输入密码" id="password"></label>
</form>
</body>
</html>
```

![image-20201114205636332](D:%5CGitHub%5Chexo%5Csource%5C_posts%5CHTML%E5%A4%8D%E4%B9%A0.assets%5Cimage-20201114205636332.png)

> 当点击用户名或密码时，光标（输入焦点）会跳到用户名或密码输入框。

简单按钮（plain button）可以使用button来指定。按钮可以触发JavaScript活动。

## select元素

复选框和单选框是收集用户多重选择数据的有效方式，但是当选择数目较大时，表单将难以显示，此时可以使用菜单。菜单是通过标签 `<select>`指定的。菜单有两种类型：一次只能选择一个菜单项的菜单（默认）和一次可以选择多个菜单项的菜单（在select中添加属性multiple，并将值设置为multiple即可使用）。`<select>`的name属性是必需的。还可以包含size属性用于指定为用户现实的菜单项的数目，未指定size时，默认为1。如果size的值为1，但未指定multiple属性，就显示一个带有向下滚动箭头的菜单项，单击滚动箭头，菜单将弹出显示。如果指定了multiple属性，或者size的值大于1，那么菜单通常为一个滚动列表。

菜单中每个条目是通过标签 `<option>`指定的，他嵌套在`<select>`元素中，其内容就是菜单项的值，只能是文本，不能包含其他标签；属性有selected，如果将其值设为selected，则表示该条目默认已经选中。

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>Select</title>
    <meta charset="utf-8">
</head>
<body>
<select name="menu" size="1">
    <option checked="checked">----</option>
    <option>湖南</option>
    <option>湖北</option>
    <option>上海</option>
    <option>北京</option>
    <option>深圳</option>
</select>

</body>
</html>
```

![未设置multiple](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201106164743266.png)

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>Select</title>
    <meta charset="utf-8">
</head>
<body>
<select name="menu" multiple="multiple">
    <option checked="checked">----</option>
    <option>湖南</option>
    <option>湖北</option>
    <option>上海</option>
    <option>北京</option>
    <option>深圳</option>
</select>

</body>
</html>
```

![设置multiple](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201106164900449.png)

设置了multiple属性可以选中多个。

## textarea元素

可以使用标签 `<textarea>`创建一个能够输入多行文本的区域。可以使用属性rows和cols为其设置适当大小。也可以在其中添加一些默认文本。

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>TextArea</title>
    <meta charset="utf-8">
</head>
<body>
    <textarea name="text" cols="40" rows="10">
        这里是默认文本
    </textarea>
</body>
</html>
```

![image-20201106165530118](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201106165530118.png)

## 动作按钮

重置按钮可以将表单所有控件恢复到初始状态。提交按钮的作用分为两步，首先将表单数据编码并发送到服务器，然后请求服务器执行驻留在服务器中的通过标签`<form>`的action指定的程序。提交按钮和重置按钮都是通过 `<input>`创建的，其value属性可以指定在按钮显示的文本。

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>表单演示</title>
    <meta charset="utf-8">
</head>
<body>
<p>
    <h2>表单演示</h2>
</p>
    <form action="404.html" method="get">
        <p>性别：<br>
            <input type="submit" value="提交按钮">
            <input type="reset" value="重置按钮">
        </p>
    </form>
</body>
</html>
```

![image-20201106170039912](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201106170039912.png)

## 一个表单例子

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>Popcorn</title>
    <meta charset="utf-8">
</head>
<body>
<h2>Welcome to Millenium Gynmastics Booster Club Popcorn Sales</h2>
<form>
    <p>
        <label>Buyer's name: <input type="text" size="40"></label><br>
        <label>Street Address: <input type="text" size="40"></label><br>
        <label>City,State,Zip: <input type="text" size="40"></label><br>
    </p>
    <p>
    <table>
        <tr>
            <th>
                Product Name
            </th>
            <th>
                Price
            </th>
            <th> Quantity</th>
        </tr>
        <tr>
            <td>Unpopped Popcorn(1 lb)</td>
            <td>$3.00</td>
            <td><input type="text" size="2"></td>
        </tr>
        <tr>
            <td>Caramel Popcorn(2 lb cannister)</td>
            <td>$3.50</td>
            <td><input type="text" size="2"></td>
        </tr>
        <tr>
            <td>Caramel Nut Popcorn(2 lb cannister)</td>
            <td>$4.50</td>
            <td><input type="text" size="2"></td>
        </tr>
        <tr>
            <td>Toffey Nut Popcorn(2 lb cannister)</td>
            <td>$5.00</td>
            <td><input type="text" size="2"></td>
        </tr>
    </table>
    </p>
    <h3>Payment Method</h3>
    <label><input type="radio" name="payment_method" checked="checked">Visa</label><br>
    <label><input type="radio" name="payment_method">Master Card</label><br>
    <label><input type="radio" name="payment_method">Discover</label><br>
    <label><input type="radio" name="payment_method">Check</label><br>
    <input type="submit" value="Submit Order">
    <input type="reset" value="Clear Order Form">
</form>
</body>
</html>
```

![image-20201106173257134](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201106173257134.png)

# HTML5

## audio元素

audio元素唯一的常用属性是controls，他总是被设置为controls，该属性会显示一个开始/停止按钮，一个时钟，一个播放进度条，文件的总时长以及一个音量控制滑动条。

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>Audio</title>
    <meta charset="utf-8">
</head>
<body>
<audio controls="controls">
    <source src="someMusic.mp3">
    <source src="someMusic.ogg">
    <source src="someMusic.wav">
</audio>
</body>
</html>
```

![image-20201106202040956](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201106202040956.png)

## video元素

video元素有几个属性，并且与audio元素一样可以包含多个嵌套的source元素。width和height属性以像素为单位设置视频屏幕的宽度和高度；autoplay属性指定在准备好后自动播放；preload属性告诉浏览器在文档加载时就载入视频；controls属性在视频播放时显示开始、暂停和音量条；loops属性指定视频是否循环播放。

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>TextArea</title>
    <meta charset="utf-8">
</head>
<body>
<video width="720" height="600" controls="controls" preload="auto">
    <source src="video.mp4" type="video/mp4">
</video>
</body>
```

![image-20201106213708505](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201106213708505.png)

## 组织元素

HTML4.01实现大纲的唯一方式时使用标题，但是符合逻辑的做法是一个文档中只使用一个h1标题。而且h2，h3等标题元素必须按照编号进行嵌套。HTML5提供了一些新的元素来帮助组织文档和文档的大纲。

许多文档的第一个部分是标题，如果标题只包含一个短语，那么可以是一个h1元素，但文档的标题经常包含更多的信息，很多时候还包含第二个短语，或者叫做标语（tagline）。HTML5的header元素可以包含文档的整个标题，这样就更容易看出标题包含哪些部分。

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>TextArea</title>
    <meta charset="utf-8">
</head>
<body>
<h1>普通的一级标题</h1>
<h2>普通的二级标题</h2>

<header>
    <h1>在header元素中的一级标题</h1>
    <h2>在header元素中的二级标题</h2>
</header>
</body>
```

文档的开始部分可能在主体的前面包含更多信息，如一个目录，可以使用hgroup元素包含标题和主体前面的其他信息。

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>TextArea</title>
    <meta charset="utf-8">
</head>
<body>
<hgroup>
    <header>
        <h1>一级标题</h1>
        <h2>二级标题</h2>
    </header>
    ----文档主体部分----
</hgroup>
</body>
```

footer元素用于包含文档中的页脚内容，例如作者和版权数据。

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>TextArea</title>
    <meta charset="utf-8">
</head>
<body>
<hgroup>
    <header>
        <h1>一级标题</h1>
        <h2>二级标题</h2>
    </header>
    <p>----在这里插入文档主体----</p>
</hgroup>
<footer>
    &copy;不二承 2018-2020
</footer>

</body>
```

![image-20201106220537204](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201106220537204.png)

section元素用于包含文档的各节，footer可以包含一节或多节；article元素用于容纳来自外部的某个文档的独立部分。一个article元素可以包含一个header、一个footer和多个section。

adise元素用于与文档的主要信息关系不大的内容。

nav元素用于包含导航部分，也就是可以导航到文档不同部分的链接列表。

## time元素

time元素用于给文章或文档添加时间戳。该元素包含一个文本部分和一个机器可读部分。文本部分的时间和或日期信息可以是任意格式的，但是机器可读部分必须有严格的格式化。机器可读部分是time元素可选属性datetime的值。datetime的date部分的格式是：一个有4位数字表示的年份，横线，一个有两位数字表示的月份，横线和一个两位数字表示的天，例如2020-11-06；如果机器可读的数据中包含时间，则要在日期后面加上大写T，后面是小时冒号分钟冒号和秒。如果秒为0，可以省略。小时，分钟，秒必须以两位数字表示。time元素还有另一个可选的属性pubdate。如果time元素没有嵌套在一个article元素内，那么pubdate指定的时间戳是文档的发布日期。如果嵌套在article元素内，则是文章的发布日期。