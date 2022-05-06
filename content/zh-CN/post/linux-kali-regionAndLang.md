---
title: "[Linux] Kali Linux 新手引导 - 区域与语言配置"
date: 2020-12-07T16:50:05+08:00
tags:
  - Linux
  - Kali
  - 笔记
---

使用 tzselect 配置时区, 使用 sudo dpkg-reconfigure locales 配置语言

<!--more-->

> 我的 Kali
> 操作系统：Linux NullKali 5.9.0-kali2-amd64 #1 SMP Debian 5.9.6-1kali1 (2020-11-11) x86_64 GNU/Linux
> 桌面环境：Xfce Desktop Environment Version 4.14, destributed by Debian

## 配置区域

```shell
tzselect
# 在Shell中执行即可，tzselect = time zone select
```

## 配置语言

```shell
sudo dpkg-reconfigure locales
# 配置完后记得重启(reboot)
# 这条指令的意思应该是调整语言并安装相关包
# 配置完语言后，在登录页面的右上角可以快捷切换语言
```