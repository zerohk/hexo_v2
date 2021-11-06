---
title: MySQL基础知识
tags:
  - MySQL
  - java基础
  - 数据库基础
  - java笔记
categories:
  - [java]
  - [数据库]
  - [笔记]
top_img: https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/2640443603_top.jpg
cover: https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/2640443603_cover.jpg
abbrlink: 2640443603
date: 2020-10-12 01:12:25
updated: "`r format(Sys.time(), '%d %B, %Y')`"
sticky:
password:
abstract:
message:
wrong_pass_message:
wrong_hash_message:
keywords:
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

# 数据库的安装、卸载

# 数据库的启动与登录

## 启动

### 通过服务启动MySQL服务。

1、可以通过右键计算机--->管理--->服务和应用程序--->服务，找到MySQL服务启动。

2、可以通过win+R，输入services.msc快捷进入服务页面。

可以将MySQL服务设置为自动启动，就不再需要手动开启了。

### 通过控制台启动MySQL服务

以管理员模式打开控制台。
> 1、win10系统，按住win+x，选择图示选项即可快速以管理员模式打开powershell；
>
> ![win+X](https://cdn.jsdelivr.net/gh/bu2cheng/picpic/1.png)
>
> 2、如果习惯了win+R的方式，可以添加新的命令进去以管理员模式打开cmd控制台，具体方法如下：
>
>   - 在 `%windir%\system32\`目录下，找到cmd，添加快捷方式到`C:\Windows`目录下，为避免冲突给这个快捷方式起一个别名；
>
> 	![image-20210422230828986](https://cdn.jsdelivr.net/gh/bu2cheng/picpic/image-20210422230828986.png)
>
> 	![image-20210422231028599](https://cdn.jsdelivr.net/gh/bu2cheng/picpic/image-20210422231028599.png)
>
> - 右键双击此快捷方式-->快捷方式-->高级-->勾选以管理员方式运行
>
> 	![image-20210422231256468](https://cdn.jsdelivr.net/gh/bu2cheng/picpic/image-20210422231256468.png)
>
> - 使用win+R，输入之前的别名即可以管理员方式打开cmd。



`net start mysql`:启动MySQL服务。

`net stop mysql`:关闭MySQL服务。

## 登录

### 本地数据库登录

1、`mysql -u用户名 -p密码`

2、`mysql -u用户名 -p`:回车后要求输入密码

3、`mysql -h localhost -P 端口号 -u root -p[密码/回车]`:以本地服务器的方式登录数据库

> 注意：`-h、-P、-u`后面的空格可有可无，`-p`后面如果直接跟密码则不能有空格

### 远程数据库登录

1、`mysql -h远程数据库地址 -u用户名 -p密码 `

2、`mysql -h远程数据库地址 -u用户名 -p`

3、`mysql --host=远程数据库地址 --user=用户名 --password=密码`

4、`mysql --host=远程数据库地址 --user=用户名 --password`

### 数据库退出
- `exit`
- `Ctrl+c`

# 数据库的目录结构

![image-20200921211212387](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200921211212387.png)

`bin`：执行文件

`data`：用于放置一些日志文件以及数据库

`include`：用于放置一些头文件

`lib`:用于放置一系列库文件

`share`:用于存放字符集、语言等信息

`my.ini`:配置文件

# SQL语言

## 定义

Structured Query Language：结构化查询语言
	其实就是定义了操作所有关系型数据库的规则。每一种数据库操作的方式存在不一样的地方，称为“方言”。

## 通用语法

1. SQL 语句可以单行或多行书写，以分号结尾。

2. 可使用空格和缩进来增强语句的可读性。

3. MySQL 数据库的 SQL 语句不区分大小写，关键字建议使用大写。

4. 3 种注释

  * 单行注释: -- 注释内容（注意--后面的空格） 或 # 注释内容(mysql 特有) 
  * 多行注释: /* 注释 */（与java多行注释相似）

  

## 分类

1) DDL(Data Definition Language)数据定义语言
		用来定义数据库对象：**数据库，表，列**等。关键字：create, drop,alter 等
2) DML(Data Manipulation Language)数据操作语言
		用来对数据库中表的**数据**进行**增删改**。关键字：insert, delete, update 等
3) DQL(Data Query Language)数据查询语言
		用来**查询**数据库中表的**记录(数据)**。关键字：select, where 等
4) DCL(Data Control Language)数据控制语言(了解)
		用来定义数据库的**访问权限和安全级别，及创建用户**。关键字：GRANT， REVOKE 等

# DDL：操作数据库、表

## 操作数据库：

### CRUD语句

CRUD定义：

- C(Create):创建
- R(Retrieve)：查询
- U(Update):修改
- D(Delete):删除

------

#### Create语句：

```mssql
create database 数据库名;    -- 创建数据库
```

![image-20200922003534168](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922003534168.png)

新创建的数据库与已知数据库重名时：

![image-20200922003651221](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922003651221.png)

可以使用以下语句避免错误出现：

```mysql
create database if not exists  数据库名;
```

![image-20200922004033053](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922004033053.png)

![image-20200922004149497](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922004149497.png)

```mysql
create database 数据库名 character set 字符集名称;    -- 创建数据库并指定字符集
```

![image-20200922004608579](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922004608579.png)

创建数据库db4，判断是否重名，并指定字符集为gbk:

```mysql
create database if not exists db4 character set gbk;
```

![image-20200922004943303](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922004943303.png)

#### Retrieve语句：

```mysql
show databases;     -- 查询所有已创建的数据库
```

```mysql
select database();     -- 查询当前所使用的数据库
```

![image-20200922001542219](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922001542219.png)

> 在MySQL数据库的数据目录下（win7：`C:\ProgramData\MySQL\MySQL Server 5.5\data`）有三个文件夹，就是MySQL自带的数据库。
>
> ![image-20200922001933690](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922001933690.png)
>
> **`information_schema`**：视图，并不是真正的数据库。它提供了访问数据库元数据的方式。没有在data目录下。
>
> **`mysql库`**：这个是mysql的核心数据库，主要负责存储数据库的用户、权限设置、关键字等mysql自己需要使用的控制和管理信息。**不可以删除**。
>
> **`performance_schema`**：对性能提升进行操作的数据库。**尽量别动**
>
> **`test`**:测试数据库。

```mysql
show create database 数据库名;    -- 查看某个数据库字符集的名称（安装时默认utf-8)、查看某个数据库的创建语句
```

![image-20200922003250158](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922003250158.png)



#### Update语句：

```mysql
alter database 数据库名 character set 字符集;    -- 更改指定数据库的字符集
```

![image-20200922005857294](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922005857294.png)

#### Delete语句：

```mysql
drop database 数据库名;    -- 删除指定数据库，删除不存在的数据库会报错
```

![image-20200922010138546](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922010138546.png)

```mysql
drop database if exists 数据库名;    -- 如果存在则删除
```

![image-20200922010340797](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922010340797.png)

### 使用数据库的语句

```mysql
select database();     -- 查询当前使用的数据库
```

![image-20200922010702349](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922010702349.png)

返回NULL，当前未使用任何数据库；

```mysql
use 数据库名称;    -- 使用指定数据库
```

![image-20200922010821110](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922010821110.png)

## 操作数据库的表：

### Create：

```mysql
create 表名(
	列名1 数据类型1,
	列名2 数据类型2,
	...
	列名n 数据类型n
);
```

> #### MySQL常见数据类型：
>
> - int：整数类型    `age int,`
> - double:小数类型   `score  double(int digits1，int digits2),`digits1：位数，digits2：保留小数点后位数
> - date:日期，只包含年月日，格式：`yyyy-MM-dd`
> - datetime:日期，包含年月日时分秒，格式：`yyyy-MM-dd HH:mm:ss`
> - timestamp:时间戳日期，包含年月日时分秒，不赋值或赋值为NULL时，自动为其赋值为当前系统时间。
> - varchar:字符串，`name varchar(int length)`length:最多能容纳的字符数。name  varchar(20)名字最多容纳20个字符张三：两个字符------zhangsan：八个字符

在数据库db1中创建一个学生表：

```mysql
create table Student(
				id int, -- 编号
				name varchar(20), -- 名字
				age int,  -- 年龄
				birthday date,   -- 出生日期
				score double(4,1),   -- 分数
				createTime timestamp  -- 创建时间
				);
