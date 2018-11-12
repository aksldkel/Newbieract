# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required # 로그인해야만 접근할 수 있도록 제한
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView # 오브젝트를 생성하는 뷰 (form 혹은 model과 연결되서 새로운 데이터를 넣을 때 CreateView - generic view를 사용)

def index(request):
    return render(request, 'auction/index.html', {})
