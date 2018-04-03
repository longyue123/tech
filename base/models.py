# coding=utf-8
from django.db import models

class NotDeletedManager(models.Manager):
    """获取没有删掉的数据"""
    def get_queryset(self):
        return super(NotDeletedManager, self).get_queryset().filter(is_deleted=False)

class BaseModel(models.Model):
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True, blank=True)
    is_deleted = models.BooleanField(u'是否删除', default=False)

    objects = models.Manager()
    not_deleted_objects = NotDeletedManager()

    class Meta:
        abstract = True
        ordering = ['-create_time']
