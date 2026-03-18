---
name: image-compressor
description: Launch a local web-based image compression tool. Supports PNG/JPG, real-time preview, adjustable quality slider, and one-click download. Trigger on "压缩图片", "图片压缩", "compress image", "图片太大", "reduce image size".
homepage: https://github.com/jackson0730/image-compressor-skill
metadata: {"clawdbot":{"emoji":"🖼️","requires":{"bins":["python3"]}}}
---

# Image Compressor

本地网页图片压缩工具，苹果风格 UI，无需上传到服务器，纯浏览器端处理。

## 启动

```bash
python3 {baseDir}/serve.py
```

启动后自动打开浏览器，访问 http://localhost:8765

## 功能

- 支持 PNG、JPG 拖拽或点击上传
- 实时对比原图 vs 压缩后效果
- 显示压缩前后文件大小
- 质量滑块（1-100%）自由调节
- 一键下载压缩结果

## 手动打开

如果不想启动服务，也可以直接用浏览器打开：

```bash
open {baseDir}/index.html
```
