# go - GMP调度器


<a href="https:strikefreedom.top/high-performance-implementation-of-goroutine-pool">原文:GMP分析-手撸goroutine pool</a></li>
go - **GMP调度器**.
<!--more-->

<!-- directives: [] -->
<div id="content">
  <ul>
    <li>学习:<a href="https:strikefreedom.top/high-performance-implementation-of-goroutine-pool">GMP分析-手撸goroutine pool</a></li>
    <li>主流的线程模型型分三种:         <mark>内核级线程模型
      </mark>
、      <mark>用户级线程
      </mark>
模型和      <mark>两级线程
      </mark>
模型（也称混合型线程模型），传统的协程库属于用户级线程模型</li>
    <li>用户级/线程模型
      <ul>
        <li>用户层面多线程，和内核线程N-1关系，内核只知道用户进程，用户层的线程自己调度控制。</li>
        <li>原罪：并不能做到真正意义上的并发，假设在某个用户进程上的某个用户线程因为一个阻塞调用（比如 I/O 阻塞）而被 CPU 给中断（抢占式调度）了，那么该进程内的所有线程都被阻塞（因为单个用户进程内的线程自调度是没有 CPU 时钟中断的，从而没有轮转调度），整个进程被挂起</li>
        <li>解决：<code>协程库</code>会把自己一些阻塞的操作重新封装为完全的<b>非阻塞形式</b>，然后在以前要阻塞的点上，主动让出自己，并通过某种方式通知或唤醒其他待执行的用户线程在该 KSE 上运行，从而避免了内核调度器由于 KSE 阻塞而做上下文切换，这样整个进程也不会被阻塞了</li>
      </ul>
    </li>
    <li>内核级线程模型
      <ul>
        <li>线程的调度则完全交付给操作系统内核去做，应用程序对线程的创建、终止以及同步都基于内核提供的系统调用来完成</li>
      </ul>
    </li>
    <li>混合线程模型/两级线程模型
      <ul>
        <li>用户线程与内核 KSE 是多对多（N : M）的映射模型</li>
        <li><a><strong>即用户调度器实现用户线程到 KSE 的『调度』，内核调度器实现 KSE 到 CPU 上的『调度』</strong></a></li>
        <li></li>
      </ul>
    </li>
    <li>go语言的G-P-M 模型
      <ul>
        <li>goroutine 是一个独立的执行单元，OS 线程2M ，goroutine 动态， 初始 2KB，最大可达 1GB，且自己 Go Scheduler调度，还可自动回收</li>
        <li>          <mark>G
          </mark>
:
          <ul>
            <li>表Goroutine，Goroutine 对应一个 G 结构，G 存储 Goroutine 的<b>运行堆栈、状态以及任务函数</b>，可重用。G 并非执行体，每个 G 需要绑定到 P 才能被调度执行。</li>
          </ul>
        </li>
        <li>          <mark>P
          </mark>
:
          <ul>
            <li>Processor，表示逻辑处理器， 对 G 来说，P 相当于 CPU 核，G 只有绑定到 P(在 P 的 local runq 中)才能被调度。对 M 来说，P 提供了相关的执行环境(Context)，如内存分配状态(mcache)，任务队列(G)等，P 的数量决定了系统内最大可并行的 G 的数量（前提：物理 CPU 核数 &gt;= P 的数量），P 的数量由用户设置的 GOMAXPROCS 决定，但是不论 GOMAXPROCS 设置为多大，P 的数量最大为 256。</li>
          </ul>
        </li>
        <li>          <mark>M
          </mark>
:
          <ul>
            <li>Machine，OS 线程抽象，代表着真正执行计算的资源，在绑定有效的 P 后，进入 schedule 循环；而 schedule 循环的机制大致是从 Global 队列、P 的 Local 队列以及 wait 队列中获取 G，切换到 G 的执行栈上并执行 G 的函数，调用 goexit 做清理工作并回到 M，如此反复。M 并不保留 G 状态，这是 G 可以跨 M 调度的基础，M 的数量是不定的，由 Go Runtime 调整，为了防止创建过多 OS 线程导致系统调度不过来，目前默认最大限制为 10000 个</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>
</div>



