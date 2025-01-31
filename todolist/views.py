from django.shortcuts import render,redirect
from .forms import IndexForm,TodoForm
from django.urls import reverse
from .models import Todo,Day
from django.shortcuts import get_object_or_404
from datetime import datetime,timedelta
from django.core.paginator import Paginator
def index(request):
    if request.method == 'POST':
        form = IndexForm(request.POST)
        if form.is_valid():
            selected_date = form.cleaned_data['day']
            return redirect(reverse('todolist:detail',args=[str(selected_date)]))
    params = {
        'title':'Todolist',
        'form':IndexForm()
    }
    return render(request,'todolist/index.html',params)
def detail(request,date,num=1):
    day_obj = get_object_or_404(Day,day=date)
    data = Todo.objects.filter(selected_day=day_obj)
    form = TodoForm()
    page = Paginator(data,8)
    if request.method == 'POST':
        task_id = request.POST.get("task_id")
        if task_id:
            todo = get_object_or_404(Todo,id = task_id)
            is_done_value = request.POST.get(f"is_done_{task_id}", "off")
            todo.is_done = True if is_done_value == "on" else False
            todo.save()
    params = {
        'title':date+'のTODO',
        'day':date,
        'preday':(datetime.strptime(date,"%Y-%m-%d")-timedelta(days=+1)).strftime("%Y-%m-%d"),
        'nextday':(datetime.strptime(date,"%Y-%m-%d")+timedelta(days=+1)).strftime("%Y-%m-%d"),
        'form':form,
        'contents': page.get_page(num),
        'indexform':IndexForm(),
    } 
    return render(request,'todolist/detail.html',params)
def create(request, date):
    if request.method == "POST":
        obj = Day.objects.get(day=date)
        task =request.POST['assignments']
        if Todo.objects.filter(selected_day=obj,assignments=task).exists():
            return redirect(reverse('todolist:detail', args=[str(date)]))
        Todo.objects.create(selected_day=obj,assignments=task,is_done=False)
    return redirect(reverse('todolist:detail', args=[str(date)]))
def delete(request,date):
    if request.method == "POST":
        obj = Day.objects.get(day=date)
        task_id = request.POST.get('task_id')
        dele = Todo.objects.get(id=task_id)
        dele.delete()
    return redirect(reverse('todolist:detail', args=[str(date)]))

# Create your views here.
