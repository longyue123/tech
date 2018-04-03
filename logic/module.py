#coding=utf-8
from tech.models import Module_Model
from logic.baseLogic import BaseLogic
class Module(BaseLogic):
    def __init__(self):
        BaseLogic.__init__(self)


    def get_module(self,data=None):
        return self.get_base_data(Module_Model,data)
