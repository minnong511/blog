from django.db import models
# 모델은 데이터베이스 사용을 쉽게 하기 위해 사용하는 도구이다

# API(Application Programming Interface)
# 기관이나 기업이 만든 기능이나 데이터를 응용 프로그램에서 사용할 수 있게 만드는 중간 매개체
# 프로그램 => API => 내 프로그램 (난이도가 쉬워진다)


# 데이터베이스 모델
# 데이터베이스 관리 시스템이 지원하는 공식언어로 만들어진 데이터베이스나 구조나 형식

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
# 데이터베이스의 각 필드는 Field 클래스의 인스턴스로서 표현

