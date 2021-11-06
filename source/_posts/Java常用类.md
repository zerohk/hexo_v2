---
title: Java常用类
updated: '`r format(Sys.time(), ''%d %B, %Y'')`'
tags:
  - java笔记
  - java基础
categories:
  - java
  - 笔记
top_img: 'https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/class_top.jpeg'
cover: 'https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/class_cover.jpeg'
abbrlink: 3742615103
date: 2021-03-04 12:06:53
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

# Scanner类

## 功能

可以实现键盘输入数据到程序中。

### 引用类型的一般使用步骤：

#### 1、导包：

​	`import 包路径.类名称`

​	如果需要使用的目标类和当前类位于同一个包，则可以省略导包语句。只有java.lang包下的内容不需要导包，其他的包都需要import语句

#### 2、创建：

​	`类名称 对象名 = new 类名称(参数列表);`

#### 3、使用：

​	对象名.成员方法名()

## 使用

- 导包：`import java.util.Scanner`

- 构造方法：`Scanner sc = new Scanner(System.in);//没有无参构造，参数System.in表示从键盘读取输入`

- 成员方法：
	- `sc.nextInt();//读入键盘输入的整数值`
	- `sc.next();//读入键盘输入的字符串`

## 代码演示

### 1.求和

> 键盘录入两个数据并求和

```java
package cn.shenzc.java;
import java.util.Scanner;
public class ScannerSum {
    public static void main(String[] args) {
        System.out.println("请输入第一个整数：");
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        System.out.println("请输入第二个整数：");
        int b = sc.nextInt();
        int sum = a + b;
        System.out.println(a + "+" + b + "的和是：" + sum);
    }
}
```

![image-20210301224741217](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210301224741217.png)

### 2.求三个数中最大值

> 键盘录入三个数据并获取最大值

```java
package cn.shenzc.java;

import java.util.Scanner;

public class MaxInThree {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入第一个数：");
        int a = sc.nextInt();
        System.out.println("请输入第二个数：");
        int b = sc.nextInt();
        System.out.println("请输入第三个数：");
        int c = sc.nextInt();
        int max = (a > b) ? a : b;
        max = (max > c) ? max : c;
        System.out.println("最大值是:" + max);
    }
}
```

![image-20210301224959292](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210301224959292.png)

# 匿名对象

## 概念

创建对象时，只有创建对象的语句，却没有把对象地址值赋值给某个变量。虽然是创建对象的简化写法，但是应用
场景非常有限。

## 格式

```java
new 类名(参数列表);
```

比如：`new Scanner(System.in);`

## 应用场景

1. 创建匿名对象直接调用方法，没有变量名。

	```java
	new Scanner(System.in).nextInt();
	```

2. 一旦调用两次方法，就是创建了两个对象，造成浪费，请看如下代码。

	```java
	new Scanner(System.in).nextInt();
	new Scanner(System.in).nextInt();
	```

	> 一个匿名对象，只能使用一次。

3. 匿名对象可以作为方法的参数和返回值。

	- 作为参数

		```java
		class Test {
		public static void main(String[] args) {
		// 普通方式
		Scanner sc = new Scanner(System.in);
		input(sc);
		//匿名对象作为方法接收的参数
		input(new Scanner(System.in));
		}
		public static void input(Scanner sc){
		System.out.println(sc);
		}
		}
		```

		![image-20210301230616695](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210301230616695.png)

	- 作为返回值

		```java
		class Test2 {
		public static void main(String[] args) {
		// 普通方式
		Scanner sc = getScanner();
		}
		public static Scanner getScanner(){
		//普通方式
		//Scanner sc = new Scanner(System.in);
		//return sc;
		//匿名对象作为方法返回值
		return new Scanner(System.in);
		}
		}
		```

		![image-20210301231514922](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210301231514922.png)

	

# Random类

## 功能

此类的实例用于生成伪随机数。

## 使用

- 导包：`import java.util.Random`

- 构造方法：

	- `public Random()`:

	- `public Random(long seed)`:同一种子生成随机数是一样的

