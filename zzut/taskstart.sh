ps -aux|grep "zzutPunchCard"|grep -v grep|awk '{print "kill -9 "$2}'|sh
nohup python3 $(pwd)/zzutPunchCard.py >/dev/null 2>/dev/null &