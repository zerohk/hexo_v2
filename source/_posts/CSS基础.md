---
title: CSS基础
updated: '`r format(Sys.time(), ''%d %B, %Y'')`'
tags:
  - 网络基础
  - CSS
categories:
  - CSS
  - 前端
top_img: 'https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/css_base_top.jpg'
cover: 'https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/css_base_cover.jpg'
abbrlink: 1503359168
date: 2020-12-14 18:35:36
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

# 概念及优点

## 概念

- css：Cascading Style Sheets 层叠样式表。
- 层叠：多个样式可以作用在同一个html的元素上，同时生效

## 优点

- 功能强大

- 将内容展示和样式控制分离

	- 降低耦合度。解耦

	- 让分工协作更容易

	- 提高开发效率

# CSS的使用

## CSS与HTML结合

### 内联样式

在**标签内**使用**style**属性指定css代码。此方式不常用。

如：

```html
<div style="color:red;">hello css</div>
```

### 内部样式

 在**head标签**内，定义**style**标签，style标签的标签体内容就是css代码。常用。

```html
<style>
    div{
        color:blue;
	   }
		
</style>
<div>hello css</div>
```

## 外部样式

定义css资源文件。在head标签内，定义link标签，引入外部的资源文件。常用。

### 代码演示

```css
/* waibu.css*/
div {
    color : red;
}
```

```html
<!DOCTYPE html>
<html lang="cn">
<head>
    <meta charset="UTF-8">
    <title>外部样式</title>
    <link rel = "stylesheet" href="css/waibu.css">
</head>
<body>
<div>外部样式</div>
</body>
</html>
```

或者

```html
<!DOCTYPE html>
<html lang="cn">
<head>
    <meta charset="UTF-8">
    <title>外部样式</title>
    <style>
        @import "css/waibu.css";
    </style>
</head>
<body>
<div>外部样式</div>
</body>
</html>
```

![image-20201214190047324](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201214190047324.png)

# CSS语法

## 基础格式

```css
选择器 {
			属性名1:属性值1;
			属性名2:属性值2; /* 每一对属性用分号;分隔，最后一个可加可不加*/
			...
		}
```

## 选择器

筛选具有相似特征的元素。

### 基础选择器

1. **ID选择器**：选择具体的id属性值的元素.建议在一个html页面中id值唯一。
	- 语法：`#id属性值{}`
2. **元素选择器**：选择具有相同标签名称的元素。
	- 语法：`标签名称{}`
	- 注意：ID选择器优先级高于元素选择器。
3.  **类选择器**：选择具有相同的class属性值的元素。
	-  语法：`.class属性值{}`
	- 注意：类选择器优先级高于元素选择器。

### 扩展选择器

1. 选择所有元素。

	- 语法：`*{}`

2. 并集选择器：

	- 语法：`选择器1,选择器2{}`

3. 子选择器：筛选选择器1元素下的所有子选择器2元素

	- 语法：`选择器1 选择器2{}`

4. 父选择器：筛选选择器2元素的父选择器1元素

	- 语法：`选择器1 > 选择器2{}`

5. 属性选择器：选择属性名称，属性名=属性值的元素

	- 语法：`属性名称[属性名 = 属性值] {}`

6. 伪类选择器：选择一些元素具有的状态。

	- 语法：`元素：状态{}`

	- 例如：`<a>`标签元素具有以下几种状态：

		- link：初始化的状态
		- visited：被访问过的状态
		- active：正在访问状态
		- hover：鼠标悬浮状态。

		可以使用：`a:link{}`的形式指定连接样式。

## 属性

以下是常用属性。

### 字体、文本

- font-size：字体大小
- color：文本颜色
- text-align：对其方式
- line-height：行高 

### 背景

- background

### 边框

- border

### 尺寸

- height：高度
- width：宽度

### 盒子模型

- margin：外边距

- padding：内边距
	- 默认情况下内边距会影响整个盒子的大小
	- box-sizing: border-box;  设置盒子的属性，让width和height就是最终盒子的大小

- float：浮动
	 - left
	 - right

# CSS注册页面

```html
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>注册页面</title>
    <link rel="stylesheet" href="css/register.css">
</head>
<body class="body">
<div class="outer">
    <div class="info">
        <label class="cn_info">新用户注册</label><br>
        <label class="en_info">USER REGISTER</label>
    </div>
    <div class="register">
        <form class="form" method="post" action="#">
            <table class="table">
                <tr>
                    <lable for="username">
                        <td id="u_name">用户名</td>
                        <td><input name="username" placeholder="请输入用户名" id="username"></td>
                    </lable>
                </tr>
                <tr>
                    <lable for="password">
                        <td id="paw">密码</td>
                        <td><input type="password" name="password" placeholder="请输入密码" id="password"></td>
                    </lable>
                </tr>
                <tr>
                    <lable for="email">
                        <td id="em">Email</td>
                        <td><input type="email" name="email" placeholder="请输入email" id="email"></td>
                    </lable>
                </tr>
                <tr>
                    <lable for="name">
                        <td id="nam">姓名</td>
                        <td><input name="name" placeholder="请输入姓名" id="name"></td>
                    </lable>
                </tr>
                <tr>
                    <lable for="mobilephone">
                        <td id="tel">手机号</td>
                        <td><input name="mobilephone" placeholder="请输入手机号" id="mobilephone"></td>
                    </lable>
                </tr>
                <tr>
                    <td id="sex">性别</td>
                    <td>
                        <input type="radio" name="gender" id="male" value="male" checked>男
                        <input type="radio" name="gender" id="female" value="female">女
                    </td>
                </tr>
                <tr>
                    <td id="birth">出生日期</td>
                    <td><input type="date" name="birthday" id="birthday"></td>
                </tr>
                <tr>
                    <lable for="captcha">
                        <td id="code">验证码</td>
                        <td><input name="captcha" id="captcha"> <img src="img/verify_code.jpg" id="captcha_pic"></td>
                    </lable>
                </tr>
                <tr>
                    <td colspan="2" align="center"><input type="submit" value="" id="register_button"></td>
                </tr>
            </table>
        </form>
    </div>
    <div class="login">
        已有账号？<label id="login"><a href="#">立即登录</a> </label>
    </div>
</div>
</body>
</html>
```

```css
.body {
    background: aliceblue url("../img/register_bg.png") no-repeat fixed center;
}

.outer {
    margin: auto;
    margin-top: 25px;
    padding: 20px;
    width: 1000px;
    height: 500px;
    border: 5px solid darkgray;
    background-color: white;
}

.info {
    float: left;
    margin: 15px;
}

.cn_info {
    color: darkorange;
    font-size: 25px;
    margin: 20px;
}

.en_info {
    color: gray;
    font-size: 25px;
    margin: 20px;
}

.form {
    float: left;
}

#u_name, #paw, #em, #nam, #tel, #sex, #birth, #code {
    text-align: right;
    width: 100px;
    height: 50px;
    color: gray;
    padding-right: 35px;
}

#username, #password, #email, #name, #mobilephone, #birthday {
    border: 1px solid darkgray;
    border-radius: 0.4em;
    height: 30px;
    width: 300px;
    padding-left: 15px;
}

#captcha, #captcha_pic {
    height: 30px;
    width: 100px;
    border: 1px solid darkgray;
    border-radius: 0.4em;
    vertical-align: middle;
}

#register_button{
    border: 0px;
    background: url("../img/regbtn.jpg");
    width: 101px;
    height: 32px;
}

.login {
    float: right;
    margin: 15px;
}

a:link {
    color: coral;
}
```

![image-20201214183345704](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201214183345704.png)

