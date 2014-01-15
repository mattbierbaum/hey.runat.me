#!/bin/bash

pngquant 256 *.png
for f in *-fs8.png 
do 
    mv $f ${f//-fs8/} 
done
