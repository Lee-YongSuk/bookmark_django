from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from .models import Bookmark

# Create your views here.

# 클래스형 뷰 생성
class BookmarkListView(ListView):
    # 모델 설정
    model = Bookmark
    paginate_by = 3

# 북마크 추가를 위한 뷰 생성
class BookmarkCreateView(CreateView):
    model = Bookmark                    # 어떤 모델의 입력 받을 것인지
    fields = ['site_name','url']       # 어떤 필드들을 입력 받을 것인지
    success_url = reverse_lazy('list')  #
    template_name_suffix = '_create'    # 사용할 템플릿의 접미사 변경

# 북마크 확인(상세)를 위한 뷰 생성
class BookmarkDetailView(DetailView):
    model = Bookmark

# 북마크 수정을 위한 뷰 생성
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

# 북마크 삭제를 위한 뷰 생성
class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')