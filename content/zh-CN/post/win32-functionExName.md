---
title: "[Win32] Windows APi 函数后缀 (A, W, ExA, ExW) 的含义"
date: 2020-11-20T03:32:37+08:00
tags:
  - C++
  - Win32
  - 笔记
---

A = ANSI, W = WideChar, Ex = Extended, ExA = Extended ANSI, ExW = Extended WideChar

<!--more-->

- A 表示使用 ANSI 编码作为标准输入与输出流的文本编码
- W 表示使用 Unicode 作为编码
- Ex 表示拓展, 标注了 Ex 的 WinAPI 函数会比没有标 Ex 的函数多一些参数什么的, 可以说拓展了一些功能
- ExA 与 ExW 就是 A, W 与 Ex 的结合了