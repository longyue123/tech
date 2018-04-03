#coding=utf-8
import pdb

class BaseLogic(object):
    def __init__(self):
        pass

    def get_base_data(self,model_name=None,data=None):
        all_objects = list(model_name.objects.filter(is_deleted=0))
        if (data is  None):
            return all_objects
        else:
            return list(v.__dict__[data]  for v in  all_objects)