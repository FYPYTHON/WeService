# coding=utf-8
import requests
from urllib import parse
import json
import html
dthost = 'http://localhost:8081/weservice/v1'
def post_addition():
    data = ''
    with open('./test.txt', 'rb') as f:
        data = f.read()

    import os
    filesize = os.path.getsize('./test.txt')
    print(data, filesize, type(filesize))
    print(len(data))
    headers = {'type': 'addition', 'home': 'meetingData', 'path': '2.txt', 'filesize':str(filesize)}

    result = requests.post(dthost, data=data, headers=headers)

    print(result.content)


def put_rename():
    headers = {'type': 'rename', 'home': 'meetingData','path':'newdir'}
    param = {'dstpath': 'testdir'}

    result = requests.put(dthost, data=param, headers=headers)
    print(result.content)



if __name__ == "__main__":
    # post_addition()
    # put_rename()
    # put_copy()
    put_rename()
    # put_upload()


