"""FasterRunner URL Configuration

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

from django.urls import path
from fastrunner import views

urlpatterns = [
    # 项目相关接口地址
    path('project/', views.ProjectView.as_view({
        "get": "list",
        "post": "add",
        "patch": "update",
        "delete": "delete"
    })),
    path('project/<int:pk>/', views.ProjectView.as_view({"get": "get_single"})),

    # 数据库相关接口地址
    path('database/', views.DataBaseView.as_view({
        "get": "list",
        "post": "create",
    })),
    path('database/<int:pk>/', views.DataBaseView.as_view({
        'patch': 'partial_update',
        'delete': 'destroy'
    })),

    # debugtalk.py相关接口地址
    path('debugtalk/<int:pk>/', views.DebugTalkView.as_view({"get": "debugtalk"})),
    path('debugtalk/', views.DebugTalkView.as_view({"patch": "update"})),

    # 二叉树接口地址
    path('tree/<int:pk>/', views.TreeView.as_view()),

    # 文件上传 修改 删除接口地址
    path('file/', views.FileView.as_view()),

    # api接口模板地址
    path('api/', views.APITemplateView.as_view({
        "post": "add",
        "get": "list"
    })),

    path('api/<int:pk>/', views.APITemplateView.as_view({
        "delete": "delete",
        "get": "get_single"
    })),


]