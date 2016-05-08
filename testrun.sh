#!/bin/bash

rm -rf testing
rm -rf downloads
cp -r downloads\ copy downloads
rm count.txt
python3 assign4.py "downloads" "testing" > count.txt
