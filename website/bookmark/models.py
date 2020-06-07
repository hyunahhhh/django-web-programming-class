from django.db import models


# Create your models here.
class Bookmark(models.Model):
    title = models.CharField('TITLE', blank=True, max_length=100)
    url = models.URLField('URL', unique=True)

    def __str__(self):
        return self.title
        # return 내용을 확인하기 위한 테스트 코드
        # return "%s %s" %(self.title, "^^")
