---
title: "[C#] 循环所有可能的字符"
date: 2020-10-26T15:59:44+08:00
tags:
  - .NET
  - C#
  - 笔记
---

通过 char.MaxValue 来作为循环结尾, 将int强制转换为char, 即可

<!--more-->

> ~~之前自己搜索这个内容, 发现国内没有, 所以写了这个文章供参考~~ 

```csharp
for (int i = 0; i <= char.MaxValue; i++)
{
    // 此处放处理语句, (char)i 即为当前字符
}
```
 