```

​		![image-20200922022121545](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922022121545.png)

![image-20200922022147065](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922022147065.png)

```mysql
create table 新的表名 like 已存在的表名;  -- 复制表
```

![image-20200922022528398](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922022528398.png)

![image-20200922022609381](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922022609381.png)

### Retrieve：

```mysql
show tables;    -- 查询正在使用的数据库中的所有表
```

```mysql
show tables from 数据库名;    -- 查询正在特定的数据库中的所有表，如果当前使用的是另一个数据库，执行命令后仍在此数据库，而不会切换到该特定数据库
```

用use命令切换到mysql：

![image-20200922011712171](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922011712171.png)



```mysql
desc 表名称;   -- desc:description ,查询表结构
```

![image-20200922011913444](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922011913444.png)

```mysql
show create table 表名;   -- 展示表的字符集
```

![image-20200922023238467](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922023238467.png)

### Update：

```mysql
alter table 表名 rename to 新的表名;    -- 修改表名
```

![image-20200922023028607](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922023028607.png)

```mysql
alter table 表名 character set 字符集名;
```

![image-20200922023457614](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922023457614.png)

```mysql
alter table 表名 add 列名 数据类型;  -- 给表添加一列
```

![image-20200922023844489](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922023844489.png)

```mysql
alter table 表名 change 列名 新的列名 新的数据类型; -- 修改表的列名及数据类型
```

![image-20200922024110363](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922024110363.png)

```mysql
alter table 表名 modify 列名 新数据类型;  -- 修改列的数据类型
```

![image-20200922024259774](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922024259774.png)

```mysql
alter table 表名 drop 列名;   -- 删除列
```

![image-20200922024440724](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922024440724.png)

### Delete：

```mysql
drop table 表名;
```

```mysql
drop table if exists 表名;
```

![image-20200922022657901](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922022657901.png)

# DML:操作数据库中表的记录

重点掌握。包括添加数据，删除数据，修改数据。

## 添加数据

```mysql
insert into 表名(列名1,列名2,...,列名n) values(值1,值2,...,值n);
```

![image-20200922160000237](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922160000237.png)

查询表中记录(DQL语句):

![image-20200922160545422](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922160545422.png)

注意事项：

1、列名和值要一 一对应（数据类型和个数都要一致）；

2、如果表名后不定义列名，则默认给所有列添加值（不想添加值的value可以用NULL表示）

```mysql
insert into 表名 values(值1,值2,...,值n);
```

![image-20200922161232693](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922161232693.png)

3、除了数字，其他类型都需要用引号（单双引号皆可）括起来。

## 删除数据

```mysql
delete form 表名 [where 条件];    -- []中是可选的
```

![image-20200922162308779](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922162308779.png)

![image-20200922162401069](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922162401069.png)

不加条件时，默认删除表中所有记录。不推荐使用，因为表中有多少条记录，就会执行多少次删除操作，效率较低。

推荐使用以下语句，删除全部记录，效率比较高：

```mysql
truncate table 表名;    -- 先删除表，再创建一个一模一样的表
```

![image-20200922162737278](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922162737278.png)

## 修改数据

```mysql
update 表名 set 列名1=值1,列名2=值2,...[where 条件];
```

![image-20200922164110490](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922164110490.png)

![image-20200922164237142](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922164237142.png)

如果不加任何条件，则会将表中所有记录全部修改。

# DQL：数据查询

最重要的内容。

```mysql
select
		字段列表
