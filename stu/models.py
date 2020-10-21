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
# Student.objects.all() 目前返回isdelete=True得了
