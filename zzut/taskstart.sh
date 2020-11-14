# !/bin/bash

ps -aux | grep "zzutPunchCard" | grep -v grep | awk '{print "kill -9 "$2}' | sh

if [ ! -d $(pwd)/log ]; then
    mkdir log
fi

nohup python3 $(pwd)/zzutPunchCard.py >>$(pwd)/log/runtime.log 2>>$(pwd)/log/runtime.log &
