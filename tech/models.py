#coding=utf-8
from base.models import BaseModel
from django.db import models

class Questions_Model(BaseModel):
    project=models.CharField(u'所属项目',max_length=200,blank=False)
    question_desc=models.TextField(u'问题描述',blank=True)
    question_reason=models.TextField(u'产生问题原因',blank=True)
    question_module=models.CharField(u'问题所属模块',max_length=200,blank=False)
    question_reporter=models.CharField(u'提出问题人',max_length=200,blank=False)
    question_answer=models.CharField(u'问题跟进者',max_length=200,blank=False)
    question_progress=models.CharField(u'问题进度',max_length=200,blank=False)
    question_comments=models.CharField(u'问题备注',max_length=200,blank=False)
    is_system_cause=models.CharField(u'是否系统问题',max_length=200,blank=False)
    week=models.CharField(u'week',max_length=200,blank=False)

    class Meta:
        verbose_name = u'问题列表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{project} {question_desc} {question_reason} {question_module} {question_reporter} {question_answer} {question_progress} {question_comments} {is_system_cause} {week}'.format(
            project=self.project,
            question_desc=self.question_desc,
            question_reason=self.question_reason,
            question_module=self.question_module,
            question_reporter=self.question_reporter,
            question_answer=self.question_answer,
            question_progress=self.question_progress,
            question_comments=self.question_comments,
            is_system_cause=self.is_system_cause,
            week=self.week
        )

class Project_Model(BaseModel):
    project_name=models.CharField(u'项目名称',max_length=200,blank=False)


class Module_Model(BaseModel):
    module_name=models.CharField(u'模块名称',max_length=200,blank=True)

class Progress_Model(BaseModel):
    progress_name=models.CharField(u'进度名称',max_length=200,blank=True)

