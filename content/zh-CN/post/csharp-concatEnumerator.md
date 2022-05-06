---
title: "[C#] IEnumerable拼接! 将枚举器串起来~"
date: 2021-02-19T07:07:41+08:00
draft: true
---

通过 yield 可以实现很多骚操作, 例如自己定义拓展函数以支持将可迭代对象连接起来

<!--more-->

本来以为 IEnumerable 不能拼接, 就自己实现了一个, 结果发现 Linq 是提供了一个 Concat 函数的. 不过, 也没必要删了. 留着做记录也不错

```csharp
using System;
using System.Collections;
using System.Collections.Generic;

namespace NullLib.Iterator
{
    public static class NIterator
    {
        public static IEnumerable Concat(this IEnumerable iterator1, IEnumerable iterator2)
        {
            foreach (var i in iterator1)
                yield return i;
            foreach (var i in iterator2)
                yield return i;
        }
        public static IEnumerable<T> Concat<T>(this IEnumerable<T> iterator1, IEnumerable<T> iterator2)
        {
            foreach (var i in iterator1)
                yield return i;
            foreach (var i in iterator2)
                yield return i;
        }
        public static IEnumerable Concat(this IEnumerable iterator1, params IEnumerable[] iterator2)
        {
            foreach (var i in iterator1)
                yield return i;
            foreach (var i in iterator2)
                foreach (var j in i)
                    yield return j;
        }
        public static IEnumerable<T> Concat<T>(this IEnumerable<T> iterator1, params IEnumerable<T>[] iterator2)
        {
            foreach (var i in iterator1)
                yield return i;
            foreach (var i in iterator2)
                foreach (var j in i)
                    yield return j;
        }
        public static IEnumerable Concat(params IEnumerable[] iterators)
        {
            foreach (var i in iterators)
                foreach (var j in i)
                    yield return j;
        }
        public static IEnumerable<T> Concat<T>(params IEnumerable<T>[] iterators)
        {
            foreach (var i in iterators)
                foreach (var j in i)
                    yield return j;
        }
    }
}
```