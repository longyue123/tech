#coding=utf-8
from tech.models import Questions_Model
from baseLogic import BaseLogic
from django.db.models import Q
import datetime
from base import tools
import pdb
class Questions(BaseLogic):
    def __init__(self):
        BaseLogic.__init__(self)

    @staticmethod
    def add_questions(**kwargs):
        kwargs["week"]=tools.get_week(times=datetime.datetime.now())
        questions=Questions_Model.objects.create(**kwargs)
        return dict(id=questions.id)

    @staticmethod
    def update_questions(id=None,**kwargs):
        try:
            kwargs['update_time']=datetime.datetime.now()
            kwargs['week']=tools.get_week(times=datetime.datetime.now())
            Questions_Model.objects.filter(id=id).update(**kwargs)
            msg=dict(status=0,msg="update success")
        except Exception,e:
            msg=dict(status=1,msg="update failed",detail=str(e))

        return msg
    @staticmethod
    def query_questions(query_project_name=None,query_module_name=None,query_progress_name=None,query_start_date_time=None,query_end_time=None,time_week=None):

       if (query_project_name is not None and  query_project_name != ""):
           project_name_flag= Q(project=query_project_name)
       else:
           project_name_flag=Q(is_deleted=0)

       if (query_module_name is not None and  query_module_name != ""):
           module_name_flag=Q(question_module=query_module_name)
       else:
           module_name_flag=Q(is_deleted=0)

       if (query_progress_name is not None and query_progress_name != ""):
           progress_name_flag=Q(question_progress=query_progress_name)
       else:
           progress_name_flag=Q(is_deleted=0)

       if (time_week is not None and time_week != ""):
           time_week_flag=Q(week=time_week)
       else:
           time_week_flag=Q(is_deleted=0)
       # if (query_start_date_time is not None):
       #      start_time_flag=Q(create_time__gte=query_start_date_time)
       # else:
       #     start_time_flag=Q(is_deleted=0)
       #
       # if (query_end_time is not None):
       #     end_time_flag=Q(create_time__lte=query_end_time)
       # else:
       #     end_time_flag=Q(is_deleted=0)

       return Questions_Model.objects.filter(project_name_flag).filter(module_name_flag).filter(progress_name_flag).filter(time_week_flag).order_by("-create_time")

    @staticmethod
    def delete_questions(id):
        try:
            Questions_Model.objects.filter(id=id).update(is_deleted=1)
            return dict(id=id,status=0)
        except Exception,e:
            msg=e
            return dict(id=id,status=1,msg=msg)

    @staticmethod
    def get_questions_detail(id):
        return Questions_Model.objects.get(id=id)

    @staticmethod
    def get_questions_by_week(week_time):
        return Questions_Model.objects.filter(is_deleted=0).filter(week=week_time)

    @staticmethod
    def get_question_not_done():
        return Questions_Model.objects.filter(is_deleted=0).filter(question_progress__in=['New','In Progress'])

    @staticmethod
    def analysis_questions_question(time_week=None):
         all_list={}
         module_key_list=Questions_Model.objects.values("question_module").distinct()
         for obj in module_key_list:
             key=obj.get("question_module")
             total_models=Questions_Model.objects.filter(question_module=key)
             if (time_week != None):
                 total_models=total_models.filter(week=time_week)
             data={v.replace(" ","_"):len(total_models.filter(question_progress=v)) for v in tools.progress_list}
             total=sum(v for v in data.values())
             data['Total']=total
             if (total != 0):
                 resolve_time=float(data['Done']) / float(total)
             else:
                 resolve_time=0.0
             data["Resolve"]=round(resolve_time,2)
             data['Total']=total
             all_list[key]=data

         all_total=sum(v['Total'] for v in all_list.values())
         all_in_progress=sum(v['In_Progress'] for v in all_list.values())
         all_done=sum(v['Done'] for v in all_list.values())
         all_new=sum(v['New'] for v in all_list.values())
         if (all_total != 0):
             resolve_time=round(float(all_done) / float(all_total),2)
         else:
             resolve_time=0.0
         all_list['总数']=dict(Total=all_total,Done=all_done,New=all_new,In_Progress=all_in_progress,Resolve=resolve_time)
         return all_list