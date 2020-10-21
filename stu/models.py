from django.db import models
from django.db.models.manager import Manager


class CustomManager(Manager):
    def all(self):
        return Manager.all(self).filter(isdelete=True)


# Create your models here.
class Student(models.Model):
    sname = models.CharField(max_length=30)
    isdelete = models.BooleanField(default=False)
    objects = CustomManager()

    def __str__(self):
        return u'Student:%s'%self.isdelete
# Student.objects.all() 默认返回全表数据  但是现在打算返回indelete中=true的。这个时候就需要自定义manager