- 成员方法：

	- `public int nextInt()`:返回伪随机整数。
	- `public int nextInt(int n)`:返回一个伪随机数，范围在0（包括）和指定值n（不包括）之间的
		int 值。

## 代码演示

### 1.生成三个十以内的整数

```java
package cn.shenzc.java;

import java.util.Random;

public class TestRandom2 {
    public static void main(String[] args) {
        Random random = new Random();
//        System.out.println("第一个十以内随机整数" + random.nextInt(10)) ;
//        System.out.println("第二个十以内随机整数" + random.nextInt(10)) ;
//        System.out.println("第三个十以内随机整数" + random.nextInt(10)) ;
        for(int i = 1;i <= 3;i++) {
            System.out.println("第" + i + "个十以内随机整数:" + random.nextInt(10));
        }
    }
}
```

![image-20210303202621072](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210303202621072.png)

### 2.猜数字小游戏

> 游戏开始时，会随机生成一个1-100之间的整数`number` 。玩家猜测一个数字`guessNumber` ，会与`number`作比
> 较，系统提示大了或者小了，直到玩家猜中，游戏结束。

```java
package cn.shenzc.java;

import java.util.Random;
import java.util.Scanner;

public class TestRandom3 {
    public static void main(String[] args) {
        //生成一个随机数
        Random random = new Random();
        int number = random.nextInt(100) + 1;
        System.out.println("生成的随机数是:" + number);

        Scanner sc = new Scanner(System.in);
        int guessNumber;
        while (true) {
            System.out.println("请输入你认为的数字:");
            guessNumber = sc.nextInt();
            // 如果用户猜测小于随机数
            if (guessNumber < number) {
                System.out.println("你猜的数小了。");
                continue;
            }
            // 如果用户猜测大于随机数
            if (guessNumber > number) {
                System.out.println("你猜的数大了。");
                continue;
            }
            // 如果用户猜测等于随机数
            if (guessNumber == number) break;
        }
        System.out.println("恭喜你，猜对了！");
    }
}
```

![image-20210303205932148](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210303205932148.png)

# ArrayList集合类

## 引入---对象数组

使用学生数组，存储三个学生对象，代码如下：

```java
// Student
package cn.shenzc.java;

public class Student {
    private String name;
    private int age;

    public Student() {
    }

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}

```

```java
package cn.shenzc.java;

public class ObjectArray {
    public static void main(String[] args) {
        Student s1 = new Student("刘备",18);
        Student s2 = new Student("关羽",19);
        Student s3 = new Student("张飞",20);

        Student[] students = new Student[3];
        students[0] = s1;
        students[1] = s2;
        students[2] = s3;

        for(int i = 0;i < students.length;i++) {
            System.out.println(students[i].getName() + "---" + students[i].getAge());
        }
    }
}
```

![image-20210303212335559](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210303212335559.png)

到目前为止，我们想存储对象数据，选择的容器，只有对象数组。而数组的长度是固定的，无法适应数据变化的需
求。为了解决这个问题，Java提供了另一个容器`java.util.ArrayList` 集合类,让我们可以更便捷的存储和操作对
象数据。

## 什么是ArrayList

`java.util.ArrayList` 是大小可变的数组的实现，存储在内的数据称为元素。此类提供一些方法来操作内部存储的元素。  ArrayList 中可不断添加元素，其大小也自动增长。

数组的长度不可以发生改变，但是ArrayList集合的长度是可以随意变化的。

![Screenshot_20200624_164629](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/Screenshot_20200624_164629.png)

上图的 `<E>` 表示泛型。

泛型只能是**引用类型**，不能是基础类型。

泛型就是定义一种模板，例如`ArrayList<T>`，然后在代码中为用到的类创建对应的`ArrayList<类型>`

```java
public class ArrayList<T> {
    private T[] array;
    private int size;
    public void add(T e) {...}
    public void remove(int index) {...}
    public T get(int index) {...}
}
```

