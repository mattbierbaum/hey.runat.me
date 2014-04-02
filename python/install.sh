#!/bin/bash

read -p "Are you sure? " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    make clean
    git branch -D gh-pages
    git push origin --delete gh-pages
    git checkout -b gh-pages
    sed -i -e '/index.html/d' .gitignore
    sed -i -e '/pages/d' .gitignore
    make
    git add .
    git commit -m "updating gh-pages from master"
    git push origin gh-pages
    make clean
    git checkout master
fi
