#!/usr/bin/env bash

option=$1

cur_dir=$(dirname "$0")
cd ${cur_dir}
KDFS_PID=../stsps.pid
if [ -e ${KDFS_PID} ];then
    uwsgi --stop ${KDFS_PID}
    rm -rf ${KDFS_PID}
    sleep 1
    echo "OK."
fi
uwsgi_pid=`ps aux|grep "stsps"|grep -v "grep"|awk '{print $2}'`
[ -z ${uwsgi_pid} ] && echo "stsps is not running" || kill -9 ${uwsgi_pid}

cd - >/dev/null 2>&1
