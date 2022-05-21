---
title: 'FFmpeg 使用概述'
date: 2020-02-14
draft: true
---

通过简单的格式转换以及视频压缩示例讲解 FFmpeg 基本使用

<!--more-->

## 命令格式
使用 `ffmpeg --help` 可以查看 ffmpeg 的详细帮助手册, 其中包含对于视频, 音频, 以及其他的选项, 使用这些, 可以做到对多媒体文件进行压缩, 剪切, 裁切等操作

ffmpeg 的标准命令格式是:
```bash
ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}
ffmpeg [选项] [[输入文件选项] -i 输入文件]... {[输出文件选项] 输出文件}...
```

其中, options, infile 是可选项, outfile 是必选项, 当指定定了 infile, 则可以指定 infile options; outfile options 也是可选项.
infile 可以指定多个, 对应的, outfile 也可以指定多个, 但是 infile 和 outfile 一定是对应的. infile options 和 outfile options 分别位于 infile 和 outfile 的前方, 如果位置指定错误, 那么运行起来也是不同的.

## 格式转换
使用 `ffmpeg -i 输入文件 输出文件` 可以直接将一个文件转换为另一个文件, ffmpeg 会自动识别文件后缀, 并应用对应的格式.

ffmpeg 可转换的格式非常多, 视频, 音频, 以及常用的图片格式, 例如我们想要讲一个 test.png 转为 webp 格式, 那么可以使用以下的代码
```bash
ffmpeg -i test.png test.webp
```

## 压缩内容
对于视频, 如果要压缩, 那么可操作的方式是非常多的, 例如减小帧率, 减小分辨率, 减小比特率, 这些都是可以通过 ffmpeg 的参数直接达到的.

```bash
-r rate             设置帧率 (赫兹值, 分数或简写)
-s size             设置帧尺寸 (宽x高, 或缩写)
-ab bitrate         音频比特率 (请使用 -b:a)
-b bitrate          视频比特率 (请使用 -b:v)
```

例如将一个 test.mp4 视频压缩至 30hz刷新率, 1280x720分辨率, 1mb视频比特率, 128kb音频比特率, 可以使用以下指令
```bash
ffmpeg -i test.mp4 -r 30 -s 1280x720 -b:v 1m -b:a 128k test_compressed.mp4
```



