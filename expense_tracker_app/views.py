from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from expense_tracker_app.forms import ExpenseForm, CategoryForm
from expense_tracker_app.models import AddExpense, AddCategory

  # HOME PAGE
def home(request):
  expense = AddExpense.objects.all()
  category = AddCategory.objects.all()
  return render(request,'home.html',{'expense':expense,'category':category})
  
  # ADD EXPENSE
def new_expense(request):
  if request.method == 'POST':
    form = ExpenseForm(request.POST)
    if form.is_valid():  
      form.save()
      return redirect('home')
  else:
    form = ExpenseForm()
  return render(request,'expense.html',{'form':form})
  
  # ADD CATEGORY
def new_category(request):
  if request.method == 'POST':
    form = CategoryForm(request.POST)
    if form.is_valid():  
      form.save()
      return redirect('home')
  else:
    form = CategoryForm()
  return render(request,'category.html',{'form':form})
  
  # UPDATE EXPENSE
def update_expense(request,exp_id):
  required_expense = get_object_or_404(AddExpense,id = exp_id)
  if request.method == 'POST':
    form = ExpenseForm(request.POST,instance = required_expense)
    if form.is_valid():  
      form.save()
      return redirect('home')
  else:
    form = ExpenseForm(instance = required_expense)
  return render(request,'updateexpense.html',{'form':form})
  
  # DELETE EXPENSE
def delete_expense(request,exp_id):
  required_expense = get_object_or_404(AddExpense,id = exp_id)
  if request.method == 'POST':
    required_expense.delete()
    return redirect('home')
  
  return render(request,'deleteexpense.html',{'form':required_expense})
  # DELETE CATEGORY
  # LOGIN
  # REGISTER NEW USER 
  