---
title: vercel部署hexo
tags:
  - github
  - 博客
  - hexo
  - vercel
categories:
  - 教程
keywords:
  - github
  - 博客
  - hexo
  - vercel
description: 阅读全文
top_img: 'https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/vercel_create_blog_top.jpg'
cover: >-
  https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/vercel_blog_create_cover.png
abbrlink: 776259585
date: 2020-10-13 17:58:03
updated:
sticky:
password:
abstract:
message:
wrong_pass_message:
wrong_hash_message:
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

# 第一部分：本地部署

这一步主要参考了[知乎这篇文章](https://zhuanlan.zhihu.com/p/44213627)和[hexo官方文档](https://hexo.io/zh-cn/docs/)

## 1.安装Git

官方地址：https://git-scm.com/download/win

淘宝镜像地址：https://npm.taobao.org/mirrors/git-for-windows/

## 2.安装 Node.js

官方地址：https://nodejs.org/en/download/

淘宝镜像地址：https://npm.taobao.org/mirrors/node

## 3.安装Hexo

前面git和nodejs安装好后，就可以安装hexo了，你可以先创建一个文件夹blog，然后`cd`到这个文件夹下（或者在这个文件夹下直接右键git bash打开）。

输入命令：

```shell
npm install -g hexo-cli
```

至此就全部安装完了。

接下来初始化一下hexo：

```shell
hexo init myblog
```

这个myblog可以自己取什么名字都行，然后：

```shell
cd myblog //进入这个myblog文件夹
npm install
```

新建完成后，指定文件夹目录下有：

- node_modules: 依赖包
- public：存放生成的页面
- scaffolds：生成文章的一些模板
- source：用来存放你的文章
- themes：主题
- ** _config.yml: 博客的配置文件**

继续执行：

```shell
hexo g
hexo server
```

打开hexo的服务，在浏览器输入localhost:4000就可以看到你生成的博客了。使用ctrl+c可以把服务关掉。

本地安装就基本结束了。

# 第二部分：同步静态网页到github

> 注意：这里同步的是利用`hexo g`生成的静态网页文件

## 1.创建仓库

github主页右上角，`New repository`，如果不需要使用githubpage部署的话，名字随便取，如果要使用githubpage部署的话，必须保证仓库名为`github用户名.github.io`。保证仓库为public，创建完成

![image-20201013183848372](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013183848372.png)

![image-20201013184310009](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013184310009.png)

## 2.生成SSH添加到Github

回到你的git bash中，

```shell
git config --global user.name "yourname"
git config --global user.email "youremail"
```

这里的yourname输入你的GitHub用户名，youremail输入你GitHub的邮箱。这样GitHub才能知道你是不是对应它的账户。

可以用以下两条，检查一下你有没有输对

```shell
git config user.name
git config user.email
```

然后创建SSH,一路回车

```shell
ssh-keygen -t rsa -C "youremail"
```

这个时候它会告诉你已经生成了.ssh的文件夹。在你的电脑中找到这个文件夹。

![image-20201013184640451](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013184640451.png)

而后在GitHub的settings中，找到SSH keys的设置选项，点击`New SSH key` 把你的`id_rsa.pub`里面的信息复制进去。

![image-20201013184817623](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013184817623.png)

![image-20201013184921881](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013184921881.png)

![image-20201013185039166](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013185039166.png)

在gitbash中，查看是否成功

```shell
ssh -T git@github.com
```

![image-20201013185216648](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013185216648.png)

> 不成功可能有很多原因，可以百度解决

# 第三部分：部署博客

## 1.将博客部署到github

这一步，我们就可以将hexo和GitHub关联起来，也就是将hexo生成的文章部署到GitHub上，打开站点配置文件 `_config.yml`，翻到最后，修改为 YourgithubName就是你的GitHub账户。

```yml
deploy:
  type: git
  repo: https://github.com/YourgithubName/YourgithubName.github.io.git
  branch: master #分支名有可能默认为main
```

这个时候需要先安装deploy-git ，也就是部署的命令,这样你才能用命令部署到GitHub。在`myblog`目录下（以上命令也全是在该目录下，下同）打开gitbash，输入以下命令

```shell
npm install hexo-deployer-git --save
```

然后

```shell
hexo clean #删除public目录
hexo generate #生成静态网页文件
hexo deploy #部署到github
```

注意deploy时可能要你输入username和password。

得到类似的信息说明部署成功：

![image-20201013190148372](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013190148372.png)

如果是用githubpage部署的，这时候访问`http://yourname.github.io`就能打开博客了。

## 2.将博客部署到Vercel

众所周知，GithubPage的访问速度很慢，但是有了Vercel（Zeit）咱就不用担心了。

进入[vercel](https://vercel.com/)，使用邮箱注册或者使用github登录。

进入dashboard，选择`Import Project`

![image-20201013190748764](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013190748764.png)

vercel提供了两种方式导入项目，这里我们选择第一种，直接导入仓库的静态网页文件。第二种是直接导入模板，在vercel服务器上生成网页，大概就是生成速度比较慢吧，但是部署简单。（我也没发现两者太大的区别）。

![image-20201013191045347](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013191045347.png)

接下来，填入你之前生成的仓库地址，可以在github主页找到。形如`https://github.com/zerohk/hexo_blog.git`

![image-20201013191250052](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013191250052.png)

接下来选择root路径，一般就是仓库名。

![image-20201013191720346](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013191720346.png)

projectname就默认，框架就选择other，然后deploy部署

![image-20201013192006781](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013192006781.png)

部署成功就会显示礼花场景，然后会分配一个二级域名，打开就可以访问博客了。

# 第四部分：添加自定义域名

回到dashboard，点击项目

![image-20201013192319324](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013192319324.png)

view domains

![image-20201013192427234](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013192427234.png)

![image-20201013192526447](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013192526447.png)

去域名商那里添加DNS记录即可。

![image-20201013192755615](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013192755615.png)

# 第五部分：发表文章、更改主题

## 1.发布文章更新站点

参考[发布文章指南](https://blog.buercheng.space/posts/1820155650)。都是在本地博客根目录，打开shell或gitbash执行这些命令。

执行`hexo d`到github后，vercel会自动更新部署。基本上，上传到github后，vercel就自动更新网站了。

![image-20201013193433227](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20201013193433227.png)

## 2.更改主题

可以上[hexo官网](https://hexo.io)找到喜欢的主题，按照文档更改