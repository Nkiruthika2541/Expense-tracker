from django.db import models
# from django.contrib.auth.models import User
# Create your models here.


class AddCategory(models.Model):
  name = models.CharField(max_length = 255)  
  # user = models.ForeignKey(User, on_delete = models.CASCADE)  
  
  def __str__(self):
    return self.name



class AddExpense(models.Model):
  # user = models.ForeignKey(User, on_delete = models.CASCADE)  
  amount = models.DecimalField(max_digits=10,decimal_places=3)
  category = models.ForeignKey(AddCategory, on_delete = models.SET_NULL, null = True, blank = True)
  date = models.DateField()
  description = models.TextField(null = True,blank = True)
  created_at = models.DateTimeField(auto_now_add = True)
  
  def __str__(self):
    return f"{self.amount} - {self.category}"
  
  
