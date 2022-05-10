#!/bin/bash

<<EOF
    注意: 
    1.md文件是index或_inde.md,如需使用当前的resource加载image,比如前置参数的resource.name src信息
    2.一个空的模板
        
EOF
echo -e "\033[0;32mDeploying updates to GitHub...\033[0m"

# Build the project.
# hugo # if using a theme, replace with `hugo -t <YOURTHEME>`
# hugo serve --disableFastRender
hugo

# Go To Public folder
cd public

mkdir feng1o_domain 
cp zh-cn/sitemap.xml feng1o_domain/sitemap.xml
cp zh-cn/index.html feng1o_domain/index.html
sed -i '' 's/feng1o.github.io/feng1o.com/'  feng1o_domain/sitemap.xml
sed -i '' 's/feng1o.github.io/feng1o.com/'  feng1o_domain/index.html

git init
git remote add origin git@github.com:feng1o/feng1o.github.io.git
# Add changes to git.
git add .

# Commit changes.
msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"

# Push source and build repos.
git push origin master -f

# Come Back up to the Project Root
cd ..

rm -rf public

# add src to dev branch
git add .
git commit -m "$msg add src to dev"
git push 