```java
// 创建可以存储String的ArrayList:
ArrayList<String> strList = new ArrayList<String>();
// 创建可以存储Float的ArrayList:
ArrayList<Float> floatList = new ArrayList<Float>();
// 创建可以存储Person的ArrayList:
ArrayList<Person> personList = new ArrayList<Person>();
```

对于ArrayList来说，直接打印得到的不是地址值，而是其中的内容；如果ArrayList为空，则得到的是:**[]**

## 使用

- 导包：`java.util.ArrayList`
- 构造方法：`public ArrayList() `
	- `ArrayList<E> list = new ArrayList<E>();`
	- 在JDK 7后,右侧泛型的尖括号之内可以留空，但是<>仍然要写。简化格式：
		- `ArrayList<E> list = new ArrayList<>();`
- 成员方法：见下

## 常用方法

### 方法定义

`public boolean add(E e):`向集合中添加元素。参数类型和泛型一致。

​		**对于ArrayList的add方法来说，添加元素一定是成功的，返回值可用可不用，但是对于其他集合来说，添加元素不一定成功**

`public E  get(int index):`从集合中获取元素，参数是索引编号。

`public E  remove(int index):`从集合中删除元素。

`public int size():`获取集合的尺寸长度，返回值时集合中元素个数。

### 代码演示

```java
package cn.shenzc.java;

import java.util.ArrayList;

public class TestArrayList2 {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        // 添加元素
        list.add("Java");
        list.add("is");
        list.add("interesting");
        list.add("interesting");
        for (String s : list) {
            System.out.println(s);
        }
        // 获取集合大小
        int size = list.size();
        System.out.println(size);

        // 删除元素
        String rmStr = list.remove(0);
        System.out.println(rmStr);
        // 获取集合大小
        size = list.size();
        System.out.println(size);

        // 获取索引元素
        System.out.println(list.get(1));
    }
}
```

![image-20210303221044643](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210303221044643.png)

## 如何存储基本数据类型

ArrayList对象不能存储基本类型，只能存储引用类型的数据。类似<int> 不能写，但是存储基本数据类型对应的
包装类型是可以的。所以，想要存储基本类型数据， <> 中的数据类型，必须转换后才能编写，转换写法如下：

| 基本类型 | 基本包装类型 |
| :------: | :----------: |
|   byte   |     Byte     |
|  short   |    Short     |
|   int    |   Integer    |
|   char   |  Character   |
|   long   |     Long     |
|  float   |    Float     |
|  double  |    Double    |
| boolean  |   Boolean    |

## 代码演示

### 1.数值添加到集合

> 生成6个1~33之间的随机整数,添加到集合,并遍历

```java
package cn.shenzc.java;

import java.util.ArrayList;
import java.util.Random;

public class TestArrayList3 {
    public static void main(String[] args) {
        // 生成6个1-33的随机整数，并添加到集合
        Random random = new Random();
        ArrayList<Integer> numbers = new ArrayList<>();
        int number;
        for (int i = 0; i < 6; i++) {
            number = random.nextInt(33) + 1;
            numbers.add(number);
        }

        // 遍历集合
        for (Integer num : numbers) {
            System.out.println(num);
        }
    }
}
```

![image-20210304113328560](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210304113328560.png)

### 2.对象添加到集合

> 自定义4个学生对象,添加到集合,并遍历

```java
package cn.shenzc.java;

import java.util.ArrayList;

public class TestArrayList4 {
    public static void main(String[] args) {
        // 自定义4个学生对象
        Student s1 = new Student("唐僧", 18);
        Student s2 = new Student("孙悟空", 500);
        Student s3 = new Student("猪八戒", 1500);
        Student s4 = new Student("沙和尚", 800);

        // 创建ArrayList
        ArrayList<Student> students = new ArrayList<>();
        students.add(s1);
        students.add(s2);
        students.add(s3);
        students.add(s4);

        // 遍历集合
        for (Student student : students) {
            System.out.println(student.getName() + "---" + student.getAge());
        }
    }
}

```

![image-20210304113830425](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210304113830425-1614831522073.png)

# String类

## String类概述

### 概述

