#!/usr/bin/env bash

option=$1

cur_dir=$(dirname "$0")
cd ${cur_dir}
uwsgi -i ../uwsgi.ini

cd - >/dev/null 2>&1
