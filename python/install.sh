#!/bin/bash

read -p "Are you sure? " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    make clean
    git checkout gh-pages
    git rebase master
    make
    git add .
    git commit -m "updating gh-pages from master"
    git push origin gh-pages
    make clean
    git checkout master
fi