from
		表名列表
where
		条件列表
group by
		分组字段
having
		分组之后的条件
order by
		按【】排序
limit
		分页限定
```



## 基础查询

```mysql
select * from 表名;  -- 查询表中所有记录
```

### 多字段查询

```mysql
select 列名1,列名2,... from 表名; -- 多字段查询
```

### 查询细节
添加着重号可区分关键字和字段。
比方说，`myemployees`表中有个字段为`name`,如果不添加着重号，查询时会把`name`当作关键字，使得查询出错：
![](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/%E6%89%B9%E6%B3%A8%202021-04-24%20002627.jpg)
给`name`字段加上着重号，可以避免查询出错：
![](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/%E6%89%B9%E6%B3%A8%202021-04-24%20003028.jpg)

#### 代码演示：

1.创建一个表student：

```mysql
CREATE TABLE student( 
		id int, -- 编号 
		name varchar(20), -- 姓名 
		age int, -- 年龄 
		sex varchar(5), -- 性别 
		address varchar(100), -- 地址 
		math int, -- 数学 
		english int -- 英语 
); 
INSERT INTO 
	student(id,NAME,age,sex,address,math,english) 
VALUES 
	(1,'马云',55,'男','杭州',66,78),
	(2,'马化腾',45,'女','深圳',98,87),
	(3,'马景涛',55,'男','香港',56,77),
	(4,'柳岩',20,'女','湖南',76,65),
	(5,'柳青',20,'男','湖南',86,NULL),
	(6,'刘德华',57,'男','香港',99,99),
	(7,'马德',22,'女','香港',99,99),
	(8,'德玛西亚',18,'男','南京',56,65);
