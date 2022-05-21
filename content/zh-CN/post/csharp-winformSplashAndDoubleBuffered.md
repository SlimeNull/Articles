---
title: "C# WinForm Graphics 闪屏与双缓冲"
date: 2022-02-26T10:19:44+08:00
tags:
  - .NET
  - C#
  - WinForm
  - 笔记
---

简单介绍 C# WinForm 实现双缓冲的方法以及一些代码示例

<!--more-->

GDI+ 是 C# 常用的绘图库, .NET Framework 内置, 只需添加 System.Drawing 的引用即可, 而 .NET Core 也可以使用 System.Drawing.Common 的 nuget 包来安装此库.

## Graphics

一般网上常用的 Graphics 使用方法, 都会告诉你, 去订阅 Paint 事件, 然后再 Paint 事件的事件参数中获取 Graphics 对象, 进行绘制.

### 控件是如何绘制的?

Paint 事件是 WinForm 中, 每一个控件进行绘制时引发的事件, 例如控件添加到窗体上时, 会进行绘制, 当控件内容改变时, 会重绘, 或者当你的窗口大小调整并且边框影响到这个控件的时候, 控件也会重绘, 而只要是绘制, 就会引发 Paint 事件.

Paint 事件一般发生在控件自身的内容绘制完毕后, 例如反编译 Button 的基类 ButtonBase 可发现, OnPaint 方法中, 最先是绘制按钮的逻辑, 最后是引发 Paint 事件的逻辑.

所以, 如果用户订阅了 Paint 事件, 并在 Paint 事件中加入自己的绘图逻辑, 那么自己所绘制的内容就能持久的显示在控件上(因为控件每一次绘制都会引发 Paint).

> OnPaint 方法是一个可重写的, 定义在 Control 类中的方法, 他的默认实现是引发 Paint 事件, 在其他控件中, 一般会重写这个方法, 然后加入绘制自身的逻辑, 最后调用 base.OnPaint 引发 Paint 事件

### 闪屏问题是如何引起的?

事实上, Windows 的窗口绘制还分为 PaintBackground 和 Paint, 它们分别对应 WM_ERASEBKGND 和 WM_PAINT 消息, 作用是绘制(擦除)背景和绘制内容.

> WM_ERASEBKGND 和 WM_PAINT 是 Windows 消息, 消息处理是 Windows 窗口的核心组成部分, Windows 窗口的一切活动都依赖于能引发各种行为的 Windows 消息, 包括鼠标移动, 点击, 窗口大小调整, 布局改变等等

如果一个控件频繁的重绘, 那么这两个逻辑会不断的引发, 如果不擦除背景, 那么在第二次绘制的时候, 上一次的内容还存在于窗口, 那么就会出现显示上的一些错误. 而频繁的调用这两个方法, 就会造成内容擦除(绘制背景时所有内容被擦除), 内容绘制(绘制内容时, 新的内容显示出来).

所以, 内容的频繁擦除与绘制, 造成了视觉上的闪屏.

### AllPaintingInWmPaint

WinForm 中, 部分控件是不引发 PaintBackground 的, 这些控件将所有的绘图逻辑都在 Paint 中处理, 但是尽管如此, 闪屏问题其实还是存在的, 因为只不过是把擦除内容的逻辑放在了不同的地方, 背景擦除还是存在的.

### 脱离控件事件进行绘图

刚刚我们提到, 直接在 Paint 事件中加入绘图逻辑, 我们的绘图逻辑就会自动执行, 但是如果频繁的刷新, 就会有闪屏现象, 如何解决这个?

Windows 窗口本来就是分离了 PaintBackground 和 Paint 的, 所以, 这方面我们无法改变, 既然如此, 我们是否可以脱离控件的 Paint 事件, 而是交由我们自己去控制绘制逻辑呢? 没错, 可以.

每一个控件都有一个 CreateGraphics 方法, 调用这个方法, 我们就可以获取一个可以在该控件上进行绘图的 Graphics 对象, 同时你也可以使用 Graphics.FromHwnd(控件.Handle) 来获取一个控件的 Graphics, 两者是等价的.

既然有了 Graphics, 那么我们就可以进行绘制了, 可以尝试添加一个按钮, 然后在这个按钮的 Click 事件订阅者中添加在窗口中绘图的逻辑, 这样当点击按钮时, 你的绘图逻辑就被执行了.

