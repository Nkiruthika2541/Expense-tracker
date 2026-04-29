from django.urls import path
from expense_tracker_app import views


urlpatterns = [
  path('',views.dashboard,name='dashboard'),
  path('add-expense',views.ExpenseCreateView.as_view(),name='expense-add'),
  path('filter-result',views.ExpenseListView.as_view(),name='expense-list'),
  path('add-category',views.new_category,name='new_category'),
  path('view-expense',views.view_expense,name='view_expense'),
  path('update-expense/<int:pk>',views.ExpenseUpdateView.as_view(),name='expense-update'),
  path('delete-expense/<int:pk>',views.ExpenseDeleteView.as_view(),name='expense-delete'),
  path('update-category/<int:catg_id>',views.update_category,name='update_category'),
  path('delete-category/<int:catg_id>',views.delete_category,name='delete_category'),
  
  ]