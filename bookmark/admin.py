from django.contrib import admin

# models.py파일에서 Bookmark라는 모델을 불러오겠다.
from .models import Bookmark

# Register your models here.

# Bookmark 모델 등록
admin.site.register(Bookmark)