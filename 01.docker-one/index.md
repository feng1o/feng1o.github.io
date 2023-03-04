# docker - 第一个容器


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

### 1.docker守护进程
```
    早期版本 docker daemon -H tcp://ip:port -H ...
    后期dockerd
```
### 2.第一个容器
```
    docker run --restart=alawys[on-failure:5] --name test -i -t centos /bin/bash
    docker update --restart=always <CONTAINER ID>
    docker rename name1 name2
    docker create 容器不运行，更细粒度的控制
      本地无，docker hub下载镜像
      会创建一个新的容器，有自己的net、ip、网桥； 然后进入一个新的bash页
```
### 3.使用第一个容器
```
      docker ps -a 查看所有容器
    a.主机名
        hostname 
        cat /etc/hosts
    b.ip信息 docker 母鸡
        ip a
        docker inspect hostName
    c.容器里安装软件包
        yum install vim
    d.退出
        exit 这个容器还在，回到宿主机后docker ps -a
```

### 4.启动容器
    docker start dockername/dockerid

### 5.附着到容器
    docer attach name/id

### 6.守护容器
    docker run --name daemon_test -d centos /bin/sh -c "while true;  do echo "ehllo; sleep 2; done"
    后台运行
    docker stop name/id； 

### 7.docker logs
    docker logs -tf  name
    docker logs --tail 1 -t name
    docker logs --tail - -f  -t name

### 8.docker Log驱动
    docker run --log-driver="syslog"

### 9.观察
    docker inspect  --format='{{ .State.Running }}' test1 
    ```
        [22-root@localhost /var/lib/docker]# ll
        total 4
        drwx------. 2 root root   24 Jun 13 00:15 builder
        drwx------. 4 root root   92 Jun 13 00:15 buildkit
        drwx------. 4 root root  150 Jun 16 00:07 containers
        drwx------. 3 root root   22 Jun 13 00:15 image
        drwxr-x---. 3 root root   19 Jun 13 00:15 network
        drwx------. 8 root root 4096 Jun 19 23:15 overlay2
        drwx------. 4 root root   32 Jun 13 00:15 plugins
        drwx------. 2 root root    6 Jun 19 23:15 runtimes
        drwx------. 2 root root    6 Jun 13 00:15 swarm
        drwx------. 2 root root    6 Jun 19 23:15 tmp
        drwx------. 2 root root    6 Jun 13 00:15 trust
        drwx------. 2 root root   25 Jun 13 00:15 volumes
        [23-root@localhost /var/lib/docker]# cd containers/
        [24-root@localhost /var/lib/docker/containers]# ll
        total 0
        drwx------. 4 root root 237 Jun 19 23:15 901ab0e98300cc163901f94214f5ee69c962c685e098cf350db2c2d26c01ec9e
        drwx------. 4 root root 237 Jun 19 23:15 a6bc5cee2d394136c6f45d5ade6cad44a4a8be4cc851c3534c2a054b5acfbcc5
        [25-root@localhost /var/lib/docker/containers
    ```
### 10.删除
```
    docker rm name / [`sudo docker ps -q -a`]
```
### 11.cmd
```
    docker rmi
    docker images
```
 
### 12.容器内运行进程
```
    docker exec -d name cmd[touch /data/test_exec]

    [14-root@localhost /var/lib/docker]# cd containers/
    [15-root@localhost /var/lib/docker/containers
```