```

![image-20200922173407504](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922173407504.png)

2.从student表中查询姓名，math，和English

```mysql
select name,math,english from student;
```

![image-20200922173618963](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922173618963.png)

### 去重查询



```mysql
select address from student;
```

使用该语句查询时，会出现重复的项目：

![image-20200922173926807](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922173926807.png)

可以使用关键字 `distinct`去重查询：

```mysql
select distinct address from student;
```

![image-20200922174106138](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922174106138.png)

只有查询出的结果完全一致时才会去重，比如以下代码：

```mysql
select distinct name,address from student;
```

![image-20200922174229579](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922174229579.png)

因为姓名有一致的，即使地址重复了，且使用了地distinct关键字也不会将重复地址筛选掉。

### 计算列

 一般可以使用四则运算计算一些列的值。（一般只会进行数值型的计算）

#### 代码演示

```mysql
select name,math,english,math+english from student; -- 查询名字，数学成绩，英语成绩并计算总成绩
```

![image-20200922174559726](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922174559726.png)

#### ifnull(exp1,exp2)函数

从上述操作中可以发现，当查询的值中存在NULL时，进行四则运算后得到的值也会是NULL。为了避免出现这种问题，我们可以使用`ifnull`函数来进行处理。

```mysql
ifnull(exp1,exp2)   -- exp1表示可能为null的值，exp2表示将NULL替换掉的值
```

因此上述计算总分的查询语句可以改为：

```mysql
select name,math,english,math+ifnull(english,0) from student; -- 为NULL时就将值用0替换
```

![image-20200922175500877](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922175500877.png)

### 起别名

从上述查询我们发现列`math+ifnull(english,0)`在结果中不好看，所以我们可以对其设置别名，当然任意列都可以设置别名。

```mysql
列名 as 别名 -- 使用关键字as对列名设置别名
```

**别名的好处**：
- 便于理解
- 如果要查询的字段存在重复名称时，使用别名可以区分开来

#### 代码演示

```mysql
select name,math,english,math+ifnull(english,0) as 总分 from student;
```

![image-20200922180001216](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922180001216.png)

```mysql
select name as 姓名,math as 数学,english as 英语,math+ifnull(english,0) as 总分 from student;
```

![image-20200922180146752](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922180146752.png)

#### 起别名简化形式

```mysql
select 列名1 别名1,列名2 别名2,... from 表名;
```

```mysql
select name,math 数学,english 英语,math+ifnull(english,0) 总分 from student;
```

![image-20200922180414253](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922180414253.png)

> 当别名中存在关键字时，可以将别名用引号（单双皆可）包括起来。

## 条件查询

where子句后加条件。

### 运算符

| 比较运算符          | 备注                                               |
| ------------------- | -------------------------------------------------- |
| >、<、=、>=、<=、<> | <>在SQL中表示不等于，在mysql中也可以使用!=没有==   |
| BETWEEN...AND...    | 在一个范围之内，包头又包尾                         |
| IN(集合)            | 集合表示多个值，各个值之间用逗号隔开               |
| LIKE '张%'          | 模糊查询                                           |
| IS [NOT] NULL       | 查询某一列为[NOT]NULL的值，注：不能写=NULL(!=NULL) |

| 逻辑运算符 | 备注                                |
| ---------- | ----------------------------------- |
| &&或 AND   | 与，SQL中建议使用AND，&&并不通用。  |
| \|\| 或 OR | 或，SQL中建议使用OR，\|\|并不通用。 |
| ! 或 NOT   | 非，SQL中建议使用NOT，!并不通用。   |

> 注：null不能用`=、>、<`等符号来进行判断。判断一个字段是否为null，除了使用IS NULL之外，还可以使用安全等于：`<=>`。此外安全等于也可以用于判断非NULL的字段是否相等。
> ![使用IS NULL判断字段是否为NULL](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/%E6%89%B9%E6%B3%A8%202021-04-24%20230952.jpg)
> ![使用安全等于判断字段是否为NULL](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/%E6%89%B9%E6%B3%A8%202021-04-24%20231157.jpg)
> ![使用=查询字段是否满足](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/%E6%89%B9%E6%B3%A8%202021-04-24%20231520.jpg)
> ![使用安全等于](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/%E6%89%B9%E6%B3%A8%202021-04-24%20231625.jpg)


### 代码演示

1.查询math大于80的人

```mysql
select * from student where math > 80;
```

![image-20200922222724078](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922222724078.png)

查询English小于90的人

```mysql
select * from student where english < 90;
```

![image-20200922222757117](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922222757117.png)

查询sex等于女的人

```mysql
select * from student where sex = '女';
```

![image-20200922222936439](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922222936439.png)

2、查询年龄位于18-30（包含两头）之间的人

```mysql
-- 以下查询效果一致
select * from student where age >= 18 && age <= 30;
select * from student where age >= 18 AND age <= 30; -- 推荐使用AND,不推荐&&
select * from student where age BETWEEN 18 AND 30;
```

![image-20200922223444233](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922223444233.png)

![image-20200922223514518](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922223514518.png)

![image-20200922223625776](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922223625776.png)

3.查询英语成绩为空的人

```mysql
select * from student where english IS NULL;
```

![image-20200922223931763](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922223931763.png)

4.查询英语成绩不为空的人

```mysql
select * from student where english IS NOT NULL;
```

![image-20200922224126958](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922224126958.png)

5.查询年龄为18，22，50的人

```mysql
-- 以下查询结果一致
select * from student where age IN(18,22,50);
select * from student where age = 18 OR age = 22 OR age = 50;-- 推荐使用OR，不推荐||
select * from student where age = 18 || age = 22 || age = 50;

