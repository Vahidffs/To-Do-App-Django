from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('add', views.addToDo,name='add'),
    path('complete/<todo_id>',views.completeToDo,name="complete"),
    path('deleteComplete',views.deleteCompleted,name="deleteComplete"),
    path('deleteAll',views.deleteAll,name="deleteAll")
]