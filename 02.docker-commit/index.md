# docker - 构建


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


### 1.构建
```
    docker commit
    docker build + dockerfile
```

### 2.docker image设置

[daocloud比较快](https://www.daocloud.io/mirror)
[ustc中科大的](http://mirrors.ustc.edu.cn/help/dockerhub.html?highlight=docker#id3)

### 3.docker commit
```
    docker commit -m 'comomment' -a 'author'  [id]  user/reigtname
```

### 4.dockerfile
```
    docker build -t="仓库/镜像名:tag" . 
    docker build -t="仓库/镜像名:tag"  -f 指定dockerfile
    docker build --no-cache -t="仓库/镜像名:tag"  git@github.com:xx/xx的dockerfile
```

```
# Version: 0.1
FROM ubuntu:14.04   层
MAINTAINER lf "xx.com"  层...
RUN apt-get update && apt-get install  -y nginx 
RUN echo "hi dockerfile" > /usr/share/nginx/html/index.html

CMD  ["/bin/bash", "ls", " -l /"]  [运行时执行run是build。cmd只能一条]
ENTRYPOINT  ["/usr/bin/nginx"，"-g" " daemon off;"] [不会被run的覆盖，和cmd不一样]
ENV  XX_PAHT /home/xx
VOLUME --TODO:
USER
ADD / COPY 
LABEL
ARG  --build-arg x=b  部分预定义args变量
ONBUILD

EXPOSE 8082

```

### 5.other cmd
```
docker history id 看build命令
```

### 6.port和宿主机绑定
```
    a.随机选32678 -- 61000
    b.指定： -p

    c.docker ps -l  或 docker port id  port
    d.docker run -P 会把dockerfile里expose的端口对外公开
```

### 7.push docker hub
```
    
```

### 8.local registry
```
 加tag： docker tag id registryhost:port /name/仓库
```

