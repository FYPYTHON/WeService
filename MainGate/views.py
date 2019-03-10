# coding=utf-8
"""
create  : 2019/3/8 19:48
Author  : feiying
"""
from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from common import message

class CsrfExempt(SessionAuthentication):
    """
    CSRF 检查免除
    """
    def enforce_csrf(self, request):
        return


# Create your views here.
def home(request):
    with open('Templates/home.html', 'rb') as f:
        content = f.read()
    return HttpResponse(content)


# load js
def wejs(request, filename):
    with open('Templates/{}'.format(filename), 'rb') as f:
        js_content = f.read()
    return HttpResponse(content=js_content,
                        content_type='application/javascript')


# load css
def wecss(request, filename):
    with open('Templates/{}'.format(filename), 'rb') as f:
        css_content = f.read()
    return HttpResponse(content=css_content,
                        content_type='text/css')


# load img
def weimg(request, filename):
    with open('Static/{}'.format(filename), 'rb') as f:
        img_content = f.read()
    return HttpResponse(content=img_content,
                    content_type='image/jpeg')


def weico(request, filename):
    with open('Static/{}'.format(filename), 'rb') as f:
        ico_content = f.read()
    return HttpResponse(content=ico_content,
                        content_type='application/x-ico')


class LoginViewMixin(APIView):
    def get(self, request, format=None):
        with open('Templates/login.html', 'rb') as f:
            content = f.read()
        return HttpResponse(content)

    def post(self, request, format=None):
        request_params = request.data
        account = request_params.get('account')
        password = request_params.get('password')
        vercode = request_params.get('vertifyCode')
        print(account, password, vercode)

        resp = message.WebMsg(message.FAIL, 400, message.FUNCTION_NOT_FINISHED)
        return Response(data={'webmsg': resp.to_dict()}, status=status.HTTP_200_OK)

