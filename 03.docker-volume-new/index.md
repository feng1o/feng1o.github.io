# docker - 卷和网络


<a style="color:red;"> <strong>基础</strong> </a>**docker**.
<!--more-->

<!-- 注释,此处是style -->
<style>
pre {
    white-space: pre-wrap;
    word-wrap: break-word;
    align: left;
}

h3,h1 {
background : lightgray;
}

h3:hover {
color : red;
}
</style>



### 1.volume是什么

### 2.volume 用途
```
    a.multi docker共享代码
    b.changed frequency， so do not want build
    c.test and delop at the same time
```

### 3.how to config
```
    docker run -v  $PWD/xxx:/var/xx【：ro/rw可选】
```

---


### 1.docker之间网络
```
    a.docker 内部网络 不灵活 
    b.1.9后 docker networking  [v]
            不同宿主机
            停止  重启 无序关系链接
            运行顺序无关
    c.docker链接， 通信抽象层
```

### 2.创建docker networking
```
    a.docker network create xx  
        docker run  --net=xx  --name=bbb。。。 指定网络；
        会在/etc/hosts里有配置，会有bbb.xx作为域名
    b.docker network inspect xx
    c.overlay网络支持跨宿主机
    d.docker network connect xx  contianernamexx
    e.docker network disconnect xx continerx
```

### 3.docker特权模式 --privileged  docker内在跑docker必须

