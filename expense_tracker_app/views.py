from django.db.models import Sum, Avg, Min, Max
from django.utils import timezone
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from expense_tracker_app.forms import ExpenseForm, CategoryForm, BudgetForm 
from expense_tracker_app.models import AddExpense, AddCategory, AddBudget

# FUNCTION BASED VIEWS
def get_expense():  
  return AddExpense.objects.all()

def get_category():  
  return AddCategory.objects.all()

def get_budget():  
  return AddBudget.objects.all()


  # HOME PAGE / DASHBOARD
def dashboard(request):
  total_spent = get_expense().aggregate(t=Sum('amount'))
  total_budget = get_budget().aggregate(t=Sum('amount'))
  
  all_categories = get_category()
  budget = get_budget()
  
  today = timezone.now().date()
  now_month = timezone.now().month
  now_year = timezone.now().year
  
  recent_expenses = get_expense().filter(date__lte=today).order_by('-date')
  
  categories = get_category()

  result = []
  
  for cat in categories:
    spent = get_expense().filter(category=cat) \
        .aggregate(total=Sum('amount'))['total'] or 0
  
    budget_obj = get_budget().filter(category = cat).first()
    budget = budget_obj.amount if budget_obj else 0
    
    savings = budget - spent 
    
    result.append({
      'name': cat.name,
      'spent': spent,
      'budget': budget,
      'savings': savings
    })
  
  
  return render(request,'dashboard.html',{'total_spent':total_spent,'total_budget':total_budget,'all_categories':all_categories,'expenses':recent_expenses,'result':result})

  # VIEW ALL EXPENSES
def view_expense(request):
  expense = AddExpense.objects.all()
  return render(request,'Expense/view_expense.html',{'expense':expense})
  
  
  # ADD CATEGORY
def new_category(request):
  if request.method == 'POST':
    form = CategoryForm(request.POST)
    if form.is_valid():  
      form.save()
      return redirect('dashboard')
  else:
    form = CategoryForm()
  return render(request,'Category/category.html',{'form':form})
  
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
  return render(request,'Category/update_category.html',{'form':form})
  
  # DELETE CATEGORY
def delete_category(request,catg_id):
  required_category = get_object_or_404(AddCategory,id = catg_id)
  if request.method == 'POST':
    required_category.delete()
    return redirect('dashboard')
  
  return render(request,'Category/delete_category.html',{'form':required_category})


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
    return render(request,'Expense/expense.html',{'form':form})
  
  def post(self,request):  
    form = ExpenseForm(request.POST)
    if form.is_valid():  
      form.save()
      return redirect('dashboard')
    return render(request,'Expense/expense.html',{'form':form})
    
  # UPDATE
class ExpenseUpdateView(View):
  
  def get_object(self,pk):  
    return get_object_or_404(AddExpense,pk = pk)
    
  def get(self,request,pk):  
    expense = self.get_object(pk)
    form = ExpenseForm(instance = expense)
    return render(request,'Expense/update_expense.html',{'form':form})
  
  def post(self,request,pk):  
    expense = self.get_object(pk)
    form = ExpenseForm(request.POST,instance = expense)
    if form.is_valid():  
      form.save()
      return redirect('dashboard')
    return render(request,'Expense/update_expense.html',{'form':form})
    
  # DELETE 
class ExpenseDeleteView(View):
  
  def get_object(self,pk):  
    return get_object_or_404(AddExpense,pk = pk)
  
  def get(self,request,pk):  
    expense = self.get_object(pk)
    return render(request,'Expense/delete_expense.html',{'expense' : expense})
  
  def post(self,request,pk):  
    expense = self.get_object(pk)
    expense.delete()
    return redirect('dashboard')

# BUDGET
  # CREATE
class BudgetCreateView(View):
  
  def get(self,request):  
    form = BudgetForm()
    return render(request,'Budget/budget.html',{'form':form})
    
  def post(self,request):  
    form = BudgetForm(request.POST)
    if form.is_valid():  
      form.save()
      return redirect('dashboard')
    return render(request,'Budget/budget.html',{'form':form})

  # UPDATE
  # DELETE 
  
