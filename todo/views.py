from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'todo/index.html')


@login_required
def index_list(request):
    """
    v 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'todo/question_list.html', context)


def detail(request, question_id):
    """
    todo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'todo/question_detail.html', context)


def answer_create(request, question_id):
    """
    todo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('todo:detail', question_id=question.id)




