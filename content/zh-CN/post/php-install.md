---
title: PHP 的安装概述
date: 2022-02-08
tags:
  - PHP
  - 教程
  - 笔记
---

基本介绍 PHP 在 Windows 中的安装, 配置, 以及基本使用

<!--more-->

1. 下载 php 并解压到任意安装目录
2. 设置环境变量 PHPRC 为安装目录

## 下载
在 Windows 中, php 是不需要安装的, 直接下载并解压到任意安装目录即可

## 配置文件
php.ini 是 php 的配置文件, 默认 php 会在系统中寻找, C:\Windows, 但是通过设置 PHPRC 环境变量, 可以使 php 从指定的目录加载 php 文件
默认 php.ini 文件是不存在的, 但是 php 提供了默认的 php.ini-development 和 php.ini-production, 它们分别是用于开发和发布的 php 配置文件, 用户只需要拷贝它们并重命名为 php.ini 即可直接使用

php.ini 内指定了哪些插件是启用的, 默认提供的配置文件中已经写好了这些, 并注释掉了. 用户只需要取消注释对应内容即可.

事实上, 如果 php 不加载配置文件, 也是可以运行的

## 环境变量
PHPRC 环境变量的值需要是 php 的安装目录, 该目录下应存在 php 的可执行文件以及 php 的配置文件 php.ini (如果没有, 则在系统中寻找)