```

![image-20200922224250640](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922224250640.png)

![image-20200922224557584](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922224557584.png)

![image-20200922224637532](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922224637532.png)

### 模糊查询

MySQL通配符：_:匹配单个任意字符；%:匹配任意多个字符。

查询姓马的有哪些人

```mysql
select * from student where name LIKE '马%';
```

![image-20200922230728661](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922230728661.png)

查询姓名第二个字为化的人

```mysql
select * from student where name LIKE '_化%';
```

![image-20200922230954627](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922230954627.png)

查询名字包含德字的人

```mysql
select * from student where name LIKE '%德%';
```

![image-20200922231144759](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922231144759.png)

查询名字是三个字的人

```mysql
select * from student where name LIKE '___';
```

![image-20200922231318145](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200922231318145.png)


#### 使用转义字符

如果想要查询结果中包含`_、%`的字段可以使用转义字符
- 使用`\`来转义
- 使用`escape`关键字来定义任意符号为转义字符

```mysql
#查询员工中，名字第二个字为_的员工信息
SELECT 
  * 
FROM
  employees 
WHERE last_name LIKE '_\_' ; #用\将_转义，不再作为通配字符
```

```mysql
SELECT 
  * 
FROM
  employees 
WHERE last_name LIKE '_$_' ESCAPE '$' ; # 使用ESCAPE关键字将$设置为转义字符，$将_转义，不再作为通配字符

