---
title: "[踩坑记录] 某功能在C#7.3中不可用,请使用 8.0 或更高的语言版本 (通用解决方案)"
date: 2021-02-06T00:26:32+08:00
tags:
  - 踩坑记录
  - .NET
  - C#
---

使用自动修复或者手动编辑项目文件指定语言版本

<!--more-->

## 问题:

正如标题描述, 是某个语法在低版本中不受支持, 只需要升级到高版本即可.
## 步骤:
**> 第一种 :**
1. 使用快捷键 Alt + Enter 或点击黄色的的提示调出快速操作
    ![](https://img-blog.csdnimg.cn/20200917143210762.png)
2. 选择 将该项目升级为 C# 语言版本 "8.0"
   
    > 如果没有这一选项, 继续看第二种.

**> 第二种 :**

1. 打开项目所在目录并打开项目文件.
    ![](https://img-blog.csdnimg.cn/20210206001925422.png)
2. 在 PropertyGroup 节点下添加 LangVersion, 如图:
    ![](https://img-blog.csdnimg.cn/20210206002242856.png)
> 第二种其实就是通过更改 csproj 文件内容来置顶所使用的语言版本, 某些时候可能在这个文件中没有 LangVerison 节点, 就导致了快速操作中没有 "升级项目版本" 的选项, 这时就需要手动改文件了

<br/><br/><br/><br/>
如果没能解决你的问题, 麻烦在下面评论下, 这样我可以搜寻更多答案以修改这边文章.
如果解决了, 就点个赞吧 (卑微ovo)