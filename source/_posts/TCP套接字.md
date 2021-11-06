---
title: TCP套接字
updated: '`r format(Sys.time(), ''%d %B, %Y'')`'
tags:
  - java基础
  - JAVA SOCKET
  - 网络基础
categories:
  - - Java Web
  - - java
  - - 计算机网络
top_img: 'https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/images.png'
cover: >-
  https://cdn.jsdelivr.net/gh/zerohk/blogpic@pics/img/Id_1f0835cb-f3a7-4c80-8670-8889b0599d4d.png
abbrlink: 1692463639
date: 2020-11-08 00:29:28
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

# 概述

Java为TCP通信提供了两个类：` java.net.Socket`和`java.net.ServerSocket`。一个Socket对象代表一个TCP连接中的一端。一个TCP连接是一个抽象的双向信道，他的两端由IP地址和端口号来进行识别。要进行TCP通信，TCP连接要进行一系列的活动：首先，客户端TCP向服务端TCP发送请求，要求建立TCP连接；服务端存在一个ServerSocket的实例，用来监听来自客户端的所有TCP连接的请求，并且对每一个进入的连接创建一个Socket对象来处理其请求。因此，客户端只需要使用Socket对象即可，服务端则需要处理ServerSocket和Socket两者的对象。

# 创建一个TCP客户端

客户端与一个积极等待连接的服务端初始化通信，TCP客户端一般要经过以下几个步骤：

1. 构造一个Socket类的实例：构造器与指定的远程主机和端口建立一个TCP连接。
2. 通过Socket的IO流进行通信：建立连接后的Socket实例包含一个InputStream和OutputStream，这两个IO流可以像其他IO流一样使用。
3. 使用Socket的close()方法关闭连接。

```java
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.net.SocketException;

public class TCPEchoClient {
    public static void main(String[] args) throws IOException {
        if (args.length < 2 || args.length > 3) {
            throw new IllegalArgumentException("Parameter(s): <Server> <Word> [<Port>]");
            // 如果参数不是：服务器（ip或域名） 描述信息 端口号（可选）的格式，则抛出非法参数异常
        }
        String server = args[0]; // 服务器名或IP地址
        //利用String类的getBytes()方法将描述信息转为byte数组
        byte[] data = args[1].getBytes();
        //如果输入的参数包含端口号就将其赋值给port，否则默认port为7
        int servPort = (args.length == 3) ? Integer.parseInt(args[2]) : 7;

        //创建连接指定服务器端口的套接字
        Socket socket = new Socket(server, servPort);
        System.out.println("Connected to server...sending echo string");

        // 每一个被连接的Socket实例都有一个InputStream和一个OutputStream，它们可以向其他Java I/O流一样使用
        InputStream in = socket.getInputStream();
        OutputStream out = socket.getOutputStream();

        out.write(data); //发送描述信息给服务器

        // 从服务器接收相同的描述信息
        int totalBytesRcvd = 0;// 当前接收到的字节总数
        int bytesRcvd;// 最后一次read接收到的字节数
        while (totalBytesRcvd < data.length) {
            if ((bytesRcvd = in.read(data, totalBytesRcvd, data.length) - totalBytesRcvd) == -1) {
                throw new SocketException("Connection closed prematurely");
            }
            totalBytesRcvd += bytesRcvd;
        }

        System.out.println("Received:" + new String(data));

        socket.close();// 关闭连接

    }
}

```

# Socket方法详解

## 构造方法

- `public Socket()`：创建一个未连接的Socket对象。如果该应用指定了客户端TCP socket的实现，则调用该实现类的`createSocketImpl`方法来创建该Socket对象。如果没有则使用系统默认的socket实现类来创建该对象。在进行通信之前，必须通过connect()方法显式的建立连接。

------



- `public Socket(String host,int port) throws UnknownHostException,IOException`：创建一个流式TCP套接字，并连接到指定主机的指定端口。如果指定主机为null，相当于调用了`InetAddress.getByName(null)`,也就是说，将地址指定为回环接口。不能确定主机的IP地址时，抛出`UnknownHostException` ；创建socket时发生IO错误，抛出`IOException`;端口号不在正确范围内（0~65535）时，抛出`IllegalArgumentException`。

------



