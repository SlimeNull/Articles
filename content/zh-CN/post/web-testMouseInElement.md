---
title: '[Web] JS MouseDown 事件与判断鼠标是否在某个元素中'
date: 2021-05-26
tags: 
  - Web
  - JavaScript
---

监听全局鼠标按下事件, 并通过判断对应元素是否包含 e.target 来实现检查鼠标是否在某个元素内

<!--more-->

## 创建事件监听器:

对于创建全局的事件监听器(EventListener), 我们可以使用 document 对象.

```js
document.addEventListener("mousedown", function(e){
    // e 参数为鼠标按下的事件, 具体有什么成员, 可以在浏览器调试器里面直接 console.log(e) 查看
    // 这里写逻辑代码
});
```

## 判断鼠标是否位于某个元素上:

对于事件监听器中的事件参数, 有一个 path 包含了鼠标事件的路径, 第一个元素为点击的最内层元素, 最后一个元素则是 window, 倒数第二个是 document. 并且, 还有一个成员 target 表示触发事件的最内层元素, 与 path 的第一个元素相同.

一个 DOM 节点, 可以通过其 contains 方法来判断它是否包含一个元素, 也就是判断这个元素是否位于它自己内部, 如果这个元素是它自己, 同样是返回 true

```js
document.addEventListener("mousedown", function(e){
    // 例如我们要判断鼠标是否点击了  div#mydiv
    let ele = document.querySelector("div#mydiv");
    let inele = ele.contains(e.target);
    console.log(inele ? "点击了 div#mydiv" : "没有点击 div#mydiv");
});
```

#### 另一种方式

还有另外一种比较麻烦的方法, 就是去判断这个鼠标的位置是否在元素显示区域的内部, 这个的话, 我可以明确的告诉你, 很多时候行不通... 网上虽然有很多示例代码, 但是这种方法有很大局限性, 例如你是一个 fixed 元素套了一个 absolute 元素, 你还得去进行大量的运算, 有时候还根本算不出来, 所以使用上面的通过 DOM 节点去判断是否包含, 最为妥当