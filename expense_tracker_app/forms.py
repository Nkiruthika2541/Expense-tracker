from django import forms
# from django.contrib.auth.models import User
from expense_tracker_app.models import AddExpense,AddCategory



class ExpenseForm(forms.ModelForm):
  class Meta:
    model = AddExpense
    fields = ['amount','category','date','description']
    widgets = {
      'date' : forms.DateInput( attrs = {
        'class' : 'form-control',
        'type' : 'date'
      }),
      'description' : forms.Textarea( attrs = {
        'rows' : 4,
        'cols' : 20
      })
    }
    
    
class CategoryForm(forms.ModelForm):
  class Meta:
    model = AddCategory
    fields = '__all__'