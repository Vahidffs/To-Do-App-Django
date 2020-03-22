from django import forms

class TodoForm(forms.Form):
    todoitem = forms.CharField(max_length=40,
    widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Enter ToDo e.g. Delete Junk File', 'aria-label':'ToDo','ariadescribeby':'add-btn'}
    ))