- `public Socket(String host,int port,InetAddress localAddr,int localPort) throws IOException`：创建一个TCP socket，与给定的主机和端口号相连接，并且也会将socket绑定（`bind()`）到指定的本地地址和端口。如果指定主机为null，相当于调用了`InetAddress.getByName(null)`,也就是说，将地址指定为回环接口。如果本地端口号为0，则由系统自动分配一个可用的端口。`localAddr`为null时，可以是任意本地（anyLocal）地址。创建socket时发生IO错误，抛出`IOException`;端口号不在正确范围内（0~65535）时，抛出`IllegalArgumentException`。

------



- `public Socket(InetAddress addr,int port) throws IOException`：`addr`为IP地址。创建一个流式TCP socket并将其连接到指定IP地址的指定端口。如果该应用指定了客户端socket的实现，则调用该实现类的`createSocketImpl`方法来创建该Socket对象。如果没有则使用系统默认的socket实现类来创建该对象。创建socket时发生IO错误，抛出`IOException`;端口号不在正确范围内（0~65535）时，抛出`IllegalArgumentException`。`addr`为null时，抛出 `NullPointerException`。

------



- `public Socket(InetAddress addr,int port,InetAddress localAddr,int localPort)throws IOException`：创建一个TCP socket并且与给定的远程地址和远程端口相连接。并且也会将socket绑定（`bind()`）到指定的本地地址和端口。如果`localAddr`为null，相当于将地址指定为任意本地地址（ `InetAddress.isAnyLocalAddress()`）。如果本地端口号为0，则由系统自动分配一个可用的端口。创建socket时发生IO错误，抛出`IOException`;端口号不在正确范围内（0~65535）时，抛出`IllegalArgumentException`。`addr`为null时，抛出 `NullPointerException`。

------

[^]: 以上方法中的String参数，可以跟InetAddress中能接收的String参数格式一致。

## 其他常用方法

- `public void connect(SocketAddress endPoint)throws IOException`:将此socket连接到指定服务器。如果在连接过程中发生错误，抛出`IOException`；如果该socket有一个关联的信道，并且该信道处于非阻塞（non-blocking）状态，则抛出`IllegalBlockingModeException`;如果 `endPoint`为null或是不受此socket支持的SocketAddress的子类，则抛出`IllegalArgumentException`。
- `public void connect(SocketAddress endPoint,int timeout)throws IOException`:将此socket连接到指定服务器，并指定超时值（timeout value，以毫秒为单位）。timeout为0时代表永不超时。连接将会处于阻塞状态，直到连接建立或是发生错误。
- `InputStream getInputStream()`:返回一个输入流给该socket。如果该socket与某一信道相关联，则输入流的操作都将交给此信道。如果该信道处于非阻塞状态，那么该输入流的read操作将会抛出`IllegalBlockingModeException`。
- `OutputStream getOutputStream()`：返回一个输出流给该socket。
- `void close()`：关闭socket以及其关联的输入输出流。
- `void shutdownInput()`：在输入流一端关闭TCP连接。任意未读数据将会被丢弃，包括socket缓存的数据，运输中的数据以及将来到达的数据。此后任何尝试从此socket读取数据的行为都将抛出异常。
- `void shutdownOutput()`：在输出流一端关闭连接。但此方法会确保已经写入socket输出流的数据已经传输到另一端。
- `InetAddress getInetAddress()`:
- `int getPort()`:
- `InetAddress getLocalAddress()`:
- `int getLocalPort()`:
- `SocketAddress getRemoteSocketAddress()`:
- `SocketAddress getLocalSocketAddress()`:

# SocketAddress抽象类以及InetSocketAddress类

```java
public abstract class SocketAddress extends Object implements Serializable
```

这个类位于`java.net`包下，代表一个无协议的Socket 地址。因为是抽象类，所以需要一个带指定协议的子类来实现：**InetSocketAddress**。

```java
public class InetSocketAddress extends SocketAddress
```

这个类位于`java.net`包下，这个类实现了SocketAddress类，代表了一个IP类型的Socket地址（IP地址+端口)，也可以是域名+端口的形式。它提供了一个不可变对象，以供socket对象来绑定（binding)、连接(connecting)或返回(return value) 。wildcard指的是一个特定的本地地址，他通常意味着“any”，并且只能用于绑定

## InetSocketAddress方法

### 构造方法

- `public InetSocketAddress(int port)`：创建一个socket地址，它的IP是一个wildcard地址，端口是port参数。
- `public InetSocketAddress(String hostname, int port)`：从给定的域名和端口号创建一个socket address。会尝试把域名解析为IP地址，如果解析失败，会把域名标记为*unresolved*。端口为0，自动分配。
- `public InetSocketAddress(InetAddress addr, int port)`：从给定的IP地址和端口号创建一个socket address。IP地址为null时，指派wildcard地址。端口为0，自动分配。

