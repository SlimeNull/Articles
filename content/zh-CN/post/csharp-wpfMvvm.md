---
title: "[.NET] WPF 数据绑定与 MVVM 模型"
date: 2021-02-15T18:13:33+08:00
tags:
  - .NET
  - C#
  - WPF
  - MVVM
  - 参考
---

欸? 听说你还在使用 Dispatcher 来设置与获取数据? 落后啦! 快来试试 MVVM 吧!

<!--more-->

## 数据绑定:
数据绑定需要有一个源, 这个源可以是一个控件, 也可以是一个对象.

最简单的数据绑定是对控件属性的绑定. 例如, 一个 Label 始终显示 Slider 的值:
![](https://img-blog.csdnimg.cn/20210216034234250.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2NTU1Mzgw,size_16,color_FFFFFF,t_70)
![\[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-mi0xbExM-1613418382294)(https://i.loli.net/2021/02/16/4qFhAxjnDcHfmOv.gif#pic_center)\]](https://img-blog.csdnimg.cn/img_convert/b3e1831313da53797781fd6b7ddf92f8.gif#pic_center)
绑定数据到某个控件, 此时, 数据绑定的源就是这个控件. Path是Value, 即, 我们要获取与设置这个控件的Value
## DataContext:
如果要设置源为一个对象. 例如我们定义的 MyObj 的实例, 则需要指定 DataContext. 指定 DataContext 的控件以及它的子元素都将使用指定的对象作为数据绑定的源. 例如:
![](https://img-blog.csdnimg.cn/2021021604063641.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2NTU1Mzgw,size_16,color_FFFFFF,t_70)
![](https://img-blog.csdnimg.cn/20210216040836373.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2NTU1Mzgw,size_16,color_FFFFFF,t_70)


## MVVM:
MVVM 的意思是: Model, View, ViewModel, 其中:

- Model: 程序的核心代码, 例如数据库操作
- View: 程序的展示层, 例如UI展示与UI事件.
- ViewModel: 视图数据层.

啊我知道你很迷惑... 毕竟当时我也是这样, 反正, 一个例子足够描述出来了.

## 例子:
1. 新建一个 WPF 项目. 此次演示, 我们以 MvvmTest 作为项目名.
2. 在项目中创建以下文件夹: Model, View, ViewModel.
3. 将 MainWindow.xaml 移动到 View 中. 并调整 xaml 中的 Window 的 x:Class 属性值.