`java.lang.String`类代表字符串。Java程序中所有的字符串文字（例如"abc" ）都可以被看作是实现此类的实
例。
类`String`中包括用于检查各个字符串的方法，比如用于比较字符串，搜索字符串，提取子字符串...

### 字符串的特点

1. 字符串的内容永不可变

	- ```java
		String s1 = "abc";
		s1 += "d";
		System.out.println(s1); // "abcd"
		// 内存中有"abc"，"abcd"两个对象，s1从指向"abc"，改变指向，指向了"abcd"。
		```

2. 因为字符串不可变，所以字符串可以共享使用

	- ```java
		String s1 = "abc";
		String s2 = "abc";
		// 内存中只有一个"abc"对象被创建，同时被s1和s2共享。
		```

3. 字符串效果上相当于char数组，但是底层实现是byte数组

	- `"abc"` 等效于 `char[] data={ 'a' , 'b' , 'c' }` 。

	- ```java
		String str = "abc";
		等价于
		char[] data = {'a','b','c'};
		String str = new String(data);
		```

## 使用

- 导包：String类位于`java.lang`包下，无需导包即可使用。
- 构造方法：
	- `public String()`:初始化创建新的String对象，以使其表示空字符串。
	- `public String(char[] values)`:通过当前参数的字符数组来创建新的字符串。
	- `public String(byte[] values)`:通过当前参数的byte数组来创建新的字符串。
- 成员方法：见下

## 常用方法

### 判断功能的方法

1. `public boolean equals(Object anObject):`将此字符串与指定对象进行比较。当且仅当指定对象不为空且为字符序列与比较字符串一致的String对象时，返回true；其他情况返回false。
2. `public boolean equalsIgnoreCase(String str):`将此字符串于指定字符串进行比较。

### 代码演示

```java
package cn.shenzc.java;

public class TestString1 {
    public static void main(String[] args) {
        // 三种构造方法
        String str1 = new String(); // 创建空字符串
        System.out.println("str1 = " + str1);
        char[] data = {'d', 'a', 't', 'a'};
        String str2 = new String(data);
        System.out.println("str2 = " + str2);
        byte[] number = {97, 98}; // 数字转换成对应的ASCII值
        String str3 = new String(number);
        System.out.println("str3 = " + str3);

        // 直接生成字符串
        String str4 = "Hello Java!";

        // 判断功能的方法
        System.out.println(str4.equals("Hello Java"));
        System.out.println("Hello java!".equals(str4));// 推荐写法，因为对象可能为null，会抛出NPE
        System.out.println("hello java!".equalsIgnoreCase(str4));
    }
}
```

![image-20210304153815835](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210304153815835.png)

### 获取功能的方法

1. `public int length()`:返回字符串的长度。
2. `public String concat(String str)`:将指定字符串连接到字符串末尾。
3. `public char charAt(int index)`:返回索引处的char值。
4. `public int indexOf(String str)`:返回指定子字符串在此字符串中第一次出现的索引值。
5. `public String substring(int beginIndex)`:返回从beginIndex开始直到字符串末尾的子字符串。
6. `public String substring(int beginIndex, int endIndex)`:返回beginIndex（包括）与endIndex（不包括）之间的子字符串。

### 代码演示

```java
package cn.shenzc.java;

public class TestString2 {
    public static void main(String[] args) {
        String str = "abcdefghijklmnopqrstuvwxyz";
        System.out.println("str的长度为：" + str.length());
        System.out.println("str第20位的字符为：" + str.charAt(19)); // 索引从零开始
        System.out.println("i第一次出现的位置为：" + (str.indexOf('i') + 1));
        System.out.println("第6位到结尾的子字符串为：" + str.substring(5));
        System.out.println("第7位到12位的子字符串为：" + str.substring(7, 13));
        System.out.println("将str与123连接后的字符串为：" + str.concat("123"));
    }
}
```

![image-20210304202117487](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210304202117487.png)

### 转换功能的方法

