# views.py에 작성한 기능을 실행하기 위해/작성한 view를 실행하기 위해 url 파일을 작성해 연결해줘야 한다.
from django.urls import path
from . import views

urlpatterns = {
    path('', views.index, name='index'),
}