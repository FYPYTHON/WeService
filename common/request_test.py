# coding=utf-8
import requests
from urllib import parse
import json
import html
# path:[path1,path2,…]
# type: status
#   	文件状态的标志
#   home:(AiData,meetingData,mtLog,platformData,platformLog)
def post_test():
    headers = {'type': 'status', 'home': 'meetingData'}
    # param = {'path': ['1.txt', '2.txt', 'ss.bmp']}
    param = {'path':[u'mtf/6.0文件服务器接口文档1.docx',u'mtf/人员信息维护通知.docx']}
    # param = {'path':'[1.txt,2.txt]'}
    f1 = parse.quote('mtf/6.0文件服务器接口文档1.docx')
    f2 = parse.quote('mooooooo-oooo-oooo-oooo-defaultserdo/655/1551843038949/邀请终端 搜索 集团公共群组1.png', encoding='utf-8')
    f3 = parse.quote_plus('mooooooo-oooo-oooo-oooo-defaultserdo/655/1551837056320/邀请终端 搜索 集团公共群组1.png', encoding='utf-8')
    # print(f1+','+f2)
    # print(parse.unquote(f1))
    pp = f1 + ','+ f2 +','+f3
    param = {'path': pp}
    result = requests.post('http://172.16.186.75:8083/api/inner/kdfs/v1', data=param, headers=headers)

    print(result.content)

def putre():
    headers = {'type': 'status', 'home': 'meetingData'}
    param = {'path': ['1.txt', '2.txt', 'ss.bmp']}

    result = requests.post('http://172.16.186.75:8083/api/v1', data=param, headers=headers)

    print(result)
    print(result.content)


def post_addition():
    data = ''
    with open('./test.txt', 'rb') as f:
        data = f.read()

    import os
    filesize = os.path.getsize('./test.txt')
    print(data, filesize, type(filesize))
    print(len(data))
    headers = {'type': 'addition', 'home': 'meetingData', 'path': '2.txt', 'filesize':str(filesize)}

    result = requests.post('http://172.16.186.75:8083/api/inner/kdfs/v1', data=data, headers=headers)

    print(result.content)


def put_rename():
    headers = {'type': 'rename', 'home': 'meetingData','path':'newdir'}
    param = {'dstpath': 'testdir'}

    result = requests.put('http://172.16.186.75:8083/api/inner/kdfs/v1', data=param, headers=headers)
    print(result.content)


def put_copy():
    headers = {'type': 'copy', 'home': 'meetingData', 'path': 'newdir'}
    param = {'dstpath': 'testdir'}

    result = requests.put('http://172.16.186.75:8083/api/inner/kdfs/v1', data=param, headers=headers)
    print(result.content)

def put_upload():
    data = ''
    with open('./邀请终端 搜索 集团公共群组1.png', 'rb') as f:
        data = f.read()

    import os
    filesize = os.path.getsize('./邀请终端 搜索 集团公共群组1.png')
    # print(data, filesize, type(filesize))
    print(len(data))
    headers = {'type': 'upload', 'home': 'meetingData', 'path': parse.quote_plus('mooooooo-oooo-oooo-oooo-defaultserdo/655/1551837056320/邀请终端 搜索 集团公共群组1.png'), 'filesize': str(filesize)}

    result = requests.put('http://172.16.186.75:8083/api/inner/kdfs/v1', data=data, headers=headers)

    print(result.content)


if __name__ == "__main__":
    # post_addition()
    # put_rename()
    # put_copy()
    post_test()
    # put_upload()