1. `public char[] toCharArray()`:将此字符串转换为新的字符数组。
2. `public byte[] getBytes()`:使用平台的默认字符集将该 String编码转换为新的字节数组。
3. `public String replace(CharSequence target, CharSequence replacement)`:将与target字符串匹配的子字符串用replacement替换。

### 代码演示

```java
package cn.shenzc.java;

public class TestString3 {
    public static void main(String[] args) {
        String str = "TestString";
        char[] chars = str.toCharArray();
        for (char aChar : chars) {
            System.out.print(aChar + " ");
        }
        System.out.println();
        byte[] bytes = str.getBytes();
        for (byte aByte : bytes) {
            System.out.print(aByte + " ");
        }
        System.out.println();
        System.out.println("原始字符串：" + str);
        String replace = str.replace("String", "Java");
        System.out.println("替换后的字符串：" + replace);
    }
}
```

![image-20210304204600802](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210304204600802.png)

### 分割功能的方法

- `public String[] split(String regex)`:将字符串按照指定的regex（规则）拆分为字符串数组。

### 代码演示

```java
package cn.shenzc.java;

public class TestString4 {
    public static void main(String[] args) {
        String str = "aabacadaea";
        String[] as = str.split("a");
        for (String a : as) {
            System.out.print(a + "-");
        }
        System.out.println();
        String str2 = "a-b-c-d--e---f";
        String[] split = str2.split("-");
        for (String s : split) {
            System.out.print(s + "+");
        }
    }
}
```

![image-20210304205507768](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210304205507768.png)

## 字符串常量池

由于字符串是不可变的，所以字符串是可以共享的，由此引出字符串常量池。只要是直接用双引号生成的字符串都位于字符串常量池中，是可以共享的。

```java
public class TestStringPool {
    public static void main(String[] args) {
        String s1 = "Shen";
        String s2 = "Shen";
        char[] c = {'S','h','e','n'};
        String s3 = new String(c);

        System.out.println(s1 == s2);
        System.out.println(s1 == s3);
        System.out.println(s2 == s3);
    }
}
```

![](D:%5CGitHub%5Chexo%5Csource%5C_posts%5CJava%E5%B8%B8%E7%94%A8%E7%B1%BB.assets%5Cimage-20200624220304046.png)

对于基本类型来说，==是进行值比较；对于引用类型来说是地址比较。

![image-20200624222535093](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20200624222535093.png)

## 代码演示

### 1.拼接字符串

> 定义一个方法，把数组{1,2,3}按照指定格式拼接成一个字符串。格式参照如下：`[word1#word2#word3]`。

```java
package cn.shenzc.java;

public class TestString5 {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3};
        String s = arrayToString(numbers);
        System.out.println(s);
    }
    public static String arrayToString(int[] arr) {
        String str = new String("[");
        for(int i = 0;i < arr.length;i++) {
            if(i == (arr.length - 1)) {
                str = str.concat(arr[i] + "]");
            } else {
                str = str.concat(arr[i] + "#");
            }
        }
        return str;
    }
}
```

![image-20210304212500806](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210304212500806.png)

### 2.统计字符个数

> 键盘录入一个字符串，统计字符串中大小写字母及数字字符个数。

```java
package cn.shenzc.java;

import java.util.Scanner;

public class TestString6 {
    public static void main(String[] args) {
        System.out.println("请输入一个字符串：");
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        int upper = 0;
        int lower = 0;
        int number = 0;
        int others = 0;
        char element;
        for (int i = 0; i < str.length(); i++) {
            element = str.charAt(i);
            if(element >= 48 && element <= 57) {  // 直接用'0'和'9'代替即可
                number++;
            } else if(element >= 65 && element <= 90) {  // 直接用'A'和'Z'代替即可
                upper++;
            } else if(element >= 97 && element <= 122) {  // 直接用'a'和'z'代替即可
                lower++;
            } else others++;
        }
        System.out.println("在字符串" + str + "中\n，数字出现了" + number + "次，小写字母出现了" +
                lower + "次，大写字母出现了" + upper + "次，其他字符出现了" + others + "次");
    }
}
```

![image-20210304223956949](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210304223956949.png)

