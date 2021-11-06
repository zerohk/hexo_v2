---
title: MySQL常用函数
updated: '`r format(Sys.time(), ''%d %B, %Y'')`'
tags:
  - MySQL
  - 数据库基础
categories:
  - 数据库
top_img: 'https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/mysql_function_top1.jpg'
cover: 'https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/mysql_function_cover.jpg'
abbrlink: 1865743498
date: 2021-04-26 23:05:08
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

# 字符函数

## length计算长度

### 定义和使用

`LENGTH()`方法返回字符串的长度，以字节为单位。

### 语法

```
LENGTH(string)
```

### 参数

`string`：必选。需要计算字节长度的字符串。

### 代码演示

```mysql
# 查询系统使用的字符集。在ascll编码中，汉字占两个字节；在utf-8中，汉字占三个字节；在utf-16中汉字占两个字节。
SHOW VARIABLES LIKE '%char%';
```

![image-20210426214822430](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426214822430.png)

```mysql
SELECT LENGTH("中国");
```

![image-20210426214957079](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426214957079.png)

## substr截取子串

### 定义和使用

substring()方法从一个字符串中提取子串（从任意位置开始）

### 语法

```mysql
substring(string,start,length)
```

或者

```mysql
substring(string FROM start FOR length)
```

### 参数

`string`：必选。需要提取子串的字符串。

`start`：必选。**不能为0**，可以是负数，可以是正数。如果为正数，则从开头开始（数start位）提取；为负数则从末尾开始。

`length`：可选。如果为空，则默认提取start开始后的所有字符。

### 代码演示

```mysql
SELECT SUBSTRING("I love China",3,10);
```

![image-20210425170534410](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210425170534410.png)

```mysql
SELECT SUBSTRING("I love China" FROM 3 FOR 10);
```

![image-20210425204219329](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210425204219329.png)

```mysql
SELECT SUBSTRING("I love China",-1,10); # 从-1位也就是倒数第一位开始数10位，这时候已到末尾，因此只有倒数第一位a
```

![image-20210425205203224](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210425205203224.png)

```mysql
SELECT SUBSTRING("I love China" FROM -10 FOR 10);
```

![image-20210425205848706](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210425205848706.png)

### 相同的函数

`SUBSTR()`和`MID()`函数的功能与`SUBSTRING()`是一样的。

`SUBSTR()、MID()`与`SUBSTRING()`的用法完全一致。

```mysql
SUBSTR(str,start,length)
MID(str,start,length)
```

或者

```mysql
SUBSTR(str FROM start FOR length)
MID(str FROM start FOR length)
```

## upper将字符串转为大写形式

### 定义和使用

`UPPER()`函数将一个字符串转为大写形式。

### 语法

```mysql
UPPER(text)
```

### 参数

`text`:必选。需要转换的字符串。

### 代码演示

```mysql
SELECT UPPER("aBcdEFGHijklmnopqRsTUvwXyz");
```

![image-20210425211713047](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210425211713047.png)

### 相同的函数

`UCASE()`函数的用法与`UPPER()`函数一致。

## lower将字符串转为小写形式

参见`UPPER()`函数。

`LCASE()`函数与`LOWER()`函数的功能和使用一致。

```mysql
SELECT LOWER(first_name) FROM employees;
SELECT first_name FROM employees;
```

![image-20210425212516339](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210425212516339.png)

![image-20210425212533559](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210425212533559.png)

## trim去除前后指定的空格或字符

### 定义和使用

`TRIM()`可以去除字符串中前导和结尾的空格或指定字符。

### 语法

`TRIM([{BOTH|LEADING|TRAILING} [removed_string] FROM] string)`

### 参数

`BOTH|LEADING|TRAILING`：都是可选的。缺省为BOTH，即首尾皆删除。LEADING表示删除指定前导字符或是前导空格；TRAILING表示删除指定后缀字符或是后缀空格。

`removed_string:`可选。缺省为空格。表示需要删除的前导、后缀字符。

