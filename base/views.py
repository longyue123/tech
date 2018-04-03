#coding=utf-8
import json
from django.shortcuts import HttpResponse
from django.views.generic import View
class BaseView(View):
    content_type="application/json"

    def render_json_response(self,context):
        return HttpResponse(json.dumps(context),self.content_type)

