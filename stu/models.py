from django.db import models


# Create your models here.
class Student(models.Model):
    sname = models.CharField(max_length=30)
    isdelete = models.BooleanField(default=False)

# Student.objects.all() 默认返回全表数据  但是现在打算返回indelete中=true的。这个时候就需要自定义manager