`TRIM(string)`：删除string前后的空格，并返回去掉空格后的字符串。string也可以是字段。

### 代码演示

```mysql
SELECT TRIM("   I love China   ");
```

![image-20210425215829308](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210425215829308.png)

```mysql
SELECT TRIM('_' FROM "__I am here    __");
```

![image-20210425220028451](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210425220028451.png)

```mysql
SELECT TRIM(LEADING '&' FROM "&&&&&&&&I am here&&&&");
```

![image-20210425220150837](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210425220150837.png)

## ltrim、rtrim分别去掉前导和后缀空格

如果只需要去掉空格可以使用`LTRIM()`和`RTRIM()`函数

## replace替换字符

### 定义和使用

`REPLACE()`函数可以使用一个新的字符串代替某字符串中出现的所有指定的子串。

> 注意，该函数大小写敏感。

### 语法

```mysql
REPLACE(String,from_string,to_string); # String 也可以是字段
```

### 参数

`String`：必选。原始字符串。

`from_string`：必选。需要替换的子串。

`to_string`：必选。替换串。

### 代码演示

```mysql
SELECT REPLACE("something,someone,somebody,somewhere,sometime","some","any");
```

![image-20210426085053656](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426085053656.png)

## lpad左填充、rpad右填充

### 定义和使用

`LPAD()`:用一个指定的字符串左填充给定字符串，扩充字符串到指定长度。

`RPAD()`：用一个指定的字符串右填充给定字符串，扩充字符串到指定长度。

### 语法

```mysql
LPAD(string,length,lpad_string);
RPAD(string,length,rpad_string);
```

### 参数

`string`:必选。待填充的字符串。

`length`:必选。需要扩充到的长度。包括原始字符串的长度。

`lpad_string`:必选。用来填充的字符串。

`rpad_string`:必选。用来填充的字符串。

### 代码演示

```mysql
SELECT LPAD(first_name,20,"#@*") FROM employees;
```

![image-20210426095216847](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426095216847.png)

```mysql
SELECT RPAD(LPAD('a',10,'l'),21,'r');
```

![image-20210426095452986](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426095452986.png)

```mysql
SELECT LPAD("aaaaa",2,'b');# 指定的长度小于原字符串的长度，字符串会被截断
```

![image-20210426220357465](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426220357465.png)

## instr返回子串第一次出现的索引

### 定义和使用

`instr()`：返回某一字符串在另一字符串中第一次出现的位置。

### 语法

```mysql
instr(string1,substring)
```

### 参数

`string`:必选。待查字符串。

`substring`:必选。需要在`string`中查找的子串。

返回值：`substring`在`string`中首次出现的位置。如果没有找到，则返回0。

### 代码演示

```mysql
SELECT INSTR("abcabcdefacddefddf","ddf");
```

![image-20210426100810456](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426100810456.png)

```mysql
SELECT INSTR("abcd",'e');
```

![image-20210426100929159](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426100929159.png)



## 其他函数

`CURRENT_DATE()`:返回年月日。

`CURRENT_TIME()`:返回时分秒。

`CURRENT_TIMESTAMP()`:返回当前时间。包括年月日时分秒。

![image-20210426102107190](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426102107190.png)

![image-20210426101642130](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426101642130.png)

![image-20210426101731308](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426101731308.png)

# 数学函数

## ceil向上取整

### 定义和使用

`CEIL()`函数返回大于或等于某数的最小整数。

### 语法

```
CEIL(number)
```

### 参数

`number`:必选。数值型数据。

### 代码演示

```mysql
SELECT CEIL(2);
SELECT CEIL(2.34);
SELECT CEIL(-1.1);
SELECT CEIL(-1);
```

![image-20210426105600331](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426105600331.png)

![image-20210426105637044](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426105637044.png)

![image-20210426110530438](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426110530438.png)

![image-20210426110632052](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426110632052.png)

