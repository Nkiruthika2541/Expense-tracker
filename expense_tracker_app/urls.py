from django.urls import path
from expense_tracker_app import views


urlpatterns = [
  path('',views.home,name='home'),
  path('add-expense',views.new_expense,name='new_expense'),
  path('add-category',views.new_category,name='new_category'),
  ]