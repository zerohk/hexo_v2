---
title: 'IDEA构建错误:Gradle:Cause:zip END header not found'
tags:
  - java基础
  - 编译错误
categories: 
	- [java]
	- [教程]
	- [IDEA]
	- [Gradle]
keywords:
	- IDEA
    - JAVA
    - GRADLE
    - Cause-zip-END-header-not-found
top_img: 'https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/20201018190550.png'
cover: 'https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/20201018190550.png'
abbrlink: 3790347158
date: 2020-10-18 19:09:43
updated: 2020-10-18 19:09:43
sticky:
password:
abstract:
message:
wrong_pass_message:
wrong_hash_message:
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

# 1.问题复现

在[hyperskill](https://hyperskill.org/)学习Java时，之前导入项目都好好的。由于换了个账号（可能是切换了账号的原因），打开学习项目时，提示如下，运行按钮是灰的，并且提示：

![](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/20201018191932.png)

按提示点击按钮后，出现`build failed`：

![没有截图，网上找的图](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/20200917144049894.png)

# 2.解决方法

按照这篇教程：[idea使用gradle进行build时报错 Cause: zip END header not found](https://blog.csdn.net/bhfswrcn/article/details/107116657)的方法，修改了配置

![修改配置](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/20201018193701.png)

重新构建，问题依然存在。

再次搜索了一下，按照这篇文章[问题: gradle Cause: zip END header not found](https://blog.csdn.net/haiquanquan123456/article/details/108642649)试了一下，还是不行。

改变思路。

同时更改了`gradle-wrapper.properties`文件，配置如下：

```gradle
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
#把远程地址注释掉
#distributionUrl=https\://services.gradle.org/distributions/gradle-6.6.1-bin.zip
#使用本地的gradle包
distributionUrl=file:///D:/IdeaProjects/gradle-6.7-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
```

找到`File->settings->Build,Execution,Deployment->Build Tools`下的`gradle`选项，设置为图中所示即可

![gradle设置](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/20201018195116.png)

重新build：

![重新build中](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/20201018194314.png)

![build成功](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/20201018195444.png)

build成功后，右键运行一次后，即可开始写代码了。

![右键运行](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/20201018195702.png)

这里不再是灰色了！

![ToolBar](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201018195813307.png)

# 3.小结

中间踩过的其他坑就不详细记述了，我太难了。