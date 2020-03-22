from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .models import ToDo
from .forms import TodoForm
def index(request):

    todo_list = ToDo.objects.order_by('id')
    form = TodoForm()
    context= {
        'todo_list' : todo_list,
        'form': form

    }
    return render(request, 'ToDo/index.html',context)
@require_POST
def addToDo(request):
    form =TodoForm(request.POST)
    if form.is_valid():
        new_todo = ToDo(todoitem=form.cleaned_data['todoitem'])
        new_todo.save()

    return redirect('index')    
def completeToDo(request,todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')
def deleteCompleted(request):
    completed_items = ToDo.objects.filter(complete__exact=True)
    completed_items.delete()

    return redirect('index')
def deleteAll(request):
    ToDo.objects.all().delete()

    return redirect('index')