SELECT 
  * 
FROM
  employees 
WHERE last_name LIKE '_a_' ESCAPE 'a' ; # 使用ESCAPE关键字将a设置为转义字符，a将_转义，不再作为通配字符
```


# 表的约束

## 外键约束

涉及多张表的操作。

数据有冗余的时候，进行表的拆分，然后利用外键对拆分的表进行关联。

### 添加外键

1.在创建表时添加外键约束

```mysql
create table 表名(
	...
    外键列：外键列名称 数据类型,
    constraint 外键名称 foreign key (外键列名称) references 主键表名(主键列名称),
    ...
);
```

其中，外键名称可以任意取，主键表名，即为关联的表名。

2.在表创建完成之后添加外键

```mysql
alter table 表名 add constraint 外键名 foreign key(外键列名) references 主表名(主键列名);
```



#### 代码演示

```mysql
-- 创建一个部门表，作为主表，因为副表需要引用他，所以需要先创建
CREATE TABLE department(
	dep_id INT INT PRIMARY KEY AUTO_INCREMENT,
	dep VARCHAR(20),
	dep_loacation VARCHAR(20)
);
-- 向表中添加两个部门
INSERT INTO department VALUES(NULL, '研发部','广州'),(NULL, '销售部', '深圳');
```

![image-20200926164650983](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200926164650983.png)

```mysql
-- 创建员工表，利用外键和部门表产生关联
CREATE TABLE employee(
	id INT PRIMARY KEY AUTO_INCREMENT,
	NAME VARCHAR(20),
	age INT,
	dep_id INT,  -- 外键列，与主表主键列类型要一致
	CONSTRAINT emp_dep_id FOREIGN KEY(dep_id) REFERENCES department(dep_id)
);
-- 添加员工信息
INSERT INTO employee (NAME, age, dep_id) VALUES 
('张三', 20, 1),
('李四', 21, 1),
('王五', 20, 1),
('老王', 20, 2),
('大王', 22, 2),
('小王', 18, 2);
```

![image-20200926165713224](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200926165713224.png)

添加约束后，主键的列不能被删除，因为和从表产生了关联

![image-20200926165821510](https://cdn.jsdelivr.net/gh/bu2cheng/picpic@master/blogimg/image-20200926165821510.png)

### 删除外键

```mysql
alter table 表名 drop foreign key 外键名称;
```

## 级联操作

添加级联操作时需要谨慎对待。在添加外键约束的语句中添加相应的语法，以便主表改变时，从表发生相应变化。级联操作有两种：级联更新和级联删除。级联更新：主表的主键发生变化时，从表的外键也会发生相应变化。级联删除：主表删除主键列的数据时，相应的从表的外键列会被全部删除。因此添加级联操作时要慎之又慎。

### 级联更新

在添加外键约束的语句中添加相应的语法。

```mysql
on update cascade
```

1.创建表时添加级联更新

```mysql
create table 表名(
	...
    外键列：外键列名 数据类型,
    constraint 外键名称 foreign key(外键列名) references 主表名(主键名) on update cascade,
    ...
);
```

2.创建完表后添加级联更新

```mysql
alter table 表名 add constraint 外键名称 foreign key(外键列名) refereces 主表名(主键列名) on update cascade;
```

3.删除级联更新

```mysql
alter table 表名 drop foreign key  外键名称;
```

### 级联删除

```mysql
on delete cascade
```

1.创建表时添加

```mysql
create table 表名(
	...
    外键列：外键列名 数据类型,
    constraint 外键名称 foreign key(外键列名) references 主表名(主键名) on delete cascade,
    ...
);
```

2.创建完表后添加级联更新

```mysql
alter table 表名 add constraint 外键名称 foreign key(外键列名) refereces 主表名(主键列名) on delete cascade;
```

3.删除级联更新

```mysql
alter table 表名 drop foreign key  外键名称;
```

### 同时添加两种级联操作

```mysql
create table 表名(
	...
    外键列：外键列名 数据类型,
    constraint 外键名称 foreign key(外键列名) references 主表名(主键名)on update cascade on delete cascade,
    ...
);
```





