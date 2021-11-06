---
title: Lambda表达式
tags:
  - java基础
  - java笔记
categories:
  - [java]
  - [笔记]
top_img: >-
  https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/Lambda_expression_cover.jpg
cover: 'https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/Lambda_expression_top.jpg'
abbrlink: 3150929911
date: 2020-10-14 22:50:00
updated: 2020-10-14 23:13:00
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
# Lambda的使用前提

## 函数式接口

**The functional interface** is an interface (not a class or enum) with a single abstract method (SAM type). Static and default methods are allowed here.

> 函数式接口是一个只有单一抽象方法的接口（不是类或枚举类型）。静态方法和默认方法允许出现在函数式接口中。

There is a special annotation **@FunctionalInterface** in **The Java Class Library**. It marks functional interfaces and indicates if the interface doesn't  satisfy the requirements of a functional interface (compile-time error). The annotation is not mandatory but it's recommended to mark functional interfaces.

> Java类库中指定了注解**@FunctionalInterface** 来标识函数式接口，使用此注解后不是函数式接口的接口将会出现编译期错误。此注解不是必须的，但建议用来标识函数式接口。

```java
@FunctionalInterface 
interface Func<T, R> { 

    R apply(T val);

    static void doNothingStatic() {

    }

    default void doNothingByDefault() {

    } 
}
```

这是一个泛型函数式接口。只有一个实例方法**apply**。

The interface represents a function (in the math sense). The function has an instance method apply which takes a value of type T and returns a result of type R.

> 这个接口代表一个函数（数学意义上的）。这个函数有一个实例方法，该方法接收一个泛型T的值，返回一个泛型R的值。

The functional interface is another way to model functions using object-oriented programming instead of methods.

## 实现函数式接口

We can't create an instance of the functional interface **Func<T, R>** because it's an interface. First, we should implement it and then  create an instance of the concrete class. The main thing is to implement the **apply** method to get a concrete behavior.

> 我们不能直接实例化函数式接口，因为它是一个接口。首先，我们需要用一个实现类实现这个接口，然后创建一个实现类的实例。主要的事情就是实现apply方法得到具体行为。

Like any interface, a functional interface can be implemented using regular inheritance or anonymous classes.

### 匿名内部类

To implement a functional interface let's create an anonymous class and  override the method apply. The overridden method calculates the square  of a given value.

```java
new Func<Long,Long> square = new Func<Long,Long>(){
	@Override
	Long apply(Long va){
        return val * val;
    }
};
long val = square.apply(10L);//100L
```

### Lambda表达式

```java
new Func<Long,Long> square = val -> val * val;
long val =  square.apply(10L);//100L
```



## Lambda表达式作为参数传给方法

It's possible to pass a lambda expression to a method if the method takes an object of type a suitable functional interface.

Here is an example. The method **acceptFunctionalInterface** takes an object of the standard type **Function<Integer, Integer>**.

```java
public static void acceptFunctionalInterface(Function<Integer, Integer> f) {
   System.out.println(f.apply(10));
}
```

Let's pass some functions in the method:

```java
// it returns the next value
Function<Integer, Integer> f = (x) -> x + 1;

acceptFunctionalInterface(f); // it prints 11

// or even without a reference
acceptFunctionalInterface(x -> x + 1); // the result is the same: 11
```

Inside the method **acceptFunctionalInterface**, the given function will be invoked. In enterprise programming, it is often called **the callback**.

According to Wikipedia: "*a callback is a piece of executable code that is passed as an argument to other code, which is expected to call  back (execute) the argument at some convenient time."*

In other words, in Java, we can pass our functions (presented by objects) in a method/function as its arguments.

**Note**. In functional programming, a function (including methods in Java) that accepts or returns another function is called a **higher-order function**. A lot of features such as **function composition**, **currying**, **monads**, and some others are based on this idea.

## Usage of closures

In the body of a lambda expression, it's  possible to capture values from a context where the lambda is defined.  This technique is called **closure**.

Let's see an example.

```java
final String hello = "Hello, ";
Function<String, String> helloFunction = (name) -> hello + name;

System.out.println(helloFunction.apply("John"));
System.out.println(helloFunction.apply("Anastasia"));
```

The lambda expression captured the final variable **hello**.

The result of this code.

```java
Hello, John
Hello, Anastasia
```

It's possible only if a context variable has a keyword **final** or it's **effectively final**, i.e. variable can't be changed. Otherwise, an error happens.

Let's consider the example with an effectively final variable.

```java
int constant = 100;
Function<Integer, Integer> adder = x -> x + constant;

System.out.println(adder.apply(200));
System.out.println(adder.apply(300));
```

The variable **constant** is effectively final and being captured by the lambda expression.

**Note.** If we use anonymous classes instead of lambdas, we can do the same tricks.