> `CELING()`函数与`CEIL()`函数功能和使用方法一致。

## floor向下取整

### 定义和使用

`FLOOR()`函数返回小于或等于某数的最大整数。

### 语法

```
FLOOR(number)
```

### 参数

`number`:必选。数值型数据。

### 代码演示

```mysql
SELECT FLOOR(2.5);
SELECT FLOOR(2);
SELECT FLOOR(-3.4);
SELECT FLOOR(-5);
```

![image-20210426112128441](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426112128441.png)

![image-20210426112209061](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426112209061.png)

![image-20210426112302977](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426112302977.png)

![image-20210426112333720](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426112333720.png)

## round四舍五入

### 定义和使用

`ROUND()`函数将数字四舍五入到指定的小数位数。

### 语法

```
ROUND(number,decimals)
```

### 参数

`number`：必选。需要进行舍入的数字。

`decimals`：可选。`number`需要舍入到的小数的位数。缺省时，不保留小数位，返回整数类型。

### 代码演示

```mysql
SELECT ROUND(233.123,2);
SELECT ROUND(233.567,2);
SELECT ROUND(123.4);
SELECT ROUND(123.7);
```

![image-20210426113625956](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426113625956.png)

![image-20210426113746253](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426113746253.png)

![image-20210426113909533](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426113909533.png)

![image-20210426114017392](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426114017392.png)

## truncate截断

### 定义和使用

`TRUNCATE()`函数可以将一个数截断成指定的小数位数。

### 语法

```
TRUCATE(number,decimals)
```

### 参数

`number`:必选。需要截断的数字。

`decimals`：必选。需要截断的小数位数。

### 代码演示

```mysql
SELECT TRUNCATE(123.45678,2);

```

![image-20210426115207539](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426115207539.png)



## 取余函数

### 定义和使用

MOD()函数可以返回一个数除以另一个数的余数。

### 语法

```
MOD(x,y) # x mod y = x- x/y * y
或
x MOD y
或
x % y
```

### 参数

`x`:必选。被除数。

`y`：必选。除数。

### 代码演示

```mysql
SELECT MOD(5,2);
SELECT 5 MOD 2;
SELECT 5 % 2;
```

![image-20210426132851907](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426132851907.png)

![image-20210426133011212](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426133011212.png)

![image-20210426133101551](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426133101551.png)

## rand取随机数

### 定义和使用

`RAND()`函数返回一个0（包含）到1（不包含）的随机数。

### 语法

```
RAND(seed)
```

### 参数

`seed`：可选。表示种子数。如果设定了种子数，则每次生成随机数都是相等的。没有种子数则生成完全随机数。

### 代码演示

```mysql
SELECT RAND();
SELECT RAND()*10; # 生成1（包括）-10（不包括）的随机数
```

![image-20210426134040809](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426134040809.png)

![image-20210426134229398](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426134229398.png)

## 日期函数

