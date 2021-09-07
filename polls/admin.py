from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.StackedInline): # class ChoiceInline(admin.TabularInline): # table모습으로 simple하게 변형 가능/나타낼 수 있음.
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # 개별 데이터의 사용자 정의(customizing)
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date']}),    
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date'] # 필터 창을 추가 (발행일을 필터(기준)으로 Question 확인 가능)
    search_fields = ['question_text'] # 검색창 추가

    # 리스트의 사용자 정의(리스트에서 보이는 항목 변경)
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # 속성 부여(편리성 향상 가능) - models.py에서 속성 부여

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)