### 使用计时器循环更新控件

现在, 我们可以主动向控件中绘制内容了, 不妨… 试试做一个图片序列播放器? 假设我一个很短的视频, 每一帧都转为了图片, 存在了一个目录中, 那么通过 Graphics, 我们也可以将他绘制出来.

通过计时器(Timer), 我们可以定时执行我们想执行的代码, 尝试做一个借助计时器的图片序列播放器吧

> Graphics.DrawImage 可以在绘图区域中绘制一个图片

### 避免绘制的内容被清除

即使我们现在已经可以主动向控件中绘制, 但是 WinForm 自身的绘制逻辑仍会对我们绘制的内容产生影响, 例如内容被 PaintBackground 清空, 解决方案就是, 我们可以在 Paint 事件中也使用我们的绘图逻辑.

为了方便, 我建议将绘图逻辑封装为方法, 然后使用的时候调用它, 在 Paint 事件中也是调用这个绘图逻辑.

### 主动绘制时引起的闪屏

假若我们绘制的不是图片, 而是一些线条和图形, 那么会如何? 如果这些都是会改变位置的, 在下一次绘制时, 和上一次是不同的, 那么, 该怎么办?

前面所说的图片序列播放器说的是绘制图片, 在绘制下一张图片的时候, 我们只需要把新的图片绘制上去, 之前的内容就被覆盖掉了, 固然不会有什么问题, 但是如果我们绘制的是可变化的几何, 事情就不一样了.

因为绘制的内容会变动, 所以还用这种方法的话, 那么在第二次绘制的时候, 第一次绘制的内容还在窗口上, 就产生了重合… 我们应该在第二次绘制之前, 先清空我们绘制的内容, 对吧? 等等, 有些熟悉… 这不就是 WinForm 引起闪屏的原因??? 

不慌, 接着往下看.

## 双缓冲

既然清空内容然后绘制内容会引起闪屏, 那我们干脆不清空, 直接把新的内容覆盖上去, 岂不美哉? 但是… 新的内容从哪来? 答案就是双缓冲.

双缓冲意思就是在后台分配一个绘图区域, 绘制的时候在这个后台的绘图区域上绘制, 绘制完毕后再拷贝到前台界面上, 因为期间涉及到前台的界面和后台的绘图区, 所以被称为双缓冲.

> WinForm 虽然自带双缓冲, 但是对于我们的绘制不会起到任何作用, 即便我们通过更改窗口的 DoubleBuffered 属性

### Bitmap

如果你搜索双缓冲的话, 我相信, 大部分答案都是使用 Bitmap, 虽然这个方法并不是最好的方法, 但是还是介绍一下罢.

Bitmap, 位图, 我们可以创建一个 Bitmap, 大小和我们的控件相同, 然后在绘制的时候, 在这个 Bitmap 上绘制, 绘制完毕之后, 把这个 Bitmap 通过 DrawImage 的形式将他绘制到控件上, 覆盖原有内容, 这样就避免了闪屏问题.

> Graphics.FromImage 可以通过一个图像来创建 Graphics 对象, 使用该对象将在对应图片上绘图.

> 使用 Bitmap 的话, 如果缓冲区的大小不改变, 也没有什么不妥, 但是如果你的绘制区域可能频繁的调整大小, 那么你的内存可能会哭唧唧


### BufferedGraphics

BufferedGraphics 正如其名, 是缓冲了的 Graphics, 其官方介绍是这么介绍的: '为双缓冲提供图形缓冲区'.