Lambda的语法非常简洁，完全没有面向对象复杂的束缚。但是使用时有几个问题需要特别注意：

1. 使用Lambda必须具有接口，且要求接口中有且仅有一个抽象方法。
	无论是JDK内置的 Runnable 、 Comparator 接口还是自定义的接口，只有当接口中的抽象方法存在且唯一
	时，才可以使用Lambda。
2. 使用Lambda必须具有上下文推断。
	也就是方法的参数或局部变量类型必须为Lambda对应的接口类型，才能使用Lambda作为该接口的实例。

> 备注：有且仅有一个抽象方法的接口，称为“函数式接口”。



# 函数式编程思想概述

在数学中，函数就是有输入量、输出量的一套计算方案，也就是“拿什么东西做什么事情”。相对而言，面向对象过
分强调“必须通过对象的形式来做事情”，而函数式思想则尽量忽略面向对象的复杂语法——强调做什么，而不是以
什么形式做。
面向对象的思想:
做一件事情,找一个能解决这个事情的对象,调用对象的方法,完成事情.
函数式编程思想:
只要能获取到结果,谁去做的,怎么做的都不重要,重视的是结果,不重视过程

# 冗余的Runnable代码

## 传统写法

当需要启动一个线程去完成任务时，通常会通过 java.lang.Runnable 接口来定义任务内容，并使用
java.lang.Thread 类来启动该线程。代码如下：

```java
package space.buercheng.java.demo05;

public class TestThread {
    public static void main(String[] args) {
        //使用匿名内部类创建一个Runnable的实现类对象，作为参数传入Thread的构造器中，并重写Runnable的run方法设置线程任务，
        // 然后调用start方法，启动线程
        new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("重写了run方法");
            }
        }).start();
    }
}

```

本着“一切皆对象”的思想，这种做法是无可厚非的：首先创建一个 Runnable 接口的匿名内部类对象来指定任务内
容，再将其交给一个线程来启动。

## 代码分析

对于 Runnable 的匿名内部类用法，可以分析出几点内容：

- Thread 类需要 Runnable 接口作为参数，其中的抽象 run 方法是用来指定线程任务内容的核心；
- 为了指定 run 的方法体，**不得不**需要 Runnable 接口的实现类；
	为了省去定义一个 RunnableImpl 实现类的麻烦，**不得不**使用匿名内部类；
	必须覆盖重写抽象 run 方法，所以方法名称、方法参数、方法返回值**不得不**再写一遍，且不能写错；
	而实际上，**似乎只有方法体才是关键所在**。

# 编程思想转换

# 改用更优的Lambda表达式

借助Java 8的全新语法，上述 Runnable 接口的匿名内部类写法可以通过更简单的Lambda表达式达到等效：

```java
package space.buercheng.java.demo05;

public class TestThread {
    public static void main(String[] args) {
        /*//使用匿名内部类创建一个Runnable的实现类对象，作为参数传入Thread的构造器中，并重写Runnable的run方法设置线程任务，
        // 然后调用start方法，启动线程
        new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("重写了run方法");
            }
        }).start();*/

        //Lambda表达式写法
        new Thread(() -> {
            System.out.println("重写了run方法");
        }).start();
    }
}

```

这段代码和刚才的执行效果是完全一样的，可以在1.8或更高的编译级别下通过。从代码的语义中可以看出：我们
启动了一个线程，而线程任务的内容以一种更加简洁的形式被指定。
不再有“不得不创建接口对象”的束缚，不再有“抽象方法覆盖重写”的负担，就是这么简单！

# 匿名内部类回顾

## 使用实现类

要启动一个线程，需要创建一个 Thread 类的对象并调用 start 方法。而为了指定线程执行的内容，需要调用
Thread 类的构造方法：
public Thread(Runnable target)
为了获取 Runnable 接口的实现对象，可以为该接口定义一个实现类 RunnableImpl，然后创建该实现类的对象作为 Thread 类的构造参数。

## 使用匿名内部类

这个 RunnableImpl 类只是为了实现 Runnable 接口而存在的，而且仅被使用了唯一一次，所以使用匿名内部类的
语法即可省去该类的单独定义。

## 匿名内部类的好处与弊端

一方面，匿名内部类可以帮我们**省去实现类的定义**；另一方面，匿名内部类的**语法——确实太复杂了**！

## 语义分析

仔细分析该代码中的语义， Runnable 接口只有一个 run 方法的定义：
public abstract void run();
即制定了一种做事情的方案（其实就是一个函数）：

- 无参数：不需要任何条件即可执行该方案。
- 无返回值：该方案不产生任何结果。
- 代码块（方法体）：该方案的具体执行步骤。

同样的语义体现在 Lambda 语法中，要更加简单：

