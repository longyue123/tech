#coding=utf-8
from django.shortcuts import render
from base.views import  BaseView
from logic.module import Module
from logic.progress import Progress
from logic.project import Project
from logic.questions import Questions
import pdb
from base import tools
from base.paginator import ToolPaginator
import datetime
def index(request):
    return render(request,"base.html")

class AddQuestions(BaseView):
    def get(self,request,**kwargs):
        module_list=Module().get_module("module_name")
        project_list=Project().get_progect("project_name")
        progress_list=Progress().get_progress("progress_name")
        response_data=dict(module_list=module_list,project_list=project_list,progress_list=progress_list)
        return render(request,"questions/add.html",response_data)

    def post(self,request,**kwargs):
        body=request.body
        body=eval(body)
        questions=Questions.add_questions(**body)
        return self.render_json_response(questions)

class QuestionsList(BaseView,ToolPaginator):
    def get(self,request,**kwargs):
        project_name=request.GET.get("project_name",None)
        module_name=request.GET.get("module_name",None)
        progress_name=request.GET.get("progress_name",None)
        start_time=request.GET.get("start_time",None)
        end_time=request.GET.get("end_time",None)
        page=request.GET.get("page",1)
        page_size=request.GET.get("page_size",10)

        data=Questions.query_questions(query_project_name=project_name,query_end_time=end_time,query_module_name=module_name,query_progress_name=progress_name,query_start_date_time=start_time)

        module_list = Module().get_module("module_name")
        project_list = Project().get_progect("project_name")
        progress_list = Progress().get_progress("progress_name")

        data,paginator=self.paginate(data,page_size=page_size,page=page)

        response_data = dict(module_list=module_list, project_list=project_list, progress_list=progress_list,questions_list=data,paginator=paginator)

        return render(request,"questions/list.html",response_data)

class QuestionsDetail(BaseView):
    def get(self,request,**kwargs):

        question_id=kwargs.get("question_id",None)
        response_obj=Questions.get_questions_detail(id=question_id)

        module_list = Module().get_module("module_name")
        project_list = Project().get_progect("project_name")
        progress_list = Progress().get_progress("progress_name")
        response_data = dict(module_list=module_list, project_list=project_list, progress_list=progress_list,question_detail=response_obj)
        return render(request,"questions/edit.html",response_data)

    def post(self,rquest,**kwargs):
        pass

class QuestionsEdit(BaseView):
    def post(self,request):
        body=request.body
        body=eval(body)
        id=body.pop("id")
        msg=Questions.update_questions(id,**body)
        return self.render_json_response(msg)


class QuestionsReport(BaseView):
    def get(self,request):
        now_time=datetime.datetime.now()
        now_week=tools.get_week(times=now_time)

        now_week_questions=Questions.analysis_questions_question(now_week)
        all_questions=Questions.analysis_questions_question()
        not_done_questions=list(Questions.get_question_not_done())
        return render(request,"questions/report.html",dict(now_week_questions=now_week_questions,not_done_questions=not_done_questions,all_questions=all_questions))

class QuestionListByModule(BaseView,ToolPaginator):
    def get(self,request):

        module_name=request.GET.get("module_name",None)
        now_week = request.GET.get("now_week",None)
        if (now_week != None and int(now_week) == 1):
            time_week=tools.get_week(times=datetime.datetime.now())
        else:
            time_week=None
        data=Questions.query_questions(query_module_name=module_name,time_week=time_week)


        module_list = Module().get_module("module_name")
        project_list = Project().get_progect("project_name")
        progress_list = Progress().get_progress("progress_name")
        page = request.GET.get("page", 1)
        page_size = request.GET.get("page_size", 10)

        data, paginator = self.paginate(data, page_size=page_size, page=page)

        response_data = dict(module_list=module_list, project_list=project_list, progress_list=progress_list,
                             questions_list=data, paginator=paginator)
        return render(request, "questions/list.html", response_data)

class SendReport(BaseView):
    def get(self,request):
        now_time = datetime.datetime.now()
        now_week = tools.get_week(times=now_time)

        now_week_questions = Questions.analysis_questions_question(now_week)
        all_questions = Questions.analysis_questions_question()
        not_done_questions = list(Questions.get_question_not_done())

        send_content=dict(now_week_questions=now_week_questions,not_done_questions=not_done_questions,all_questions=all_questions)
        tools.send_week_report(send_content)
        return self.render_json_response(dict(status=0,msg='success'))
