from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question


def index(request):
    latest_question_list = Question.objects.order_by('-date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'james/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'james/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
