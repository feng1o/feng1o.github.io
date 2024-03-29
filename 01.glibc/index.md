# linux - glic升级


<a style="color:red;"> <strong>💥谨慎操作.</strong> </a>**libc.so.6: version `GLIBC_2.14' not found**.
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

<!-- directives: [] -->
<div id="content">
  <ul>
    <li>/lib64/libc.so.6: version `GLIBC_2.14&apos; not found</li>
    <li>strings  /lib64/ligc.so.6 | grep GLIBC 可看支持哪些版本</li>
      <pre><code data-lang="shell">	  
      GLIBC_2.10
	  GLIBC_2.11
	  GLIBC_2.12
      </code></pre>
    <li><a href="https:cloud.tencent.com/developer/article/1710774">安装gcc-参考</a>：
      <blockquote>
        <p>gcc主要依赖有：gmp，MPFR，MPC，手动安装均可。 根据download_prerequisites比较easey
          <br />
<img src="../assets/image_1651469479377_0.png" title="image.png" />
          <br />
</p>
      </blockquote>
</li>
    <li>安装 新版glibc：比较简单，网上资料很多<a href="https:www.cnblogs.com/kevingrace/p/8744417.html">参考</a>
      <ul>
        <li>之后把glibc.so.6指向新的，或者改LD_LIBRARY_PATH： 比如export   LD_LIBRARY_PATH=/usr/local/glibc-2.17/lib:/lib64/:/usr/local/gcc-4.8/lib64</li>
      </ul>
    </li>
    <li><span><a>可能报错</a>：比如某些so版本问题，ld问题，甚至各种命令失效</span>
      <ul>
        <li>恢复：           <mark>此时恢复2.12为例：LD_PRELOAD=&quot;/lib64/libc.so.6-2.12&quot;  ln -s /lib64/libc-2.12.so  /lib64/libc.so.6 恢复到新的
          </mark>
</li>
        <li>error while loading shared libraries: __vdso_time: invalid mode for dlopen(): Invalid argument
<pre><code data-lang="shell" class="shell">
这个是用的ld和glic问题，比如2.17升级为例
echo &quot;&quot; &gt; /etc/ld.so.preload
LD_LIBRARY_PATH=/usr/local/glibc-2.17/lib:/lib64/:/usr/local/gcc-4.8/lib64:/usr/lib64 /usr/local/glibc-2.17/lib/ld-2.17.so    ./a.out
可以执行，但是不能每个都指定ld-2717.so
</code></pre>
</li>
  </ul>
</div>

### 最终版 -- 谨慎操作,风险极大
<a class="alg-hard" href="https://gist.github.com/harv/f86690fcad94f655906ee9e37c85b174"> 源🔗：直接升级rpm包</a>
```shell
#!/bin/bash
cat &lt;&lt;EOF
	caveat：
    	be careful, this may destroy your linux system， please backup your data first.
EOF

echo &quot;May damage your system!&quot;
read -p &quot;sure to do ?&quot; t
sleep 5

# update glibc to 2.17 for CentOS 6

GLIBC=glibc
OS=el6
SERVER=https://copr-be.cloud.fedoraproject.org/results/mosquito/myrepo-el6
VERSION=2.17-55
FULL_VERSION=$GLIBC-$VERSION.fc20
X64=x86_64
I386=i386
I636=i686
REPO_32=epel-6-$I386
REPO_64=epel-6-$X64

SERVER_32=$SERVER/$REPO_32/$FULL_VERSION
RPM_32=$VERSION.$OS.$I636.rpm
SERVER_64=$SERVER/$REPO_64/$FULL_VERSION
RPM_64=$VERSION.$OS.$X64.rpm

# Packages
P_1=$GLIBC
P_2=$GLIBC-common
P_3=$GLIBC-devel
P_4=$GLIBC-headers
P_5=$GLIBC-static
P_6=$GLIBC-utils
P_7=nscd

# Required as dependency of glibc-utils
sudo yum install --assumeyes gd

# 64-bit    --nodeps 慎重使用
sudo rpm -Uvh  --nodeps --force $SERVER_64/$P_1-$RPM_64 $SERVER_64/$P_2-$RPM_64 $SERVER_64/$P_3-$RPM_64 $SERVER_64/$P_4-$RPM_64 $SERVER_64/$P_5-$RPM_64 $SERVER_64/$P_6-$RPM_64 $SERVER_64/$P_7-$RPM_64
# Print out versions
strings /lib64/libc.so.6 | grep GLIBC

# 32-bit
# sudo rpm -Uvh --force $SERVER_32/$P_1-$RPM_32 $SERVER_32/$P_2-$RPM_32 $SERVER_32/$P_3-$RPM_32 $SERVER_32/$P_4-$RPM_32 $SERVER_32/$P_5-$RPM_32 $SERVER_32/$P_6-$RPM_32 $SERVER_32/$P_7-$RPM_32
```
> 以上操作不可逆,且需重启;如重启失败只能重装系统. 经测试可行

