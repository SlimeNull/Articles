---
title: "[.NET] WPF Triggers 触发器, EventTrigger, Trigger"
date: 2021-02-15T11:26:55+08:00
tags:
  - .NET
  - WPF
  - XAML
  - 参考
---

通过触发器来实现某种特定情况下才会对控件应用的样式, 例如鼠标悬停时改变颜色

<!--more-->

触发器, 如其名, 可根据某些事件或属性值来触发某些东西, 那么我们来了解一下 xaml 中的触发器吧.

## 样式变更:
我们试试通过使用普通触发器来实现当鼠标悬停时更改控件背景颜色.
![](/assets/202102151127/1.png)
然后运行一下, 效果就是这样:
![](/assets/202102151127/2.gif)

## 启动动画:
然后, 试着用事件触发器(EventTrigger)与DoubleAnimation来创建一个启动动画吧(其实代码都写好了):
![](/assets/202102151127/3.png)
然后运行效果如下:
![在这里插入图片描述](/assets/202102151127/4.gif)
可以看到, 窗口是渐渐浮现的, 也就是Opacity从0到1.


#### 什么? 你问我对应的CS代码怎么写?
先看看这篇文章吧, 看完它, 相信大多数的 xaml 代码, 你都能写出对应的 CS 代码, 这是一个通用的规律.
[[.NET] WPF XAML 原理, 节点与实例, 以及一些重要的零碎知识点.](https://blog.csdn.net/m0_46555380/article/details/113813184)

<br/>

推荐文章:
[[.NET] WPF DoubleAnimation 动画, 一篇文章悟透!](https://blog.csdn.net/m0_46555380/article/details/113813185)