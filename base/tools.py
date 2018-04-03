#coding=utf-8
from django.core.serializers import serialize
import json
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pdb
from django.template import Context
from django.template.loader import get_template
def id_to_dict(obj_dict,value):
    obj_dict.update(id=value)

def serialize_queryset(obj):
    obj_list = [id_to_dict(partial_item.get('fields'), partial_item.get('pk'))
                for partial_item in json.loads(serialize(obj,use_natural_foreign_keys=True))]
    return obj_list

def get_week(time_stramt="%Y-%m-%d %H:%M:%S",times=None):
    times=str(times)
    t=datetime.datetime.strptime(times.split(".")[0],time_stramt)
    return times.split("-")[0] + "_wk_" + t.strftime("%W")


def send_week_report(content,to=None,subject=u"问题总结报告"):
    week_template_report=get_template("send_week_report.html")
    c=Context(content)
    email_body=week_template_report.render(c)
    send_email(email_body,to,subject)

def send_email(content,to,subject):
    try:
            smtp_obj = smtplib.SMTP_SSL()
            smtp_obj.connect(SMTP_HOST, SMTP_PORT)
            smtp_obj.login(MAIL_USER, MAIL_PASSWORD)
            msg = MIMEMultipart()
            # 构造邮件内容
            msg.attach(MIMEText(content, _subtype='html', _charset='gbk'))
            msg['Subject'] =subject
            msg['from'] = MAIL_USER
            msg['To'] = to

            smtp_obj.sendmail(MAIL_USER, to, msg.as_string())
    except Exception, e:
        print(e)

progress_list=['New','In Progress','Done']
SMTP_HOST ='smtp.qq.com'
SMTP_PORT = 465
MAIL_USER ='XXX@qq.com'
MAIL_PASSWORD = 'password'