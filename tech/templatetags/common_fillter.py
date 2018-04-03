#coding=utf-8
from django.template import Library
import json
import time
register=Library()
import pdb
# 将字符串转为json
@register.filter
def convert_string_to_json(params):
    if (params is not None and str(params) != ""):
        return json.loads(params)
    else:
        return params

# 将dateime转为
@register.filter
def convert_date_time_to_str(data=None,format="%Y-%m-%d"):
    return data.strftime(format)

# 计算长度
def count_dict_length(list_data=None):
    return len(list_data)
