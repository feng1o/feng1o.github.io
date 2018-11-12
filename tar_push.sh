#!/bin/bash
dt=`date  +%Y-%m-%d`
echo $dt
file="blog-${dt}.tgz"
echo $file
tar czvf $file  blog
git add  $file tar_push.sh  
git commit -m "$file"
git push -f
