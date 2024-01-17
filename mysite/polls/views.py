from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return render(request, 'polls/index.html', {'latest_question_list':latest_question_list})
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("질문이 없어요~")
    return render(request, 'polls/detail.html',{'question':question})
    # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)