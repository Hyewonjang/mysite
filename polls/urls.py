# views.py에 작성한 기능을 실행하기 위해/작성한 view를 실행하기 위해 url 파일을 작성해 연결해줘야 한다.
from django.urls import path
from . import views

app_name = 'polls' # 다른 app에서도 같은 name 쓸 수 있으므로 app_name 설정할 것
urlpatterns = [
    # ex /polls/
    path('', views.index, name='index'),
    # path('', views.IndexView.as_view(), name='index'),
    
    # ex /polls/5/
    path('<int:question_id>/', views.detail, name='detail'), # 괄호 내 첫번째 ''은 urlpattern으로 urlpattern에 맞는 url의 경우 두번째에 적혀있는 해당 views를 호출하겠다는 의미이며, name은 urlpattern을 직접적으로 쓰지 않고 이를 가리킬 수 있는 것이다.
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'), # pk란? db 내의 하나의 열, 즉 하나의 데이터를 구분할 수 있는 값(중복 없음)
    
    # ex /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'), # question_id는 views.results의 parameter인 question_id와 동일하다. 
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    
    # ex /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),  # <int:변수>/ Django에서 지원하는 url패턴
    # path('<int:question_id>/vote/', views.vote, name='vote'),

]