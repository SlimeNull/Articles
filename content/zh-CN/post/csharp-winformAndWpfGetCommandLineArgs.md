---
title: "[C#] WinForm 与 WPF 获取命令行参数"
date: 2021-02-09T03:04:19+08:00
tags:
  - .NET
  - C#
  - 经验
---

使用 Environment.GetCommandLineArgs() 即可, 但是需要去除第一个元素, 因为第一个元素时文件自身路径

<!--more-->

### 推荐方法:

#### 1. Environment.GetCommandLineArgs();

```csharp
using System;
Environment.GetCommandLineArgs();   // 返回 string[]
```

注意, 与控制台程序入口处的string[] args相比较, 这个函数返回的结果是完整的命令行, 也就是包含程序自身路径. 例如我一个没有传递任何参数的程序:
![](https://img-blog.csdnimg.cn/20210209030243165.png)
所以注意区分哦.

### 其他:

- WinForm
    在 Program.cs 的 Main 入口参数处添加 string[] args, 然后你可以更改窗体的构造函数, 使其能够接收这个args.
- WPF
    暂时不知道.