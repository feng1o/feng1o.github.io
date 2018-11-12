---
title: blog-todo 
date: 2018-11-11 02:22:29
tags:
- hexo
categories:
- hexo
---

# 1.加music background
[example](https://blog.csdn.net/yjwan521/article/details/80899992)

# 2.blog todo
[tutor](https://zhuanlan.zhihu.com/p/26625249)
[side bar](https://lruihao.cn/)
[layout](http://blog.lightina.cn/)

# 3.tags categories
[expamle](https://blog.csdn.net/KnownAll/article/details/81360235)

# 4.tags cloud
```
      没有修改packages.json，直接安装,修改部分会hexo g报错
    	1.npm install hexo-tag-cloud@^2.0.* --save
    	2.next/layout/_macro/sidebar.yml
    		js文件会导致hexo g失败，参见github url 
```

[github](https://github.com/MikeCoder/hexo-tag-cloud/blob/master/README.ZH.md)

# 5.comment
```
    1.https://valine.js.org/quickstart.html 注册，然后F.； 会生成appid，key
    2.修改 vi themes/next/_config.yml ； 修改valine 开启true，把key加上
    3.最后！记得在Leancloud -> 设置 -> 安全中心 -> Web 安全域名 把你的域名加进去
```
# 6.开启字、阅读时间统计
    直接修改_conf.yml文件，开启word_count，read-count；closed

# 7.开启友情链接，修改主题配置

# 8.开启访客统计，可以直接配置key id后，通过主题下的visitors开启

# 9.修改css样式，让友情链接靠左

# 10. 修改页面宽度，太窄
[cankao 宽](https://blog.csdn.net/csdnSR/article/details/78300820)
[cankao used](https://sluggishpj.github.io/blog/2017/10/14/%E4%BF%AE%E6%94%B9NexTPisces%E4%B8%BB%E9%A2%98%E6%A0%B7%E5%BC%8F/)

```
修改layout。style 加：
// 以下为新增代码！！
// 白色区域的最大宽度
$white_max_width = 1200px
    header{ width: 90% !important; } 
header.post-header { 
  width: auto !important; 
} 
.container .main-inner { width: 90%; } 
.content-wrap { width: calc(100% - 260px); } 
.header { 
  +tablet() { 
    width: auto !important; 
    } 
    +mobile() { 
    width: auto !important; } } 

.container .main-inner { 
  +tablet() { width: auto !important; } 
  +mobile() { width: auto !important; } } 

.content-wrap { 
  +tablet() { width: 100% !important; } 
  +mobile() { width: 100% !important; } 
  }
```