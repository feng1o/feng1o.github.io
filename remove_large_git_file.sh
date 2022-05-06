#!bin/bash

for i in $(git rev-list --objects --all | grep "$(git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -10 | awk '{print$1}')" | awk ' { print $2 }'); do 
    echo $i
    echo "git filter-branch --force --prune-empty --index-filter 'git rm -rf --cached --ignore-unmatch '$i'' --tag-name-filter cat -- --all "
    git filter-branch --force --prune-empty --index-filter 'git rm -rf --cached --ignore-unmatch '$i'' --tag-name-filter cat -- --all ; 
done 

git add .
git commit -m "decrease .git size"
git push --force --all

rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now

