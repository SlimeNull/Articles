---
title: '[C#] 排序算法: 超高速根据字符串长度排序的算法'
date: 2020-06-26T02:04:05+08:00
tags:
  - .NET
  - C#
  - 笔记
  - 算法
---

使用 Dictionary 和 List, 桶排序实现超高速根据字符串长度排序字符串数组

<!--more-->

## 1. 你需要知道这些:

##### 代码适用于:

0. 适用于字符串数组的元素长度变化量较小的, 比如字符串的长度普遍在1~2000, 那么此时, 这个算法将有超高的性能, 测试结果是 10万条数据排序所需时间为91ms(你没看错).

##### 应用场景:

0. 你有一个超级长的文本文件, 这里面每一行都是一条数据, 例如这些数据是用爬虫获取的搜索关键字, 你现在需要将它们排序, 别犹豫, 我认为这个算法非常适合你.

##### 局限性

0. 字符串数组的元素长度变化量越大, 该算法效率可能会越低,因为里面包含了对字符串长度变化量排序的过程,这个过程是使用的选择排序法。（选择排序法的所需时间与数据长度不成正比,不多赘述）

## 2.算法的主要内容

##### 主要原理:

1. 定义一个字典, 键是int, 值是可变的字符串列表, 定义一个可变的字符串列表作为存储结果的容器
2. 循环源字符串数组, 将一切可能的长度作为int, 一个新的字符串列表作为值, 添加到上面所说的字典里面
3. 第二次循环源字符串数组, 将迭代到的字符串的长度作为键, 在字典中键所对应的字符串列表中添加这个字符串
4. 排序字典的键, 循环排序后的所有键, 将键对应的字符串列表的每一个字符串添加到结果中
5. 排序结束

##### 示例代码:

```csharp
// 这是C#代码
// Dictionary 与 List 位于 System.Collections.Generic 命名空间下
string[] StringSort(string[] source)
{
    int[] sortKeys(int[] src)    // 这里是用于排序字典的键的
    {
        int most;
        int mostIndex = 0;
        int temp;
        if (src.Length > 1)
        {
            for (int i = 1; i < src.Length; i++)
            {
                most = src[i];
                for (int j = i; j < src.Length; j++)
                {
                    if (src[j] < most)
                    {
                        most = src[j];
                        mostIndex = j;
                    }
                }
                if (most < src[i - 1])
                {
                    src[mostIndex] = src[i - 1];
                    src[i - 1] = most;
                }
            }
        }
        return src;
    }
    Dictionary<int, List<string>> firstSortedString = new Dictionary<int, List<string>>();
    List<string> result = new List<string>();
    foreach (string i in source)
    {
        if (!firstSortedString.ContainsKey(i.Length))
        {
            firstSortedString.Add(i.Length, new List<string>());
        }
    }
    foreach (string i in source)
    {
        firstSortedString[i.Length].Add(i);
    }
    foreach (int i in sortKeys(firstSortedString.Keys.ToArray()))
    {
        foreach (string j in firstSortedString[i])
        {
            result.Add(j);
        }
    }
    return result.ToArray();
}
```

> 这个算法只是偶然间想到的, 不喜勿喷