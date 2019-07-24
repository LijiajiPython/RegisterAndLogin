import re
from django import template
import time,datetime

register=template.Library()

@register.filter(name="setTime")
def SetTime(value):
    birthtime=re.findall(r"(\d{2,4}).*?(\d{1,2}).*?(\d{1,2})",value)
    birtime=[]
    for i in birthtime:
        birtime.append(int(i[0]))
        birtime.append(int(i[1]))
        birtime.append(int(i[2]))
        # print(birtime)
    btime="%s-%s-%s"%(birtime[0],birtime[1],birtime[2])
    nowtime = time.time()
    # print(nowtime)
    btimeArray = time.strptime(btime, "%Y-%m-%d")
    btimeStamp = float(time.mktime(btimeArray))
    agetime=nowtime-btimeStamp
    # print(btimeStamp)
    # print(agetime)
    age=int(agetime/(365*24*60*60))
    if age>=1 and age<=12:
        level="少年"
    elif age >=13 and age <= 22:
        level = "青年"
    elif age >= 23 and age <=35:
        level = "壮年"
    elif age >= 36 and age <= 45:
        level = "中年"
    elif age >= 46 and age <= 60:
        level = "老年"
    elif age >= 60 and age <= 100:
        level = "太古"
    else:
        level="未知"
    # print(age)
    return level


@register.tag(name="addNum")
def addNum(parser,token):
    try:
        content=token.split_contents()
        tag_name,tag_content=content
    except ValueError as e:
        msg=str(e)
        raise template.TemplateSyntaxError(msg)
    return AddNum(tag_content)

class AddNum(template.Node):
    def __init__(self,format_string):
        self.format_string=format_string
    def render(self,context):
        # result=int(self.format_string)+1
        result=self.format_string+"叭叭叭"
        return result