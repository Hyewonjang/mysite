# from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Question

# Create your views here.
# 각 view는 HttpResponse 객체 또는 Http404 중 하나를 무조건 반환한다.
def index(request):
    # 1
    # return HttpResponse("Hello, World.")

    # 2
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # 3
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context,request)) # data(latest_question_list)를 context를 통해 template에 전달

    # 4
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # 1
    # return HttpResponse("You're looking at question %s." % question_id)
    
    # 2
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist: # question_id에 맞는 Question Object가 존재하지 않을 때
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question':question})

    # 3
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    # 1
    # return HttpResponse("You're voting on question %s." % question_id)

    # 2
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # request(받은 정보) 중 method가 POST 인 것 중 name이 choice인 선택된 설문의 ID를 문자열로 반환한다.
    except (KeyError, Choice.DoesNotExist): # choice가 없으면 detail 페이지 달라짐.
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {  
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after succesffully deal with Post data.
        # This prevents data from being posted twice
        # if user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id, id))) # POST와 ResponseRedirect는 한 세트임. reverse의 경우 url을 하드코딩 즉, urlpattern에 맞게 적지 않기 위하여 reverse 사용하고 'polls:results' urls.py에서 설정한 name 사용한 것임.