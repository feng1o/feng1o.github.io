---
title: hexo在windows上发布错误修复
date: 2018-11-11 01:02:39
tags:
- hexo
---
# 1. err
'''
bash: /dev/tty: No such device or address
error: failed to execute prompt script (exit code 1)
fatal: could not read Username for 'https://github.com': No error
FATAL Something's wrong. Maybe you can find the solution here: http://hexo.io/docs/troubleshooting.html
Error: bash: /dev/tty: No such device or address
error: failed to execute prompt script (exit code 1)
fatal: could not read Username for 'https://github.com': No error

    at ChildProcess.<anonymous> (D:\yun\github\algorithm\feng1o.github.io\blog\node_modules\hexo-util\lib\spawn.js:37:17)
    at ChildProcess.emit (events.js:159:13)
    at ChildProcess.cp.emit (D:\yun\github\algorithm\feng1o.github.io\blog\node_modules\cross-spawn\lib\enoent.js:40:29)
    at maybeClose (internal/child_process.js:943:16)
    at Process.ChildProcess._handle.onexit (internal/child_process.js:220:5)
	
'''
# 2.主要是由于从Linux下clone的终端tty问题

```
	fix: git@github.com:feng1o/feng1o.github.io.git 

	tip: 不可改成 ssh:git@github.com/xx/xx.git, ssh会提示publickey 不支持ssh脚本，需开启
```