- `NOW()`:返回当前日期+时间。与[CURRENTTIMESTAMP()](#其他函数)函数效果一致。

	

	![image-20210426134623494](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426134623494.png)

- `CURDATE()`：返回当前日期。与[CURRENTDATE()](#其他函数)函数效果一致。

![image-20210426135637716](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426135637716.png)

- `CURTIME()`：返回当前时间。与[CURRENTTIME()](#其他函数)效果一致。

![image-20210426135855051](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426135855051.png)

- `YEAR(date)`:返回一个日期中的年份。（从1000-9999）。

	![](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426140713874.png)

	![image-20210426141107826](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426141107826.png)

	![image-20210426141202714](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426141202714.png)

	![image-20210426141635354](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426141635354.png)

	![image-20210426142955892](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426142955892.png)

	- `MONTH(date)`：返回给定日期中的月份(1-12)，用法与`YEAR(date)`一致。

	- `DAY(date)`：返回给定日期中的月份(1-30)，用法与`YEAR(date)`一致。`DAYOFMONTH()`函数与此函数用法和功能一致。

	- `DATE_FORMATE(date,formate)`:将参数日期转化为指定的格式。

		formate可以选如下一种或几种：

		| 格式 |                     描述                      |
		| :--: | :-------------------------------------------: |
		|  %a  |          缩写的星期几（从SUN到SAT）           |
		|  %b  |           缩写的月份名(从Jan到Dec)            |
		|  %c  |             数字化的月份名(0-12)              |
		|  %D  | 当月的第几天，跟上英语序数词后缀(1st,2nd,...) |
		|  %d  |          当月第几天，数字格式(00-31)          |
		|  %e  |          当月第几天，数字格式(0-31)           |
		|  %f  |              微秒(000000-999999)              |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |
		|      |                                               |

	- `STR_TO_DATE(string,formate)`:返回一个基于参数字符串和格式的日期。

	- `MONTHNAME(date)`：返回一个日期中的月份的完整英文名称。

		![image-20210426145845933](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426145845933.png)

	- `HOUR(date)`:返回一个日期中的小时部分，（0-838）。

	- `MINUTE(date)`:返回一个日期或时间中的分钟部分，（0-59）。

	- `SECOND(date)`:返回一个日期或时间中的秒钟部分，（0-59）。

	- `DATEDIFF(date1,date2)`:返回两个日期之间相隔的天数。(date1-date2)

# 高级函数

1. `version():`返回当前MySQL数据库的版本类型。

	![image-20210426150903933](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426150903933.png)

2. `user()`：返回当前MySQL连接的用户名和主机名。

	![image-20210426151359076](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426151359076.png)

	`SESSION_USER()`和 `SYSTEM_USER() `的功能和效果与该函数一致。

3. `password(string)`:加密字符串。**5.7.5**之后已废弃。

4. ` MD5(string)`:返回md5加密后的字符串。



# 流程控制函数

## if

### 定义和使用

`if()`函数当条件为true时返回一个值，为false时返回另一个值。

### 语法

```
IF(condition,value_if_true,value_if_false)
```

### 参数

`condition`:必选。需要测试的条件。

`value_if_true`:必选。当条件为true时返回的值。

`value_if_false`:必选。当条件为false时返回的值。

### 代码演示

```mysql
SELECT IF(STRCMP("hello","mysql")=0,'true','false'); # 判断两个字符串是否相等。
```

![image-20210426154855550](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426154855550.png)

## case

### 情况一

相当于switch结构。

```
case 变量或表达式或字段
when 常量1 then 值1[或语句;] #表达式不需要分号，语句的话需要分号
when 常量2 then 值2[或语句;]
...
else 值n # 相当于default
end
```

#### 案例分析

> 查询员工工资，要求
>
> - 部门号=30，显示的工资为原工资1.1倍；
> - 部门号=40，显示的工资为原工资1.2倍；
> - 部门号=50，显示的工资为原工资1.3倍；
> - 其他部门，现实的工资为原工资

```mysql
SELECT salary 原工资,
CASE department_id
WHEN 30 THEN salary * 1.1
WHEN 40 THEN salary * 1.2
WHEN 50 THEN salary * 1.3
ELSE salary
END 显示工资
FROM employees;
```

![image-20210426224856785](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426224856785.png)

### 情况二

相当于if-else结构。

```
case
when 条件1 then 值1[或语句1;] #语句要加分号。
when 条件2 then 值2[或语句2;]
...
else 值n
end
```

#### 案例

> 查询员工工资情况
>
> - 大于20000，显示A级别；
> - 大于15000，显示B级别；
> - 大于10000，显示C级别；
> - 否则，显示D级别。

```mysql
SELECT last_name,salary,
CASE 
WHEN salary > 20000 THEN "A级别"
WHEN salary > 15000 THEN "B级别"
WHEN salary > 10000 THEN "C级别"
ELSE "D级别"
END 工资级别
FROM employees;
```

![image-20210426225839842](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210426225839842.png)