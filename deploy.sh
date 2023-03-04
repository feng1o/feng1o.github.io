#!/bin/bash
local_do=${1-:"n"}
<<EOF
    注意: 
    1.md文件是index或_inde.md,如需使用当前的resource加载image,比如前置参数的resource.name src信息
    2.一个空的模板
        
EOF
echo -e "\033[0;32mDeploying updates to GitHub...\033[0m"

# create a new page: 
# hugo new posts/dir/x.md

# Build the project.
# hugo # if using a theme, replace with `hugo -t <YOURTHEME>`
# hugo serve --disableFastRender
git checkout dev
git submodule update

hugo

dir=$(pwd)
if [[ "$local_do" == "y" || "$local_do" == "Y" ]];then
    base_dir="."
else
    base_dir=$(dirname $(pwd))
fi

# Go To Public folder
mkdir -p ${base_dir}/public/
cp -r public/* ${base_dir}/public/
echo "${base_dir}/public"
cd ${base_dir}/public

mkdir feng1o_domain 
cp ${dir}/zh-cn/sitemap.xml feng1o_domain/sitemap.xml
cp ${dir}/zh-cn/index.html feng1o_domain/index.html
sed -i  's/feng1o.github.io/feng1o.com/'  feng1o_domain/sitemap.xml
sed -i  's/feng1o.github.io/feng1o.com/'  feng1o_domain/index.html

pwd
read -p "ok" ok
git init
git remote add origin git@github.com:feng1o/feng1o.github.io.git
# Add changes to git.
git add .

read -p "ok" ok
# Commit changes.
msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"

# Push source and build repos.
git push origin master -f

# Come Back up to the Project Root
cd ${dir}

#rm -rf ${dir}public

# add src to dev branch
git add .
git commit -m "$msg add src to dev"
git push 
