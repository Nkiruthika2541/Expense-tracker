from django.urls import path
from expense_tracker_app import views


urlpatterns = [
  path('',views.dashboard,name='dashboard'),
  path('add-expense',views.new_expense,name='new_expense'),
  path('add-category',views.new_category,name='new_category'),
  path('view-expense',views.view_expense,name='view_expense'),
  path('update-expense/<int:exp_id>',views.update_expense,name='update_expense'),
  path('delete-expense/<int:exp_id>',views.delete_expense,name='delete_expense'),
  path('update-category/<int:catg_id>',views.update_category,name='update_category'),
  path('delete-category/<int:catg_id>',views.delete_category,name='delete_category'),
  
  ]