### 其他方法

- `public static InetSocketAddress createUnresolved(String host,
	int port)`：利用给定的域名和端口号创建一个unresolved socket 地址，不会对域名进行解析，直接将域名标记为*unresolved*。
- `public final boolean isUnresolved()`：判断地址是否是*unresolved*。
- `public final InetAddress getAddress()`:获取InetAddress。如果为*unresolved*则返回null。
- `int getPort()`:获取端口号
- `String getHostName()`:返回域名。如果socket地址是用IP地址创建的，可能会反向域名解析查找域名。
- `String toString()`：返回该InetSocketAddress的字符串形式，调用了InetAddress的toString()方法并通过冒号加上端口号。如果地址是*unresolved*，那么将会在地址处显示 `<unresolved>` 。

# 创建一个TCP服务端

TCP服务端的任务是设置另一个通信端点，并且积极的等待来自客户端的连接。典型的服务端创建过程如下：

1. 指定端口号，构造一个ServerSocket的实例，这个实例监听该端口的所有连接。
2. 重复执行以下任务：
	1. 调用ServerSocket对象的accept()方法，获得下一个来自客户端的连接。一旦一个来自客户端的新连接建立完成，accept()方法创建了一个Socket对象并返回；
	2. 通过返回的Socket对象的InputStream和OutputStream通客户端进行通信；
	3. 通信完成后，调用Socket对象的close()方法关闭连接。

```java
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketAddress;

public class TCPEchoServer {
    private static final int BUFFSIZE = 32; // size of receive buffer

    public static void main(String[] args) throws IOException {
        if (args.length != 1) {
            throw new IllegalArgumentException("Parameter(s): <Port>");
        }

        int servPort = Integer.parseInt(args[0]);

        //创建一个服务端socket接收客户端的请求
        ServerSocket serverSocket = new ServerSocket(servPort);

        int recvMsgSize;// 接受的消息的大小
        byte[] recvBuff = new byte[BUFFSIZE];//接收 缓存

        while (true) { //一直运行，接收并处理来自客户端的连接
            Socket clinSock = serverSocket.accept();// 接受来自客户端的连接
            SocketAddress clientAddress = clinSock.getRemoteSocketAddress(); // 获取客户端地址
            System.out.println("Handling client at " + clientAddress);

            InputStream in = clinSock.getInputStream();//
            OutputStream out = clinSock.getOutputStream();//

            //一直接收，直到客户端关闭连接，当结果为-1时返回
            while ((recvMsgSize = in.read(recvBuff)) != -1) {
                out.write(recvBuff,0,recvMsgSize);
            }
            clinSock.close();//关闭socket，与客户端连接断开

        }
    }
}

```

# ServerSocket方法

## 构造方法

- `public ServerSocket() throws IOException`：创建一个未绑定的server socket；该对象未绑定任何端口，在使用前必须使用bind()方法绑定端口。
- `public ServerSocket(int port) throws IOException`:创建一个与指定端口绑定的server socket。端口号为0，随机指定一个未分派端口，一般是临时端口ephemeral port。指定的端口号可以通过getLocalPort()方法获取。该方法创建的对象将连接队列大小设置为50，当待连接的数量超过50时，会拒绝其连接。
- `public ServerSocket(int port,int backlog) throws IOException`：backlog表示能够请求的连接的最大数量。该方法创建的对象指定了能够连接的数量大小。
- `public ServerSocket(int port,int backlog,InetAddress bindAddr) throws IOException`：bindAddr表示该socket绑定的本地InetAddress。bindAddr参数对多宿主主机（multi-homed host）创建ServerSocket很有用，但只会分配其中一个地址给它。多宿主主机指的是有多个网络接口的主机。

## 其他方法

- `void bind(SocketAddress endPoint) throws IOException`：将此ServerSocket绑定到指定SocketAddress（IP地址加端口号）。如果地址为空，系统会分配一个临时端口和有效的本地地址给这个socket。
- `void bind(SocketAddress endPoint，int backlog)throws IOException`:指定能连接的最大值。
- `Socket accept()`:监听连接到此socket的连接并接受它。这个方法处于阻塞状态，直到一个连接建立。
- `void close()`:关闭此socket。
- `InetAddress getInetAddress()`:返回此server socket 的本地地址。未绑定地址时，返回null。
- `SocketAddress getLocalSocketAddress()`:返回此server socket绑定的本地socket address。未绑定地址时，返回null。
- `int getLocalPort()`:返回此server socket监听的端口，如果尚未监听端口则返回-1。

