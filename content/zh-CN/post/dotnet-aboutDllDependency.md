---
title: "[.NET] 关于 .NET 动态链接库的目标与依赖问题"
date: 2022-03-22T17:24:05+08:00
tags:
  - .NET
  - 笔记
  - 干货
---

关于 .NET 类库的目标, 多目标, 类库依赖的各种问题, 例如 .NET Framework 项目使用 .NET Framework 类库和 .NET Standard 类库有何不同, 类库如何处理依赖, 以及为何类库不可以跨目标等问题

<!--more-->

## .NET Framework

.NET Framework 运行在 Windows 平台上, 很多程序集例如 System.Drawing 都是集成在 .NET Framework 的, 如果你使用这个程序集, 则不必再为它添加依赖, 因为 .NET Framework 已经包含了它.

如果你在 .NET Framework 中使用一些目标为 .NET Standard 的类库, 那么你需要注意, .NET Standard 没有对 .NET Framework 的特定优化, 倘若这个类库依赖于其他的类库, 那么你需要添加依赖, 如果是诸如 System.Drawing 这类 .NET Framework 本身就内置的库, 你也需要重复的安装该依赖, 即便它们的功能是一样的, 但是它们是不同的程序集.

这告诉我们, 在编写类库时, 要尽可能的照顾到 .NET Framework 的特性, 如果你使用 .NET Framework 的类库, 记得在你的类库目标(Target)中添加 .NET Framework 的目标. 这样在使用 .NET Framework 内置的标准库时, 用户就不需要重复安装依赖了.

## .NET Core

.NET Core 是 .NET 的跨平台版本, 它与 .NET Framework 截然不同, 包括标准库都是不一样的, 如前面的例子, 如果想在 .NET Core 中使用 System.Drawing, 你必须在 nuget 中安装这个包.

.NET Core 使用 .NET Standard 的类库是安全的, 不需要顾及那么多, 因为 .NET Standard 只能使用 nuget 包, 而不能使用 .NET Framework 的类库. .NET Core 也是相同的, 所以无论这个 .NET Standard 的类库引用了什么依赖, 使用了这个类库的 .NET Core 程序也不会安装依赖.

## .NET

.NET, 也就是诸如 .NET5, .NET6 这类近来 .NET 重点发展方向, 它其实是基于 .NET Core 的, 你可以将它理解为 .NET Core 的新版本.

## 如何选择目标

在编写程序时, 如果你打算使他运行在 Windows 上, 那么请一定要选择 .NET Framework 的目标, 如果你打算使他运行在 Linux 上, 那么请一定要选择 .NET Core 的目标. (如果运行你软件的客户同样是开发者, 那么你可也可以使用 .NET Core 或者 .NET, 总之它们是跨平台, Windows 上也是可以运行的, 只不过普通用户可能不大会安装环境, 所以使用 .NET Framework 可以简化用户操作.)

在编写类库时, 尽可能多的支持多个目标, 一般至少包含 .NET Framework 和 .NET Standard 的目标.