from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
import requests
from django.http import JsonResponse
from .models import Question,Answer
from django.utils import timezone


def test(request):
    return render(request, "viewmap/test.html")

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    context = {"question":question}
    return render(request, 'viewmap/detail.html',context)

def answer_create(request,question_id):
    question = get_object_or_404(Question, pk = question_id)
    question.answer_set.create(content = request.POST.get('content'), create_date = timezone.now())
    return redirect('pybo:detail',question_id = question.id)