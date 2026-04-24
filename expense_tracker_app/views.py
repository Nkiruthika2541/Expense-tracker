from django.shortcuts import render,redirect
from django.http import HttpResponse
from expense_tracker_app.forms import ExpenseForm, CategoryForm
from expense_tracker_app.models import AddExpense, AddCategory

# Create your views here.
def home(request):
  expense = AddExpense.objects.all()
  category = AddCategory.objects.all()
  return render(request,'home.html',{'expense':expense,'category':category})
  
  
def new_expense(request):
  if request.method == 'POST':
    form = ExpenseForm(request.POST)
    if form.is_valid():  
      form.save()
      return redirect('home')
  else:
    form = ExpenseForm()
  return render(request,'expense.html',{'form':form})
  
  
def new_category(request):
  if request.method == 'POST':
    form = CategoryForm(request.POST)
    if form.is_valid():  
      form.save()
      return redirect('home')
  else:
    form = CategoryForm()
  return render(request,'category.html',{'form':form})
  