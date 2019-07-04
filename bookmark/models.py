from django.db import models
from django.urls import reverse

# Create your models here.

# Bookmark 클래스 생성 => 모델


class Bookmark(models.Model):

    # 두 개의 필드(site_name, url) 생성 => DB에 두가지의 정보를 저장하기 위해 생
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    # 매직메서드(던더 메서드)
    def __str__(self):
        # 객체를 출력할 때 나타날 값
        return "이름: " + self.site_name + ", 주소: " + self.url

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

