#coding=utf-8
from tech.models import Project_Model
from logic.baseLogic import BaseLogic
class Project(BaseLogic):
    def __init__(self):
        BaseLogic.__init__(self)

    def get_progect(self,data=None):
        return self.get_base_data(Project_Model,data=data)

