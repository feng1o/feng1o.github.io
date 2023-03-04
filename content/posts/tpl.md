---
# 越小权重越高,首页在前
weight: 100
title: "tpl - md模板文件"
date: 2020-03-06T21:40:32+08:00
lastmod: 2020-03-06T21:40:32+08:00
draft: false
author: "feng1o"
authorLink: "https://feng1o.github.io"
description: "Hugo - **模板** ."

# 图片
featuredImage: images/tpl-featured.png
#featuredImagePreview: /featuredImage/excel-featured-image.jpg

#resources:
#- name: "featured-image"
#  src: "./apple-touch-icon.png"
#resources:
#- name: "/images/featured-image"
#  src: "/images/featured-image.jpg" #这个不行

# tag只是方便查找
tags: ["tpl", "模板"]
# 分类更详细,会根据分类分组文章
categories: ["tpl"]

lightgallery: true 

toc:
  enable: true
  auto: true 
---

Hugo more- **模板** 使用 摘要-description, more的优先级更高.
<!--more-->

<!-- 注释,此处是style -->
<style>
h3,h1 {
background : lightgray;
}

h3:hover {
color : red;
}
</style>


### 1.clone主题并更新配置
```
 1.markdown

```

### 2.link
> 引用,link 
<a href=https://hugoloveit.com/zh-cn/theme-documentation-basics/#32-%E7%BD%91%E7%AB%99%E5%9B%BE%E6%A0%87-%E6%B5%8F%E8%A7%88%E5%99%A8%E9%85%8D%E7%BD%AE-%E7%BD%91%E7%AB%99%E6%B8%85%E5%8D%95>官方链接</a>

### 3.内容组织
> 标签:  - {\{< admonition note "本地资源引用" >}}  {\{< /admonition >}} 

> 文档:  vim  themes/LoveIt/exampleSite/content/posts/theme-documentation-content/index.zh-cn.md

{{< admonition note "本地资源引用" >}}
{{< version 0.2.10 >}}

有三种方法来引用**图片**和**音乐**等本地资源:

1. 使用[页面包](https://gohugo.io/content-management/page-bundles/)中的[页面资源](https://gohugo.io/content-management/page-resources/).
   你可以使用适用于 `Resources.GetMatch` 的值或者直接使用相对于当前页面目录的文件路径来引用页面资源.
2. 将本地资源放在 **assets** 目录中, 默认路径是 `/assets`.
   引用资源的文件路径是相对于 assets 目录的.
3. 将本地资源放在 **static** 目录中, 默认路径是 `/static`.
   引用资源的文件路径是相对于 static 目录的.

引用的**优先级**符合以上的顺序.

在这个主题中的很多地方可以使用上面的本地资源引用,
例如 **链接**, **图片**, `image` shortcode, `music` shortcode 和**前置参数**中的部分参数.

页面资源或者 **assets** 目录中的[图片处理](https://gohugo.io/content-management/image-processing/)会在未来的版本中得到支持.
非常酷的功能! :(far fa-grin-squint fa-fw):
{{< /admonition >}}

### 4.emoji

:smile:

---

### 4.***shortcut***
[shortcut官方](https://hugoloveit.com/zh-cn/theme-documentation-extended-shortcodes/#11-script)
> 也可以style加入css控制
<ol>
<li style="color:blue; ">style </li>
<li style="color:blue; ">link </li>
<li style="color:blue; ">image </li>
<li style="color:blue; ">admonition </li>
<li style="color:blue; ">mermaid </li>
<li style="color:blue; ">echarts </li>
<li style="color:blue; ">bilibili... mapbox</li>
</ol>

### 13.hugo获取资源,比如imag
![image res获取位置](hugo_image_res.png "<a href=https://gohugo.io/content-management/image-processing/#image-resources>官网链接</a>")
`必须index开头的md才能获取当前目录的文件,否则应该放在全局 /asserts/images/下; 不过前置参数resource.name .image方式不能获取`

