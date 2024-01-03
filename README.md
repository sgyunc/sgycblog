# sgycblog
# 一个简单的静态个人博客
# （本项目已经停止更新，剩下的交给各位有能力的大牛了)
# qq交流群279991611


# 项目文档
## 项目概述
### 这个项目是一个简单的静态博客生成器，能够将 Markdown 文件转换为包含标题、日期和内容的 HTML 文件。

1. 安装
```
在Windows上安装Python 3：
访问Python官方网站：Python Downloads。
在页面上找到最新版本的Python 3，点击下载。
打开下载的安装程序（通常是一个.exe文件），勾选 "Add Python 3.x to PATH" 选项，然后点击 "Install Now"。
完成安装过程。
```
2. 克隆项目：

```
git clone https://github.com/sgyunc/sgycblog.git
cd sgycblog
```
3. 安装依赖项：
```
pip install -r requirements.txt
```
4. 使用
配置：

在项目根目录创建一个 set.yml 文件，并配置网站的元信息，例如标题、关键词、页脚等。
将 Markdown 格式的博客文章放置在 posts_folder 文件夹中。
生成网站：

```
python generate.py
```
执行此命令将生成网站的 HTML 文件，并将其存储在 public 文件夹中。

查看网站：
打开浏览器，导航到 public/index.html 文件，即可查看生成的网站。
```
set.yml 配置示例
yaml

title: Your Blog Title
header_title: Your Blog Header Title
keywords: technology, coding, blog
footer_text: Your Blog Footer Text
footer_by: Your Name
nav:
  - name: Home
    link: index.html
  - name: Categories
    link: categories.html
  - name: Archive
    link: archive.html
meta_tags:
  - name: description
    content: Your blog description goes here
css:
  - ./ass/css/style.css
js:
  - ./ass/js/Search.js
links:
  - name: Friend 1
    link: https://friend1-blog.com/
    avatar: https://friend1-blog.com/avatar.png
    descr: A brief description about Friend 1's blog


```
依赖项
Python 3.x
Markdown
PyYAML

附加说明

5. 请确保 Markdown 文件中包含正确的标题和日期信息。
```
title: 测试5
category: text
date: 2024-01-15

helloworld
```
修改 set.yml 文件以适应你的网站需求。
若要添加新的 CSS 或 JavaScript 文件，请在相应的部分中更新 set.yml。
示例
一个基于此项目生成的示例网站：nav.sgyunc.com

请记得将以上信息替换为实际项目的内容，并根据实际情况添加其他必要的说明。这只是一个简单的文档示例，实际文档需要更详细地解释各个组成部分、配置选项以及常见问题的解决方案。
