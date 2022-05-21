---
title: '[Web] 25行 CSS 代码实现轮播图'
date: 2021-05-01
tags:
  - HTML
  - CSS
  - JS
  - 笔记
---

不是最漂亮但是一定简单的通用轮播图示例

<!--more-->

## 效果

![c7WUjfKexQ](/slimenull/storage/raw/master/img/blogs/carousel-preview.gif)

准备好的几张图片, 它们的路径是: "img/1.jpg", "img/2.jpg", "img/3.jpg", "img/4.jpg", "img/5.jpg", "img/6.jpg"

## 代码

最基本的 HTML 代码:

```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <title>Test</title>
  <link rel="stylesheet" href="css/index.css" />   <!--引入样式表-->
  <script src="js/index.js"></script>              <!--引入JS脚本, 脚本用来切换图-->
</head>

<body>
  <div id="test" class="slider">
    <img id="img1" src="img/1.jpg" class="current">
    <img id="img2" src="img/2.jpg">
    <img id="img3" src="img/3.jpg">
  </div>
  <button onclick="setCurrent(0)">1</button>      <!--在这里, onClick调用的是用于设置当前图片的方法, 传入参数为图片节点的索引-->
  <button onclick="setCurrent(1)">2</button>
  <button onclick="setCurrent(2)">3</button>
  <button onclick="setCurrent(3)">4</button>
  <button onclick="setCurrent(4)">5</button>
  <button onclick="setCurrent(5)">6</button>
</body>

</html>
```

引入的样式表:

```css
.slider {                 /* 指定轮播图容器尺寸, 相对定位, 隐藏溢出内容 */
    width: 750px;
    height: 450px;
    position: relative;
    overflow: hidden;
}
.slider img {             /* 指定每一个图片的尺寸, 过渡时间, 绝对定位 */
    width: 100%;
    height: 100%;
    transition: all 0.5s;
    position: absolute;
}
.slider img {                           /* 指定所有图片水平位移-100% */
    transform: translateX(-100%);
}
.slider img.current {                   /* 指定带有current类的图片不进行水平移动 */
    transform: translateX(0);
}
.slider img.current~img{                /* 指定位于带有current类的图片之后的所有图片水平位移为100% */
    transform: translateX(100%);
}
.slider img.current,                    /* 指定带有current或last类的图片置顶 */
.slider img.last{
    z-index: 999;
}
```

引入的JavaScript:

```js
function getImages() {
    return document.getElementById("test").querySelectorAll("img");       // 搜找该页面下轮播图容器中的所有img
}
function getCurrent() {
    return document.getElementById("test").querySelector("img.current");  // 搜找该页面下轮播图容器中当前展示的img
}
function setCurrent(index) {
    var imgs = getImages();
    var cur = getCurrent();
    imgs.forEach(v => v.className = "");   // 清空所有图片的类名
    cur.className = "last";                // 设置当前展示的图片的类名为 "last", 意为: "上一次展示的图片"
    imgs[index].className = "current";     // 设置要设置的图片的类名为 "current"
}
```

## 原理

图片集为一个序列, 当前展示的图片在中间, 展示图片之前的图片则是在左边, 而之后的图片则是在右边.

任意设置一个图片为当前展示的图片(即设置类名为current), 那么该图片将移动到中间. 而其它的图片, 自然也会移动到它两边.

由于滑动时, 需要显示将要展示的图片, 以及将要隐藏的图片, 所以这两张图片需要置顶, 否则, 进行多张图片的切换时, 将由于默认层级关系而导致异常, 故设置 .current 与 .last 的 z-index 为 999.
