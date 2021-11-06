---
title: WolfRam Language
updated: '`r format(Sys.time(), ''%d %B, %Y'')`'
abbrlink: 1760471615
date: 2021-10-26 22:19:14
sticky:
tags:
categories:
password:
abstract:
message:
wrong_pass_message:
wrong_hash_message:
keywords:
description:
top_img:
comments:
cover:
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

# 1. 基本算术运算

Wolfram Language支持基本的算术运算：+、-、*、/、^。直接输入公式就可以计算了，在电脑上可以使用shift+enter得到结果。

![image-20211017203905618](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262221617.png)

> 注意：
>
> 1. 输入一个数字，然后添加一个空格，再输另外一个数字，可以在两个数字之间添加×号。
>
> 	![动画](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262221392.gif)
>
> 2. 两个整数做除法，不能整除时，会显示分数；如果想要得到小数形式，可以在被除数和除数后面加上小数点。
>
> 	![image-20211017204756827](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262221974.png)
>
> 3. 当0作除数时，会得到无穷大的符号表示。
>
> 	![image-20211017205650653](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262222419.png)

# 2. 函数

当你输入2+2的时候，Wolfram Language会将它理解为Plus[2,2]。Plus就是一个函数。Wolfram Language内建超过了5000个函数。

所有的函数名称都以大写字母开头，用方括号来将参数括起来。

函数举例：

- Plus[]:表示项的和。Plus[]=0;Plus[x]=x.

	![image-20211019195153072](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262222270.png)

- Subtrac[]:表示项的差,Sub[x,y]等价于x+(-1) * y,*x*-*y* 在输入时被转换为 *x*+(-1**y*)。Subtract[]函数必须有两个参数，且只能有两个参数。

	![image-20211019195853954](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262222440.png)

- Times[]:表示项的乘积。Times[]=1;Times[x]=x。

	![image-20211019200214330](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262222611.png)

- Divide[]:表示项的除法，等价于x * y^-1，在输入中x/y被转换成x * y^-1。Divide[]函数必须有两个参数，且只能为两个参数。

	![image-20211019200722426](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262222636.png)

- Power[]:Power[x,y]给出x的y次幂。Power[x,y,z]等价于Power[x,Power[y,z]]。

	![image-20211019201400169](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262222496.png)

- Max[]:Max[x<sub>1</sub>,x<sub>2</sub>,x<sub>3</sub>...]给出x<sub>i</sub>中的最大值；Max[{x<sub>1</sub>,x<sub>2</sub>...},{y<sub>1</sub>}...]给出所有列表中的最大元素。Max[]返回-Infinity。

	![image-20211019202032454](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262222668.png)

- Min[]:Min[x<sub>1</sub>,x<sub>2</sub>,x<sub>3</sub>...]给出x<sub>i</sub>中的最小值；Min[{x<sub>1</sub>,x<sub>2</sub>...},{y<sub>1</sub>}...]给出所有列表中的最小元素。Min[]会给出Infinity。

	![image-20211019202545548](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262222991.png)

- RandomInteger[]:

	- RandomInteger[{i<sub>min</sub>,i<sub>max</sub>}]:给出{i<sub>min</sub>,i<sub>max</sub>}范围内的伪随机整数。
	- RandomInteger[i<sub>max</sub>]：给出{0...i<sub>max</sub>}范围内的伪随机整数。
	- RandomInteger[]:伪随机的给出0或1。
	- RandomInteger[range,n]:给出n个伪随机数组成的列表。随机数大小在0-range之间。
	- RandomInteger[range,{n<sub>1</sub>,n<sub>2</sub>...}]:给出由伪随机整数组成的n<sub>1</sub>×n<sub>2</sub>×...的数组。随机数大小在0-range之间。

	![image-20211019204030191](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262223218.png)

# 3. 列表

List(列表)是Wolfram Language里面用来表示元素集合的基础方式。{1,2,3}是一个数字列表，它本身不能干任何事，只是存储元素的一种方式，当你输入一个列表时，会原样的输出。

![image-20211019205023158](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262223968.png)

- ListPlot[]:用来将数字列表绘制成图像的函数。

	![image-20211019205353209](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262223759.png)

- Range[]:一个可以产生数字列表的函数。

	- Range[i<sub>max</sub>]:生成列表{1,2,...i<sub>max</sub>}。
	- Range[i<sub>min</sub>,i<sub>max</sub>]:生成列表{i<sub>min</sub>...i<sub>max</sub>}。
		- Range[-1,3]:生成列表{-1,0,1,2,3}；
		- Range[2,-2]:生成列表{};
		- Range[2,-2,-1]生成列表{2,1,0,-1,-2};
	- Range[i<sub>min</sub>,i<sub>max</sub>,d]:以步长d生成列表。

	![image-20211019210339879](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262223603.png)

- 生成一个数字列表，然后把它绘制出来：

	![image-20211019210448596](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262223637.png)

- Reverse[]:可以将列表中的元素顺序翻转过来。

	![image-20211019210720859](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262223704.png)

- Join[]:可以将多个列表连接成一个列表。

	![image-20211019211007834](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262223561.png)

> 注意：{a,b,c}和{c,b,a}表示两个不同的列表。

# 4. 展示列表

ListPlot是一种展示或者可视化数字列表的方法。另外还有许多其他方法。

- ListLinePlot[]:可以绘制列表，并把每个点连起来形成折线图。

	![image-20211019212243536](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262223630.png)