> 官方文档 [BufferedGraphics 类 (System.Drawing) | Microsoft Docs](https://docs.microsoft.com/zh-cn/dotnet/api/system.drawing.bufferedgraphics?view=dotnet-plat-ext-6.0)

BufferedGraphics类没有公共构造函数, 并且必须 BufferedGraphicsContext 使用其方法为应用程序域创建 Allocate. 可以使用 BufferedGraphicsManager 从静态属性 Current 中检索当前应用程序域的 BufferedGraphicsContext.

```csharp
// 要进行操作的 Graphics, 例如控件 Graphics
Graphics g;
// 要分配的 BufferedGraphics 大小
int Width, Height;

BufferedGraphicsContext context = BufferedGraphicsManager.Current;
BufferedGraphics bufferedG = context.Allocate(g, new Rectangle(0, 0, Width, Height));

// 此时, 创建完毕的 bufferedG 可供使用
```

使用 BufferedGraphics 的 Graphics 获取用来绘图的缓冲区, 绘制完毕后使用其 Render 方法将内容输出到目标 Graphics. 此时, 缓冲区内的内容就会一次性输出到目标 Grahpics.

```csharp
// 已经分配好的 BufferedGraphics
BufferedGraphics bufferedG;

Graphics g = bufferedG.Graphics;
g.FillRectangle(Brushes.Purple, new Rectangle(50, 50, 200, 200));
bufferedG.Render();
```

> 另外, BufferedGraphics 的核心是 使用内存 DC, 并且使用 Bitblt 直接拷贝绘图区域, 比 DrawImage 快些, 这也是推荐使用 BufferedGraphics 的原因

## 拓展知识

### 重写 OnPaintBackground

OnPaintBackground 是 Control 的一个保护的, 可重写的方法, 其内部逻辑是对控件背景进行绘制, 除此之外, 他还支持一些简单的透明背景. 如果我们既使用双缓冲, 又在 OnPaintBackground 书写我们的绘图逻辑, 那么闪屏问题将永远不会出现.

因为闪屏问题就是因为绘制背景时内容被擦除, 可是绘制背景的就是我们的代码逻辑, 而我们所绘制的背景正是所需要绘制的内容, 于是内容也将不可能被清除掉.

> OnPaintBackground 只会进行背景绘制, 不会引发任何事件, 所以在重写的方法内, 我们可以放心的把 base.OnPaintBackground(pevent) 删除掉

### 保证缓冲区与控件尺寸一致

你可以在控件尺寸更改时, 重新分配缓冲区, 使用 SizeChanged 事件, 或者干脆重写 OnSizeChanged, 在 base.OnSizeChanged(e) 之前就把缓冲区重新分配好, 这样也方便管理些

## 代码示例

简单使用 BufferedGraphics 封装一个自带 BufferedGraphics 属性的控件(继承 Control), DoubleBufferedControlBase
```csharp
using System;
using System.Drawing;
using System.Windows.Forms;

namespace NullLib.TickAnimation.WinForm
{
    public abstract class DoubleBufferedControlBase : Control
    {
        readonly BufferedGraphicsContext context;
        private BufferedGraphics bufferedGraphics;
        
        // 缓冲区保护且只读
        protected BufferedGraphics BufferedGraphics { get => bufferedGraphics; }

        public DoubleBufferedControlBase() : base()
        {
            // 创建控件时即分配缓冲区
            context = BufferedGraphicsManager.Current;
            bufferedGraphics = context.Allocate(Graphics.FromHwnd(Handle), new Rectangle(Point.Empty, Size));
        }

        // 当改变尺寸, 重新分配缓冲区
        protected override void OnSizeChanged(EventArgs e)
        {
            if (bufferedGraphics != null)
                bufferedGraphics.Dispose();
            bufferedGraphics = context.Allocate(Graphics.FromHwnd(Handle), new Rectangle(Point.Empty, Size));
            base.OnSizeChanged(e);
        }
    }
}

```

使用双缓冲绘制的三阶贝塞尔曲线编辑器控件 CubicBezierView
```csharp
using System;
using System.Drawing;
using System.Windows.Forms;

namespace NullLib.TickAnimation.WinForm
{
    // 贝塞尔曲线编辑器抽象基类
    public abstract class BezierViewBase : DoubleBufferedControlBase
    {
        public bool ControlHandleEnabled
        {
            get => controlHandleEnabled;
            set
            {
                if (controlHandleEnabled == value)
                    return;
                controlHandleEnabled = value;
                Invalidate();  // 当是否允许使用控制手柄值改变时, 立即重绘 (此操作同时也会在窗体设计器中显现出)
            }
        }
        public int ControlHandleSize { get; set; } = 20;                                                   // 控制点手柄的大小
        public Brush ControlHandleBrush { get; set; } = new SolidBrush(Color.FromArgb(196, 125, 208));     // 控制点手柄所用笔刷

        public Pen ControlHandleStickPen { get; set; } = new Pen(Color.FromArgb(196, 125, 208), 3);        // 控制点手柄与其他点连线的笔
        public Pen CurvePen { get; set; } = new Pen(Color.Black, 5);                                       // 画曲线所用笔

        private bool controlHandleEnabled;

        protected override void OnSizeChanged(EventArgs e)
        {
            base.OnSizeChanged(e);
            Invalidate();           // 当尺寸改变时, 应立即重绘以适应改动 (因为图形是适配控件大小的)
        }

        protected PointF GetControlPointFromPixelPoint(Point p)                 // 将控制点坐标转换为屏幕坐标
        {
            return new PointF(p.X / (float)Width, 1 - p.Y / (float)Height);
        }

        protected Point GetPixelPointFromControlPoint(PointF p)                 // 将屏幕坐标转换为控制点坐标
        {
            return new Point((int)(p.X * Width), Height - (int)(p.Y * Height));
        }

        protected Rectangle GetRectangleFromCenterPoint(Point p, int r)   // 通过一个中心点, 半径, 计算一个圆的外界矩形 (用来绕某点填充圆形)
        {
            return new Rectangle(p.X - r, p.Y - r, r * 2 + 1, r * 2 + 1);
        }
    }
    
    public class CubicBezierView : BezierViewBase
    {
        public PointF ControlPoint1 { get; set; } = new PointF(0.25f, 0.75f);
        public PointF ControlPoint2 { get; set; } = new PointF(0.75f, 0.25f);

        void PaintCore()
        {
            Graphics g = BufferedGraphics.Graphics;
            g.Clear(BackColor);
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            Point startPoint = new Point(0, Height - 1);
            Point endPoint = new Point(Width - 1, 0);
            Point cp1 = GetPixelPointFromControlPoint(ControlPoint1);  // 获取控制点1的屏幕坐标
            Point cp2 = GetPixelPointFromControlPoint(ControlPoint2);  // 获取控制点2的屏幕坐标

            if (ControlHandleEnabled)
            {
                g.DrawLine(ControlHandleStickPen, startPoint, cp1);
                g.DrawLine(ControlHandleStickPen, endPoint, cp2);

                g.DrawBezier(CurvePen, startPoint, cp1, cp2, endPoint);

                Rectangle
                    handleRect1 = GetRectangleFromCenterPoint(cp1, ControlHandleSize / 2),
                    handleRect2 = GetRectangleFromCenterPoint(cp2, ControlHandleSize / 2);
                g.FillEllipse(ControlHandleBrush, handleRect1);
                g.FillEllipse(ControlHandleBrush, handleRect2);
            }
            else
            {
                g.DrawBezier(CurvePen, startPoint, cp1, cp2, endPoint);
            }

            BufferedGraphics.Render();
        }

        protected override void OnPaintBackground(PaintEventArgs e)
        {
            PaintCore();    // 将背景绘制的逻辑改为自己的绘图逻辑
        }

        bool cp1Captured, cp2Captured;
        protected override void OnMouseDown(MouseEventArgs e)   // 判断是否点击了手柄
        {
            if (ControlHandleEnabled)
            {
                Point cp1 = GetPixelPointFromControlPoint(ControlPoint1);
                Point cp2 = GetPixelPointFromControlPoint(ControlPoint2);
                Rectangle
                    handleRect1 = GetRectangleFromCenterPoint(cp1, ControlHandleSize / 2),
                    handleRect2 = GetRectangleFromCenterPoint(cp2, ControlHandleSize / 2);
                if (handleRect1.Contains(e.Location))
                {
                    cp1Captured = true;
                }
                else if (handleRect2.Contains(e.Location))
                {
                    cp2Captured = true;
                }
            }

            base.OnMouseDown(e);
        }

        protected override void OnMouseMove(MouseEventArgs e)
        {
            if (ControlHandleEnabled)            // 如果开启了控制手柄
            {
                if (ClientRectangle.Contains(e.Location))   // 如果鼠标还在控件范围内
                {
                    if (cp1Captured)     // 如果在编辑第一个手柄
                    {
                        ControlPoint1 = GetControlPointFromPixelPoint(e.Location);   // 设置控制点位置
                        Invalidate();
                    }
                    else if (cp2Captured)
                    {
                        ControlPoint2 = GetControlPointFromPixelPoint(e.Location);
                        Invalidate();
                    }
                }
            }

            base.OnMouseMove(e);
        }

        protected override void OnMouseUp(MouseEventArgs e)
        {
            cp1Captured = cp2Captured = false;  // 清除手柄调整状态

            base.OnMouseUp(e);
        }
    }
}

```