# 输入输出流

从以上例子可以看出，Java中为TCP套接字提供的基础IO模型是流（stream）的抽象类；一个流就是一串有序的字节序列。Java输入流（input stream）支持读取字节，输出流（output stream）支持写入字节。

OutputStream是所有输出流的抽象父类。使用OutputStream我们可以write、flush、close。

```java
public abstract class OutputStream
extends Object
implements Closeable, Flushable //java.io
```

InputStream是所有输入流的抽象父类。使用InputStream我们可以从输入流读取字节，关闭输入流。

```java
public abstract class InputStream
extends Object
implements Closeable//java.io
```



## OutputStream的方法

- `abstract void write(int b) throws IOException`：将指定字节写入到该输出流。参数b的低八位字节将会写入到输出流，高24位将会被省略。OutputStream的子类必须实现该方法。
- `void write(byte[] b) throws IOException`：将指定字节数组b的b.length个字节写入到输出流。实现效果应该与调用`write(b,0,b.length)`一致。
- `void write(byte[] b,int off,int len) throws IOException`：将指定字节数组b中从off开始的len个字节写入到输出流。b[off]是第一个写入的字节，b[off+len]是最后一个写入的字节。OutputStream中的这个方法是，每次写入一个字节都调用一次只有一个参数的write(int b)方法，子类应该更好的实现该方法。如果b为null，抛出NullPointerException；如果off为负，或者len为负，或者off+len大于b.length，抛出IndexOutOfBoundException。
- ` void flush() throws IOException`：刷新输出流，强制写出所有缓存的字节，如果此输出流的实现已经缓冲了以前写入的任何字节，则调用此方法指示应将这些字节立即写入它们预期的目标。如果此流的预期目标是由基础操作系统提供的一个抽象（如一个文件），则刷新此流只能保证将以前写入到流的字节传递给操作系统进行写入，但不保证能将这些字节实际写入到物理设备（如磁盘驱动器）。
	OutputStream 的 flush 方法不执行任何操作。 
- `void close()throws IOException`:关闭输出流并释放占用的系统资源，关闭后的输出流不能执行任何操作也不能被重启。OutputStream的close方法不执行任何操作。

## InputStream的方法

- `abstract int read() throws IOException`：从输入流读取下一个数据字节。字节值返回的是一个0-255的int类型。如果到达输入流终点而没有字节可以读取，则返回-1；这个方法处于阻塞状态，直到输入数据是可读取的、检测到输入流的终点或是抛出了异常。

- `int read(byte[] b) throws IOException`：读取输入流的一系列字节，并将其存储到缓存数组b，读取的字节数以int形式返回。这个方法处于阻塞状态，直到输入数据是可读取的、检测到输入流的终点或是抛出了异常。如果b的长度为零，则没有数据被读取，返回0；否则，至少尝试读取一个字节。如果因为输入流到达了文件的尾部而没有字节可以读取，返回-1；否则至少读取一个字节并存储到b。该方法的实现应该等效于read(b, 0, b.length)。

- `int read(byte[] b,int off,int len) throws IOException`：至多从输入流读取len个字节存储到byte数组b中，off代表从b中哪个位置开始存储。虽然传入参数是len，但可能实际读取的字节数少于len，并且读取的字节个数以int形式返回。这个方法处于阻塞状态，直到输入数据是可读取的、检测到输入流的终点或是抛出了异常。如果len为0，没有字节被读取，返回0；否则，至少尝试读取一个字节。如果因为输入流到达了文件的尾部而没有字节可以读取，返回-1；否则至少读取一个字节并存储到b。第一个被读取的字节存储到b[off],第二个被读取的数据存储到b[off+1],以此类推。读取的字节数最多为len。

- `int available() throws IOException`：返回此输入流下一个方法调用可以不受阻塞地从此输入流读取（或跳过）的估计字节数；如果到达输入流末尾，则返回 0。下一个调用可能是同一个线程，也可能是另一个线程。一次读取或跳过此估计数个字节不会受阻塞，但读取或跳过的字节数可能小于该数。

	注意，有些 InputStream 的实现将返回流中的字节总数，但也有很多实现不会这样做。试图使用此方法的返回值分配缓冲区，以保存此流所有数据的做法是不正确的。

- `void close() throws IOException`:关闭输入流并释放占用的系统资源。InputStream的close方法不执行任何操作。