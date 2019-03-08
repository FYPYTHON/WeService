# coding=utf-8
MAINPATH = '/opt/data/region'
HOME = ['AiData', 'meetingData', 'mtLog', 'platformData', 'platformLog']
FILE = 0
PATH = 1
FAIL = '0'
SUCCESS = '1'
FUNCTION_NOT_FINISHED = u'功能尚未实现...'
SEARCH_DISK_LIST_FAIL =u'查找磁盘列表失败！'
DISK_IS_NOT_EXIST = u'服务器上没有该磁盘，请重新输入正确的磁盘！'
SEARCH_SUCCESS = u'查询成功！'
SEARCH_HAVE_NO_RESULT = u'查询结果为空'
PAREM_ERROR = u'参数错误，请检查！'
FILE_EXIST = u'文件或目录已存在！'
FILE_NOT_EXIST = u'文件或目录不存在！'
FILE_REMOVE_ERROR = u'文件或目录删除失败！'
DIRECTORY_NEW_SUCCESS = u'文件夹创建成功！'
DIRECTORY_NEW_ERROR = u'文件夹创建失败！'
UPLOAD_FILE_NOT_EXIST = u'上传的文件不存在!'
UPLOAD_FILE_SUCCESS = u'文件上传成功!'
UPLOAD_FILE_FAIL = u'文件上传失败!'
DOWNLOAD_FILE_SUCCESS = u'文件下载成功!'
DOWNLOAD_FILE_FAIL = u'文件下载失败!'
COPY_FILE_SUCCESS = u'文件复制成功!'
COPY_FILE_FAIL = u'文件复制失败!'
COPY_DIRECTORY_SUCCESS = u'文件复制成功!'
COPY_DIRECTORY_FAIL = u'文件复制失败!'


class WebMsg:
    def __init__(self, success="", code="", desp=""):
        self.success = success
        self.errcode = code
        self.details = desp

    def to_dict(self):
        return {'success':self.success, 'errcode': self.errcode, 'details':self.details}


