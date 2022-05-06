---
title: "[C#] 单文件编译 - 编译时嵌入dll"
date: 2021-02-03T06:56:00+08:00
tags:
  - .NET
  - C#
  - 笔记
---

直接安装 Costura.Fody 库就能使项目单文件编译啦~

<!--more-->

### 1.打开 NuGet 包管理器

位于 工具 -> NuGet 包管理器 -> 管理解决方案的 NuGet 程序包
![打开NuGet包管理器](https://img-blog.csdnimg.cn/20210203064653427.png)

### 2. 安装

搜索 Costura.Fody 并将其安装到你的项目
![安装Costura.Fody](https://img-blog.csdnimg.cn/20210203065115536.png)

### 3. 起飞

然后, 进行编译, 你就会发现! 所有的dll全部被打包进exe中啦~~~
![但文件发布](https://img-blog.csdnimg.cn/20210203065438794.png)