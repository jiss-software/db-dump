#!/bin/bash

cd ${0%/*}

[ -d ./tmp ] && rm -r ./tmp
[ ! -d ./log ] && mkdir ./log

[ -f ./log/error.log ] && rm ./log/error.log
[ -f ./log/main.log ] && rm ./log/main.log

python dump.py "$1" 2>> ./log/error.log >> ./log/main.log