- BarChart[]:可以将列表转换成柱状图。

	![image-20211019212550316](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262224589.png)

- PieChart[]：可以将列表转换成饼图。

	![image-20211019212659486](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262224711.png)

- NumberLinePlot[]:在数轴上将列表数字绘制出来。

	![image-20211019213118011](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262224893.png)

- Column[]:将列表元素以垂直方向展示。

	![image-20211019215705890](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262224233.png)

- 列表可以包含任何东西，包括图像。所以你可以把图像组合放到List里面。

	![image-20211019215857868](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262224897.png)



# 5. 对列表的操作

Wolfram Language中有数千种函数可以对列表进行操作。

1. 可以对列表进行算术运算

	- 加法：

		- 列表+数字：直接将列表中每个数字加上该数字，得到新列表。“{}”:没有任何元素的list叫作null list或是empty list。

			![image-20211019220724053](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262224979.png)

		- 列表+列表：列表的长度必须相同，依次将各个同一顺序的元素相加即可。

			![image-20211019220903399](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262225292.png)

	- 减法：与加法一致

		![image-20211019221024380](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262225977.png)

	- 乘法：

		- 列表*数字：各个元素与数字相乘得到新列表。
		- 列表* 列表：相同顺序的元素相乘。

	- 除法：

		- 列表/数字：各个元素除以数字。
		- 列表/列表：相同顺序元素相除。

	- 对列表求方：

		![image-20211019221549242](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262225755.png)

2. 其他函数

	- Sort[]:可以对列表进行排序。

		![image-20211019221754349](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262225545.png)

	- Length[]:返回列表的长度。

	- Total[]：返回列表所有元素相加的和。

	- Count[list,a]:返回元素a在list中出现的次数。

	- First[]：返回列表第一个元素。First[Sort[list]] = Min[list]

	- Last[]：返回列表最后一个元素。

	- Part[list,n]:返回列表特定位置的元素。

	- IntegerDigits[]:可以将数字各个位拆成列表的一个元素。

		![image-20211019222209227](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262225112.png)

	- IntegerDigits[number,base]:IntegerDigits[number]返回的是以10为基数的数字形式，base可以是任意值，返回的就是以base为基数的结果。

	- FromDigits[List[]]:IntegerDigits[]的反函数，返回列表中数字组成的整数。

	- Rest[list]:返回列表中除第一个外所有元素组成的列表。

	- Most[list]:返回列表中除最后一个元素外所有元素组成的列表。

	- Take[list,n]:返回从list第一个元素开始，到第指定个元素的列表。

	- Drop[list,n]:删掉list第一个元素到指定位元素。

# 6. 创建表

我们可以直接使用{a,b,c..}的形式、使用Range函数、IntegerDigits函数来生成列表，但是一个更通用更灵活的方法是使用Table函数。

Table函数最简单的形式是：Table[number,times]:生成一个由times个number组成的列表。

![image-20211026200146422](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262225152.png)

也可以对列表进行重复:Table[list,times]:

![image-20211026200330426](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262225318.png)

当然，可以对任何对象进行重复:

![image-20211026200459300](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262226228.png)

如果想要对不同的元素进行重复应该怎么做？这需要引入另一个变量，然后对该变量进行迭代。

![image-20211026201711178](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262226140.png)

利用Table函数生成前十个数的平方：

![image-20211026201821697](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262226982.png)

Table函数可以使用任何元素：

1. 生成连续长度的列表组成的表

	![image-20211026202103149](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262226840.png)

2. ![image-20211026202311077](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262226134.png)

3. ![image-20211026202411537](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262226833.png)

Table[f[n],{n,3,5}]:表示n从3开始迭代到5：

![image-20211026202815333](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262226273.png)

Table[f[n],{n,4,20,2}]:表示n从4开始以2的步长迭代到20：

![image-20211026202951041](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262227035.png)

Table总是会对输入的列表进行分开计算--在Table函数中使用RandomInteger函数时，可以看到这个过程：

![image-20211026203626394](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262227058.png)

生成了20个不同的伪随机数。

# 7. 颜色和格式

WolfRam Language不仅仅可以处理数字，还可以处理颜色。我们可以使用名字来获得常用颜色。

![image-20211026211855410](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262227038.png)

创建一个颜色列表：

![image-20211026212108391](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262227296.png)

ColorNegate函数可以生成一种颜色的补充色：

![image-20211026212713786](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262227166.png)

Blend函数可以将**列表中**的颜色进行混合：

![image-20211026212838660](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262227292.png)

RGBColor[]函数可以通过指定红色，绿色，蓝色的值，来指定一个颜色，可取的值得范围为0到1.

![image-20211026213126077](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262227245.png)

![image-20211026213606954](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262227437.png)

有时候用hue(色调)来描述颜色，比直接用颜色的名字来描述比较方便。函数Hue就可以达到这个目的。

![image-20211026214002652](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262227934.png)

有时候，只想要一个随机的颜色，RandomColor函数可以做到这一点，该函数不需要任何参数即可执行。

![image-20211026214437390](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262227866.png)

![image-20211026214528761](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262228628.png)

我们可以在任何地方使用颜色。比方，我们可以使用Style函数对输出的数字加上颜色。

![image-20211026214859538](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262228610.png)

我们也可以在Style函数中指定输出的元素的大小：

![image-20211026215245833](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262228992.png)

也可以同时指定元素的颜色和大小：

![image-20211026215759550](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/202110262228642.png)



