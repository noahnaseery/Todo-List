from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=300, blank=False)


class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    todo = models.CharField(max_length=1000, blank=False)
    date_created = models.DateField(auto_now_add=True)
    todo_date = models.DateField()