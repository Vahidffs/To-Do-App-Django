from django.db import models

class ToDo(models.Model):
    todoitem = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)


    def __str__(self):
        return self.todoitem