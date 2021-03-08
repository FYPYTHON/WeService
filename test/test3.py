# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#
# # coding=utf-8
# """
# create  : 2019/3/8 19:48
# Author  : feiying
# """
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from common import message
# from .models import User
#
#
# class CsrfExempt(SessionAuthentication):
#     """
#     CSRF 检查免除
#     """
#     def enforce_csrf(self, request):
#         return
#
#
# # Create your views here.
# def home(request):
#     with open('Templates/wehome.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
# # http://tool.oschina.net/commons/  -->content type
# # load js
# def wejs(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         js_content = f.read()
#     return HttpResponse(content=js_content,
#                         content_type='application/javascript')
#
#
# # load css
# def wecss(request, filename):
#     with open('Templates/{}'.format(filename), 'rb') as f:
#         css_content = f.read()
#     return HttpResponse(content=css_content,
#                         content_type='text/css')
#
#
# # load img
# def weimg(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='image/jpeg')
#
#
# # load img
# def wesvg(request, filename):
#     with open('Static/svg/{}'.format(filename), 'rb') as f:
#         img_content = f.read()
#     return HttpResponse(content=img_content,
#                     content_type='text/xml')
#
#
# def weico(request, filename):
#     with open('Static/{}'.format(filename), 'rb') as f:
#         ico_content = f.read()
#     return HttpResponse(content=ico_content,
#                         content_type='application/x-ico')
#
# # Create your views here.
# def profile(request):
#     # print("profile", request)
#     with open('Templates/weprofile.html', 'rb') as f:
#         content = f.read()
#     return HttpResponse(content)
#
#
# def wefont(request, filename):
#     # print(filename)
#     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
#         font_content = f.read()
#     return HttpResponse(content=font_content,
#                         content_type='application/x-font-woff')
# class LoginViewMixin(APIView):
#     def get(self, request, format=None):
#         with open('Templates/welogin.html', 'rb') as f:
#             content = f.read()
#         return HttpResponse(content)
#
#     def post(self, request, format=None):
#         request_params = request.data
#         account = request_params.get('account')
#         password = request_params.get('password')
#         vercode = request_params.get('vertifyCode')
#         print(account, password, vercode)
#         resp = message.WebMsg()
#         login_user = None
#         try:
#             login_user = User.objects.get(account=account)
#         except User.DoesNotExist as e:
#             # from datetime import datetime
#             # User.objects.create(account=account, password=password, email='',\
#             # create_time=datetime.now(), login_time='')
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = e
#             print(e)
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#         if login_user.account != account or login_user.password != password:
#             resp.success = message.FAIL
#             resp.errcode = 404
#             resp.details = "account or password error!"
#             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
#         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
#         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
#
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
# # # coding=utf-8
# # """
# # create  : 2019/3/8 19:48
# # Author  : feiying
# # """
# # from django.shortcuts import render,redirect
# # from django.http import HttpResponse
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.views import APIView
# # from common import message
# # from .models import User
# #
# #
# # class CsrfExempt(SessionAuthentication):
# #     """
# #     CSRF 检查免除
# #     """
# #     def enforce_csrf(self, request):
# #         return
# #
# #
# # # Create your views here.
# # def home(request):
# #     with open('Templates/wehome.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# # # http://tool.oschina.net/commons/  -->content type
# # # load js
# # def wejs(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         js_content = f.read()
# #     return HttpResponse(content=js_content,
# #                         content_type='application/javascript')
# #
# #
# # # load css
# # def wecss(request, filename):
# #     with open('Templates/{}'.format(filename), 'rb') as f:
# #         css_content = f.read()
# #     return HttpResponse(content=css_content,
# #                         content_type='text/css')
# #
# #
# # # load img
# # def weimg(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='image/jpeg')
# #
# #
# # # load img
# # def wesvg(request, filename):
# #     with open('Static/svg/{}'.format(filename), 'rb') as f:
# #         img_content = f.read()
# #     return HttpResponse(content=img_content,
# #                     content_type='text/xml')
# #
# #
# # def weico(request, filename):
# #     with open('Static/{}'.format(filename), 'rb') as f:
# #         ico_content = f.read()
# #     return HttpResponse(content=ico_content,
# #                         content_type='application/x-ico')
# #
# # # Create your views here.
# # def profile(request):
# #     # print("profile", request)
# #     with open('Templates/weprofile.html', 'rb') as f:
# #         content = f.read()
# #     return HttpResponse(content)
# #
# #
# # def wefont(request, filename):
# #     # print(filename)
# #     with open('Static/asset/fonts{}'.format(filename), 'rb') as f:
# #         font_content = f.read()
# #     return HttpResponse(content=font_content,
# #                         content_type='application/x-font-woff')
# # class LoginViewMixin(APIView):
# #     def get(self, request, format=None):
# #         with open('Templates/welogin.html', 'rb') as f:
# #             content = f.read()
# #         return HttpResponse(content)
# #
# #     def post(self, request, format=None):
# #         request_params = request.data
# #         account = request_params.get('account')
# #         password = request_params.get('password')
# #         vercode = request_params.get('vertifyCode')
# #         print(account, password, vercode)
# #         resp = message.WebMsg()
# #         login_user = None
# #         try:
# #             login_user = User.objects.get(account=account)
# #         except User.DoesNotExist as e:
# #             # from datetime import datetime
# #             # User.objects.create(account=account, password=password, email='',\
# #             # create_time=datetime.now(), login_time='')
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = e
# #             print(e)
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #         if login_user.account != account or login_user.password != password:
# #             resp.success = message.FAIL
# #             resp.errcode = 404
# #             resp.details = "account or password error!"
# #             return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #         resp = message.WebMsg(message.SUCCESS, 200, message.LOGIN_SUCCESS)
# #         return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)
# #
# #
