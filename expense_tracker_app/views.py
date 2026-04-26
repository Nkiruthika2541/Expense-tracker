from django.db.models import Sum, Avg, Min, Max
from django.utils import timezone
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from expense_tracker_app.forms import ExpenseForm, CategoryForm
from expense_tracker_app.models import AddExpense, AddCategory

  # HOME PAGE / DASHBOARD
def dashboard(request):
  total_spent = AddExpense.objects.aggregate(t=Sum('amount'))
  all_categories = AddCategory.objects.all()
  today = timezone.now().date()
  recent_expenses = AddExpense.objects.filter(date__lte=today).order_by('-date')[:10]

  return render(request,'dashboard.html',{'total_spent':total_spent,'all_categories':all_categories,'expenses':recent_expenses})

  # VIEW ALL EXPENSES
def view_expense(request):
  expense = AddExpense.objects.all()
  return render(request,'view_expense.html',{'expense':expense})
  
  # ADD EXPENSE
def new_expense(request):
  if request.method == 'POST':
    form = ExpenseForm(request.POST)
    if form.is_valid():  
      form.save()
      return redirect('dashboard')
  else:
    form = ExpenseForm()
  return render(request,'expense.html',{'form':form})
  
  # ADD CATEGORY
def new_category(request):
  if request.method == 'POST':
    form = CategoryForm(request.POST)
    if form.is_valid():  
      form.save()
      return redirect('dashboard')
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
      return redirect('dashboard')
  else:
    form = ExpenseForm(instance = required_expense)
  return render(request,'updateexpense.html',{'form':form})
  
  # DELETE EXPENSE
def delete_expense(request,exp_id):
  required_expense = get_object_or_404(AddExpense,id = exp_id)
  if request.method == 'POST':
    required_expense.delete()
    return redirect('dashboard')
  
  return render(request,'deleteexpense.html',{'form':required_expense})
  
  # UPDATE EXSISTING CATEGORY
def update_category(request,catg_id):
  required_category = get_object_or_404(AddCategory,id = catg_id)
  if request.method == 'POST':
    form = CategoryForm(request.POST,instance = required_category)
    if form.is_valid():  
      form.save()
      return redirect('dashboard')
  else:
    form = CategoryForm(instance = required_category)
  return render(request,'updatecategory.html',{'form':form})
  
  # DELETE CATEGORY
def delete_category(request,catg_id):
  required_category = get_object_or_404(AddCategory,id = catg_id)
  if request.method == 'POST':
    required_category.delete()
    return redirect('dashboard')
  
  return render(request,'deletecategory.html',{'form':required_category})


  # LOGIN
  # REGISTER NEW USER 
  