from django.shortcuts import render,redirect
from .forms import IndexForm,TodoForm
from django.urls import reverse
from .models import Todo,Day
from django.shortcuts import get_object_or_404
from datetime import datetime,timedelta
from django.core.paginator import Paginator

def index(request):
    import requests
    import os
    
    wheather_api_key=os.environ.get('weather_api')
    lat_lon = "36.08250810111,140.11071321223"
    url = f"http://api.weatherapi.com/v1/current.json?key={wheather_api_key}&q={lat_lon}&lang=ja"
    response = requests.get(url)
    data = response.json()
    location = data["location"]["name"]
    condition = data["current"]["condition"]["text"]
    icon = data["current"]["condition"]["icon"]
    params = {
        'title':'Todolist',
        'form':IndexForm(),
        'condition':condition,
        'icon':icon,
        'location':location
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
def create(request, date,num=1):
    if request.method == "POST":
        obj = Day.objects.get(day=date)
        d = request.POST.copy()
        d['is_done']=False
        d['selected_day']=obj
        form = TodoForm(d)
        if form.is_valid():
            task =request.POST['assignments']
            Todo.objects.create(selected_day=obj,assignments=task,is_done=False)
            return redirect(reverse('todolist:detail', args=[str(date)]))
    day_obj = get_object_or_404(Day,day=date)
    data = Todo.objects.filter(selected_day=day_obj)
    page = Paginator(data,8)
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
def delete(request,date):
    if request.method == "POST":
        task_id = request.POST.get('task_id')
        dele = Todo.objects.get(id=task_id)
        dele.delete()
    return redirect(reverse('todolist:detail', args=[str(date)]))
def select_day(request):
    if request.method == 'POST':
        form = IndexForm(request.POST)
        if form.is_valid():
            selected_date = form.cleaned_data['day']
            return redirect(reverse('todolist:detail',args=[str(selected_date)]))
# Create your views here.