# static关键字

## 概述

static 关键字，可以用来修饰成员变量和成员方法，被修饰的成员是属于类的，而不是单单是属
于某个对象的。也就是说，既然属于类，就可以不靠创建对象来调用了。

## static修饰成员变量

当 static 修饰成员变量时，该变量称为**类变量**。该类的每个对象都共享同一个类变量的值。任何对象都可以更改
该类变量的值，也可以在不创建该类的对象的情况下对类变量进行操作。

### 定义格式：

```java
static 数据类型 变量名;
```

## static修饰成员方法

用static修饰的成员方法，叫作类方法，更习惯叫作静态方法。静态方法在声明中有static ，建议使用类名来调用，而不需要创建类的对象。调用方式非常简单。

### 定义格式：

```java
修饰符 static 返回值 方法名(参数列表) {
	方法体
}
```

### 注意事项

1. 静态不能直接访问非静态内容，但可以访问静态内容（静态变量和方法）。因为在内存中先有静态内容，后有非静态内容。但是非静态的成员方法可以访问静态变量和方法。
2. 对于本类当中的静态方法，可以省略类名称。
3. 静态方法中不能使用this关键字。因为this代表当前对象。
4. 推荐使用  类名.静态成员  的方法调用静态成员。

## static修饰代码块

定义在成员位置，用static修饰的代码块叫作静态代码块。随着类的加载而执行且只执行一次，优先于main方法和构造方法的执行。其作用是给静态变量赋值。

```java
static { 
	//静态代码块内容
	}
```

# 数组工具类Arrays

## 概述

`java.util.Arrays`是一个与数组相关的工具类，提供了大量的静态方法，用来实现数组常见的操作，如搜索、排序。

## 常用方法

### public static String toString(int[]  arr): 

将参数数组变成字符串。格式：[元素1，元素2，...]

```java
package cn.shenzc.java;
import java.util.Arrays;
public class TestArrays {
    public static void main(String[] args) {
        int[] array1 = {1,3,2,14,12,76,34};
        System.out.println(Arrays.toString(array1));
        String[] array2 = {"shen","zhi","cheng"};
        System.out.println(Arrays.toString(array2));
    }
}
```

![image-20200626145233749](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20200626145233749.png)

### public static void sort(int[] arr)：

按照默认升序对数组元素进行排序。

```java
package cn.shenzc.java;

import java.util.Arrays;

public class TestArrays {
    public static void main(String[] args) {
        int[] array1 = {1,3,2,14,12,76,34};
        System.out.println(Arrays.toString(array1));
        String[] array2 = {"shen","zhi","cheng"};
        System.out.println(Arrays.toString(array2));

        System.out.println("===============");
        System.out.println("排序：");
        Arrays.sort(array1);
        System.out.println(Arrays.toString(array1));
        Arrays.sort(array2);
        System.out.println(Arrays.toString(array2));
    }
}
```

![image-20200626171303463](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20200626171303463.png)

## 代码演示

> 使用Arrays 相关的API，将一个随机字符串中的所有字符升序排列，并倒序打印。

```java
package cn.shenzc.java;

import java.util.Arrays;

public class TestArrays {
    public static void main(String[] args) {
        // 随机字符串
        String str = "dcvajhgyi";
        // 排序
        // 先转化为字符数组
        char[] chars = str.toCharArray();
        Arrays.sort(chars);
        // 倒序输出
        for (int i = chars.length - 1; i > 0; i--) {
            System.out.print(chars[i] + ",");
        }
        System.out.println(chars[0]);
    }
}

```

![image-20210304233719551](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20210304233719551.png)

# 数学工具类Math

## 概述

`java.lang.Math`是数学相关的工具类，提供了大量的静态方法，完成与数学相关的操作。

## 常用方法 

- `public static double abs(double num):`获取绝对值
- `public static double ceil(double num):`向上取整。返回大于等于参数的最小整数。
- `public static double floor(double num):`向下取整。返回小于等于参数的最小整数。
- `public static long round(double num):`四舍五入。

