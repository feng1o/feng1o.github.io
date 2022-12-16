---
weight: 6 
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: false  # true will be not indexed in debug mode

lastmod: {{ .Date }}
author: "feng1o"
authorLink: "https://feng1o.github.io"
description: "分类(linux) - **描述xxx`xxx`** ."

featuredImage: images/glibc.png # 对应图片
#featuredImagePreview: /featuredImage/excel-featured-image.jpg

tags: ["标签default1", "标签default2"]
categories: ["分类default"]

lightgallery: true 

toc:
  enable: true
  auto: true 
---