`() -> { System.out.println("重写了run方法");}`

- 前面的一对小括号即 run 方法的参数（无），代表不需要任何条件；
- 中间的一个箭头代表将前面的参数传递给后面的代码；
- 后面的输出语句即业务逻辑代码。

# Lambda语句标准格式

Lambda省去面向对象的条条框框，格式由3个部分组成：

- 一些参数
- 一个箭头
- 一段代码

Lambda表达式的标准格式为：

`(参数类型 参数名称) ‐> { 代码语句 }`

格式说明：
小括号内的语法与传统方法参数列表一致：无参数则留空；多个参数则用逗号分隔。
-> 是新引入的语法格式，代表指向动作。
大括号内的语法与传统方法体要求基本一致

## 代码演示

### 示例1：无参无返回

给定一个厨子 Cook 接口，内含唯一的抽象方法 makeFood ，且无参数、无返回值。如下：

```java
public interface Cook {
void makeFood();
}
```

在下面的代码中，请使用Lambda的标准格式调用 invokeCook 方法，打印输出“吃饭啦！”字样：

```java
public class InvokeCook {
public static void main(String[] args) {
// TODO 请在此使用Lambda【标准格式】调用invokeCook方法
}
private static void invokeCook(Cook cook) {
cook.makeFood();
}
}
```

```java
package space.buercheng.java.demo06;

public class InvokeCook {
    public static void main(String[] args) {
        //使用匿名内部类实现
        invokeCook(new Cook() {
            @Override
            public void makeFood() {
                System.out.println("吃饭啦！");
            }
        });

        //使用Lambda表达式
        invokeCook(() -> {
            System.out.println("吃饭啦！");
        });
    }
    private static void invokeCook(Cook cook) {
        cook.makeFood();
    }
}

```

![](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20200912012644274.png)

### 示例2：有参有返回

给定一个计算器 Calculator 接口，内含抽象方法 calc 可以将两个int数字相加得到和值：

```java
public interface Calculator {
int calc(int a, int b);
}
```

在下面的代码中，请使用Lambda的标准格式调用 invokeCalc 方法，完成120和130的相加计算：

```java
public class Demo08InvokeCalc {
public static void main(String[] args) {
// TODO 请在此使用Lambda【标准格式】调用invokeCalc方法来计算120+130的结果ß
} p
rivate static void invokeCalc(int a, int b, Calculator calculator) {
int result = calculator.calc(a, b);
System.out.println("结果是：" + result);
}
}
```

```java
public class TestLambda {
    public static void main(String[] args) {
        int a = 120;
        int b = 130;
        /*//匿名内部类方式
        invokeCalc(a, b, new Calculator() {
            @Override
            public int calc(int a, int b) {
                return a + b;
            }
        });*/

        //Lambda方式
        invokeCalc(a, b, (int x, int y) -> {
            return x + y;
        });

    }

    private static void invokeCalc(int a, int b, Calculator calculator) {
        int result = calculator.calc(a, b);
        System.out.println("结果是：" + result);
    }
}
```



# Lambda省略格式

## 省略规则

在Lambda标准格式的基础上，使用省略写法的规则为：

1. 小括号内参数的类型可以省略；
2. 如果小括号内有且仅有一个参，则小括号可以省略；
3. 如果大括号内有且仅有一个语句，则无论是否有返回值，都可以省略大括号、return关键字及语句分号（三个要一起省略）。

## 代码演示

### 示例1:

```java
package space.buercheng.java.demo06;

public class InvokeCook {
    public static void main(String[] args) {
        //使用匿名内部类实现
        invokeCook(new Cook() {
            @Override
            public void makeFood() {
                System.out.println("吃饭啦！");
            }
        });

        //使用Lambda表达式
        invokeCook(() -> {
            System.out.println("吃饭啦！");
        });

        //Lambda省略格式
        invokeCook(() -> System.out.println("吃饭啦！"));
    }
    private static void invokeCook(Cook cook) {
        cook.makeFood();
    }
}

```

![](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20200912013249950.png)

### 示例2

```java
package space.buercheng.java.demo04;

public class TestLambda {
    public static void main(String[] args) {
        int a = 120;
        int b = 130;
        /*//匿名内部类方式
        invokeCalc(a, b, new Calculator() {
            @Override
            public int calc(int a, int b) {
                return a + b;
            }
        });*/

        //Lambda方式
        invokeCalc(a, b, (int x, int y) -> {
            return x + y;
        });

        //Lambda省略格式
        invokeCalc(120,130,(x,y) -> x + y);

    }

    private static void invokeCalc(int a, int b, Calculator calculator) {
        int result = calculator.calc(a, b);
        System.out.println("结果是：" + result);
    }
}

```

![](https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/image-20200912013439324.png)