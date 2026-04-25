from django.urls import path
from expense_tracker_app import views


urlpatterns = [
  path('',views.home,name='home'),
  path('add-expense',views.new_expense,name='new_expense'),
  path('add-category',views.new_category,name='new_category'),
  path('update-expense/<int:exp_id>',views.update_expense,name='update_expense'),
  path('delete-expense/<int:exp_id>',views.delete_expense,name='delete_expense'),
  
  ]