from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .func import create_report


def test(request):
    create_report.push('hello')
    return HttpResponse("发布消息成功")
