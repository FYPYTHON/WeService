"""WeService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from MainGate.views import wejs, wecss, weico, weimg, home, LoginViewMixin

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^(home|login)/js/(?P<filename>.*\.js)$', wejs, name='myjs'),  # the same with href src
    url(r'^(home|login)/css/(?P<filename>.*\.css)$', wecss, name='mycss'),
    url(r'^(home|login)/ico/(?P<filename>.*\.ico)$', weico, name='myico'),  # load ico
    url(r'^(home|login)/css/img/(?P<filename>.*\.(jpg|png|gif|jpeg|bmp))$', weimg, name='myimg'), # load picture setting in css
    url(r'^login/', LoginViewMixin.as_view(), name="login"),
    url(r'^home/', home, name="home"),

]

