"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')), # polls앱의 url과 연결 / include 함수는 다른 URLconf들을 참조할 수 있도록 도와준다. 현 코드에서 include는 polls앱의 urls.py를 참조하고 있다.
    path('admin/', admin.site.urls),
]

# 최상위 urlconf에서 url를 parsing해서(ex) polls/, admins/, ...[parsing 해서 받은 path들] => 원래 12.003.35/polls, 12.003.35/admins 등의 형태) path를 받고 각 path별로 다른 앱으로 분기시켜줌.
