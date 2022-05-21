---
title: "C++ 获取键盘状态与操作窗口"
date: 2022-02-08
tags:
  - C++
  - Win32
  - 笔记
  - 教程
---

通过一个简单的快捷键移动窗口项目介绍 C++ 获取键盘状态与操作窗口的方式

<!--more-->

使用 Win API, 可以非常简单的获取当前键盘的按下状态, 或者对窗口的移动操作. 接下来是一个简单的小程序, 程序判断快捷键是否按下, 如果按下, 则执行移动窗口的操作.

> 下面的内容是完整的程序代码, 拼合起来是可执行的

## include
使用标准输入输出流需要包含 iostream
使用 Win API 需要包含 Windows.h
```cpp
#include<iostream>
#include<Windows.h>
```

> cmdline.h 是一个简易的命令行解析库, 其 GitHub 项目地址为: [github.com/tanakh/cmdline](https://github.com/tanakh/cmdline)
> 在本文章末同时也会附上一份 Windows 可用的 cmdline.h 源文件

## 变量与常量定义
```cpp
const char APPNAME[] = "Null.WindowMoving.Cpp";        // 应用程序名
const wchar_t APPNAME_W[] = L"Null.WindowMoving.Cpp";  // 对应宽字符串

bool hotkeyDown = false;                           // 存储热键是否按下

HWND currentWindow;                                // 存储当前活动窗口
int windowStartPointX, windowStartPointY;          // 窗口的起始位置
int mouseStartPointX, mouseStartPointY;            // 鼠标的起始位置
1
HANDLE app_mutex;                                  // 用于实现单例的 Mutex 句柄
```
## 简易日志

在窗口简单的输出一些内容.

```cpp
void logMsg(std::string msg)
{
	SYSTEMTIME systm;      // 系统时间
	GetLocalTime(&systm);  // 获取系统时间

    char szCurrentDateTime[] = "0000-00-00 00:00.00";   // 定义字符串
	sprintf_s(szCurrentDateTime, "%4d-%2d-%2d %2d:%2d.%2d",   // 格式化时间
		systm.wYear, systm.wMonth, systm.wDay,
		systm.wHour, systm.wMinute, systm.wSecond);

	std::cout << szCurrentDateTime << " @ " << msg << std::endl;    // 输出内容
}
```

## 程序初始化

Mutex 可以用来实现进程单例, 使用 CreateMutex 函数创建一个命名了的 Mutex, 并使用 GetLastError 来检查是否已经存在同名 Mutex, 若存在则表示已经运行了一个进程, 当前进程退出即可.

```cpp
/// <summary>
/// 初始化程序
/// </summary>
/// <returns>是否初始化成功</returns>
bool initApp(int argc, char* argv[])
{
	std::cout << "Null.WindowMoving" << std::endl;

	app_mutex = CreateMutex(NULL, true, APPNAME_W);   // 尝试创建 Mutex
	if (GetLastError() == ERROR_ALREADY_EXISTS)       // 如果已经存在 Mutex, 即已经有程序存在
	{
		logMsg("instance is already running");
		return false;
	}

	return true;
}
```

## 判断快捷键

通过 GetAsyncKeyState 可以获取一个按键的物理状态, 通过这个来判断快捷键是否按下.

```cpp
void testHostkey()
{
	bool valueBefore = hotkeyDown;   // 保存旧值
	hotkeyDown = (GetAsyncKeyState(VK_LWIN) & GetAsyncKeyState(VK_LSHIFT)) != 0;   // 判断是否同时按下左 Win 和左 Shift

	if (hotkeyDown != valueBefore)   // 如果值变更了
	{
		if (hotkeyDown)     // 如果按下了快捷键
		{
			currentWindow = GetForegroundWindow();   // 获取当前前台窗口

			POINT mouseP;  // 鼠标坐标
			RECT rect;     // 窗口边界
			if (GetCursorPos(&mouseP) && GetWindowRect(currentWindow, &rect))   // 获取鼠标坐标及窗口边界
			{
				mouseStartPointX = mouseP.x;      // 保存获取的信息
				mouseStartPointY = mouseP.y;
				windowStartPointX = rect.left;
				windowStartPointY = rect.top;

				logMsg("hotkey down");
				
			}
			else
			{
				hotkeyDown = false;               // 获取失败, 则记为快捷键未按下
				logMsg("hotkey down, but failed to get cursor position or window rect");
			}
		}
		else
		{
			logMsg("hotkey up");
		}
	}
}
```

## 窗口移动

SetWindowPos 可以用来设置窗口的位置, 并且通过 flags 的指定来规定他的具体行为.

```cpp
void processWindowMoving()
{
	if (hotkeyDown)  // 如果按下快捷键
	{
		POINT currentMousePoint;                                // 当前鼠标坐标
		GetCursorPos(&currentMousePoint);                       // 获取当前鼠标坐标
		int offsetX = currentMousePoint.x - mouseStartPointX,   // 计算鼠标相对初始位置的偏移量
			offsetY = currentMousePoint.y - mouseStartPointY;
		if (GetForegroundWindow() == currentWindow)
		{
			POINT newWindowPoint = { windowStartPointX + offsetX, windowStartPointY + offsetY };        // 计算新的窗口位置
			SetWindowPos(currentWindow, 0,
				windowStartPointX + offsetX,
				windowStartPointY + offsetY,
				-1, -1,
				SWP_NOSIZE | SWP_NOOWNERZORDER | SWP_DEFERERASE | SWP_NOREDRAW | SWP_NOSENDCHANGING);   // 设置窗口位置
		}
		else
		{
			hotkeyDown = false;
			logMsg("foreground window changed, hotkeyDown changed to 'false'");
		}
	}
}
```

## 循环处理

程序需要不断的判断快捷键, 并且移动窗口, 所以需要有一个主循环

```cpp
void loopProcessing()
{
	while (true)   // 循环判断快捷键以及处理窗口移动
	{
		testHostkey();
		processWindowMoving();
		Sleep(1);   // sleep 1 防止 CPU 占用过高
	}
}
```

## 入口点

入口点中, 初始化程序, 如果初始化失败, 则返回 -1, 如果成功就执行主循环.

```cpp
int main(int argc, char* argv[])
{
	if (!initApp(argc, argv))
		return -1;
	
	loopProcessing();
}
```