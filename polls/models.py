import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') # 생성일자

    def __str__(self): # Question 클래스의 object를 Question.objects.all()을 통해 shell창에서 볼 때 원래 object는 괄호 안의 id로 구분된다. 하지만 내용이 보이도록 하기 위해서 __str__을 사용하는데 이 함수의 return값에 따라 Question.objects.all()의 결과에 나오는 결과값이 달라진다.(class object 내의 특정 값을 보일 수 있다.)
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)  # '현재로부터 하루차감한 어제'의 시간 이후에 발행이 된 데이터 반환


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # question 데이터 타입은 외래키로 Question 데이터모델을 참조하겠다는 뜻 / CASCADE 종속[위의 Question의 생성에 종속]
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0) # 투표수

    def __str__(self):
        return self.choice_text
