from django.db import models
from django.db.models import QuerySet
from django.db.models.manager import Manager
from . import new


class CustomManager(Manager):
    def get_queryset(self):
        return Manager.get_queryset(self).filter(isdelete=True)


class NoDeletedManager(Manager):
    def all(self):
        return Manager.all(self).filter(isdelete=False)


class BatchDelManager(Manager):
    def get_queryset(self):
        return Manager.get_queryset(list).filter(isdelete=False)

    def filter(self, *args, **kwargs):
        # 获取需要删除记录
        delList = Manager.get_queryset(self)

        # 定义闭包方法执行修改isdelete=True操作
        def delete1(delqueryset):
            for dq in delqueryset:
                dq.isdelete = True
                dq.save()
            delList.delete = new.instancemethod(delete1, delList, QuerySet)

        return delList


# Create your models here.
class Student(models.Model):
    sname = models.CharField(max_length=30)
    isdelete = models.BooleanField(default=False)

    objects = BatchDelManager()

    def __str__(self):
        return u'Student:%s' % self.isdelete

    def delete(self, using=None, keep_parents=False):
        self.isdelete = True
        self.save()
