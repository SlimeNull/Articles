---
title: "[C#] 使用 GDI+ 在控制台绘图"
date: 2020-11-15T21:59:01+08:00
tags:
  - .NET
  - C#
  - 笔记
---

直接通过 WinAPI 获取控制台窗口句柄, 然后创建 Graphics 对象, 就可以肆无忌惮的画图了

<!--more-->

获取控制台的窗口句柄

```csharp
[DllImport("kernel32.dll")]
static extern IntPtr GetConsoleWindow();
```

获取Graphics对象

```csharp
Graphics g = Graphics.FromHwnd(GetConsoleWindow());
```

于是乎, 你就可以通过获取的Graphics对象随便进行绘图了!

> 但是, 注意, 当控制条刷新的时候, 比如Console.Clear(), 或者控制台光标经过绘图区域, 绘制的内容就会失效, 这时你需要重新绘制. (如果有控制台刷新的事件就好了)