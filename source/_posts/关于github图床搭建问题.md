---
title: 关于github图床搭建问题
sticky: 1
tags:
  - github
  - 图床
categories: 教程
keywords:
  - github
  - 图床
  - picgo
  - jsdelivr
top_img: /pics/1800832272_top.jpg
cover: /pics/1800832272_cover.jpg
abbrlink: 1800832272
date: 2020-10-08 18:15:48
updated: "`r format(Sys.time(), '%d %B, %Y')`"
description: 阅读全文
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

按照网上的教程，使用github+PicGo+jsDelivr的方式搭建免费图床，配置如下，

![](https://gitee.com/fkso/blogpics/raw/master/master/%E5%85%B3%E4%BA%8Egithub%E5%9B%BE%E5%BA%8A%E6%90%AD%E5%BB%BA%E9%97%AE%E9%A2%981.png)

一直显示服务端出错，请重试。

![image-20201008184820098](https://gitee.com/fkso/blogpics/raw/master/master/%E5%85%B3%E4%BA%8Egithub%E5%9B%BE%E5%BA%8A%E6%90%AD%E5%BB%BA%E9%97%AE%E9%A2%982.png)

按照网上的教程，改了又改，怎么都不能上传成功。最后去github看，主分支变成了`main`，而不再是`master`。于是把配置中的分支改为了`main`

![](https://gitee.com/fkso/blogpics/raw/master/master/%E5%85%B3%E4%BA%8Egithub%E5%9B%BE%E5%BA%8A%E6%90%AD%E5%BB%BA%E9%97%AE%E9%A2%983.png)

测试了一下，上传成功！

![image-20201008190221582](https://gitee.com/fkso/blogpics/raw/master/master/%E5%85%B3%E4%BA%8Egithub%E5%9B%BE%E5%BA%8A%E6%90%AD%E5%BB%BA%E9%97%AE%E9%A2%984.png)

查了一下原因，原来是BLM的原因，说来实在可笑！

![](https://cdn.jsdelivr.net/gh/zerohk/blogpic@main/%E5%85%B3%E4%BA%8Egithub%E5%9B%BE%E5%BA%8A%E6%90%AD%E5%BB%BA%E9%97%AE%E9%A2%985.png)

这个问题解决了，新的问题随之产生了！发现从picgo自动生成的链接导入typora后，图片加载不出来。直接使用浏览器访问时，出现如下问题：

![](https://cdn.jsdelivr.net/gh/zerohk/blogpic@main/%E5%85%B3%E4%BA%8Egithub%E5%9B%BE%E5%BA%8A%E6%90%AD%E5%BB%BA%E9%97%AE%E9%A2%986.png)

上网查了一下，是github的问题，时墙时不墙。没有什么特别好的方法。所以暂时也只能把图片都同步到vercel了。

**已解决！**

还是`master`的问题。将自定义域名改为`https://cdn.jsdelivr.net/gh/zerohk/blogpic@main`的形式即可

![](https://gitee.com/fkso/blogpics/raw/master/master/%E5%85%B3%E4%BA%8Egithub%E5%9B%BE%E5%BA%8A%E6%90%AD%E5%BB%BA%E9%97%AE%E9%A2%987.png)

相册区能正确显示，浏览器也能正确显示。

![](https://gitee.com/fkso/blogpics/raw/master/master/%E5%85%B3%E4%BA%8Egithub%E5%9B%BE%E5%BA%8A%E6%90%AD%E5%BB%BA%E9%97%AE%E9%A2%988.png)

![](https://cdn.jsdelivr.net/gh/zerohk/blogpic@main/%E5%85%B3%E4%BA%8Egithub%E5%9B%BE%E5%BA%8A%E6%90%AD%E5%BB%BA%E9%97%AE%E9%A2%989.png)

但是github还是时好时坏，无法解决。

------

10-12再次更新。

发现有时候不是网络原因，可能是账号原因，换个账号，换个token又能继续上传了。总之，还是不要滥用为好，毕竟是白嫖。