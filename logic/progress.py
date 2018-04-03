#coding=utf-8

from tech.models import Progress_Model
from logic.baseLogic import BaseLogic
class Progress(BaseLogic):
    def __init__(self):
        pass

    def get_progress(self,data):
        return self.get_base_data(Progress_Model,data=data)