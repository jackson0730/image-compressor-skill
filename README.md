# Image Compressor Skill

本地网页图片压缩工具，苹果风格 UI，纯浏览器端处理，无需上传到服务器。

## 功能

- 支持 PNG、JPG 拖拽或点击上传
- 实时对比原图 vs 压缩后效果及文件大小
- 质量滑块（1-100%）自由调节
- 一键下载压缩结果

## 使用方式

### 方式一：启动本地服务（推荐）

```bash
python3 serve.py
```

自动打开浏览器，访问 http://localhost:8765

### 方式二：直接打开

```bash
open index.html
```

## 作为 OpenClaw Skill 安装

```bash
clawhub install jackson0730/image-compressor-skill
```

安装后，对 agent 说"帮我压缩图片"即可触发。

## 技术实现

- 原生 HTML5 + CSS3 + JavaScript，零依赖
- FileReader API 实现图片读取
- Canvas API 实现压缩（adjustable JPEG quality）
- 启动服务仅需 Python 3 标准库
