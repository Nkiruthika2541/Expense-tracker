from django.db.models import Sum, Avg, Min, Max
from django.utils import timezone
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from expense_tracker_app.forms import ExpenseForm, CategoryForm
from expense_tracker_app.models import AddExpense, AddCategory

# FUNCTION BASED VIEWS

  # HOME PAGE / DASHBOARD
def dashboard(request):
  total_spent = AddExpense.objects.aggregate(t=Sum('amount'))
  all_categories = AddCategory.objects.all()
  today = timezone.now().date()
  now_month = timezone.now().month
  recent_expenses = AddExpense.objects.filter(date__lte=today).order_by('-date')
  return render(request,'dashboard.html',{'total_spent':total_spent,'all_categories':all_categories,'expenses':recent_expenses})

  # VIEW ALL EXPENSES
def view_expense(request):
  expense = AddExpense.objects.all()
  return render(request,'view_expense.html',{'expense':expense})
  
  
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
  return render(request,'update_category.html',{'form':form})
  
  # DELETE CATEGORY
def delete_category(request,catg_id):
  required_category = get_object_or_404(AddCategory,id = catg_id)
  if request.method == 'POST':
    required_category.delete()
    return redirect('dashboard')
  
  return render(request,'delete_category.html',{'form':required_category})


  # LOGIN
  # REGISTER NEW USER 
  
  
  
# CLASS BASED VIEWS

# EXPENSE
  
  # LIST
class ExpenseListView(View):  
  
  def get_queryset(self,request):  
    queryset = AddExpense.objects.select_related('category').order_by('-date')
    
    category = request.GET.get('category')
    min_amount = request.GET.get('min')
    max_amount = request.GET.get('max')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    month = request.GET.get('month')
    year = request.GET.get('year')
    
    if category:
      queryset = queryset.filter(category_id= category)
      
    if min_amount:
      queryset = queryset.filter(amount__gte = min_amount)
      
    if max_amount:
      queryset = queryset.filter(amount__lte = max_amount)
      
    if start_date:
      queryset = queryset.filter(date__gte = start_date)
      
    if end_date:
      queryset = queryset.filter(date__lte = end_date)
      
    if month:
      queryset = queryset.filter(date__month = month)
      
    if year:
      queryset = queryset.filter(date__year = year)
      
    return queryset
    
  def get(self,request):  
    expense = self.get_queryset(request)
    categories = AddCategory.objects.all()
    
    return render(request,'filter.html',{'expense':expense,'categories':categories,'filters':request.GET})
  
  
  # CREATE
class ExpenseCreateView(View): 
  
  def get(self,request):  
    form = ExpenseForm()
    return render(request,'expense.html',{'form':form})
  
  def post(self,request):  
    form = ExpenseForm(request.POST)
    if form.is_valid():  
      form.save()
      return redirect('dashboard')
    return render(request,'expense.html',{'form':form})
    
  # UPDATE
class ExpenseUpdateView(View):
  
  def get_object(self,pk):  
    return get_object_or_404(AddExpense,pk = pk)
    
  def get(self,request,pk):  
    expense = self.get_object(pk)
    form = ExpenseForm(instance = expense)
    return render(request,'update_expense.html',{'form':form})
  
  def post(self,request,pk):  
    expense = self.get_object(pk)
    form = ExpenseForm(request.POST,instance = expense)
    if form.is_valid():  
      form.save()
      return redirect('dashboard')
    return render(request,'update_expense.html',{'form':form})
    
  # DELETE 
class ExpenseDeleteView(View):
  
  def get_object(self,pk):  
    return get_object_or_404(AddExpense,pk = pk)
  
  def get(self,request,pk):  
    expense = self.get_object(pk)
    return render(request,'delete_expense.html',{'expense' : expense})
  
  def post(self,request,pk):  
    expense = self.get_object(pk)
    expense.delete()
    return redirect('dashboard')

# CATEGORY
  # CREATE
  # UPDATE
  # DELETE 
  
  # FILTER 