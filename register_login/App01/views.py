from django.shortcuts import render
from App01.models import User
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views import View
# Create your views here.
def index(request):
    cookiename=request.COOKIES.get("username")
    sessionname=request.session.get("username")
    if cookiename:
        if sessionname:
            theuser=User.objects.filter(username=sessionname).first()
            if theuser:
                return render(request,"app01/index.html")
    return render(request,"app01/login.html")

def register(request):
    result={"content":"","status":"error"}
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if username and password:
            name = User.objects.filter(username=username).first()
            if name:
                result["content"] = "用户名已存在"
            else:
                users=User()
                users.username=username
                users.password=password
                users.save()
                result["content"]="注册成功"
                result["status"]="success"
                return render(request,"app01/login.html",locals())
        else:
            result["content"]="用户名或密码不能为空"
    return render(request,"app01/register.html",locals())

def register_data(request):
    result = {"status": "error", "content": ""}
    username = request.GET.get("username")
    if username:
        name = User.objects.filter(username=username).first()
        # name=Students.objects.filter(username=username).first()
        if name:
            result["content"] = "用户名已存在"
        else:
            result["status"] = "success"
            result["content"] = "可以使用的用户名"
    else:
        result["content"] = "用户名不能为空"
    print(result)
    return JsonResponse(result)

def login(request):
    result={"content":"","status":"error"}
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if username and password:
            theuser=User.objects.filter(username=username).first()
            if theuser:
                if theuser.password==password:
                    result["content"]="登陆成功"
                    result["status"]="success"
                    request.session["username"] = username
                    request.session["is_login"] = True
                    response = render(request, "app01/index.html",locals())
                    response.set_cookie("username", username)
                    return response
                else:
                    result["content"]="密码错误"
            else:
                result["content"]="用户名不存在"
        else:
            result["content"]="用户名或密码不能为空"
    return render(request,"app01/login.html",locals())

def logout(request):
    response = HttpResponseRedirect("/App01/login/")
    response.delete_cookie("username")
    del request.session["username"]
    del request.session["is_login"]
    return response


def howold(request):
    people=[
        {"name":"张三","birthday":"1996-10-31"},
        {"name":"李四","birthday":"1997年11月10日"},
        {"name":"王五","birthday":"1975-2-22"},
        {"name":"赵六","birthday":"1977-10-30"},
        {"name":"周七","birthday":"1980-02-05"},
    ]
    a=12
    return render(request,"app01/howold.html",locals())

class ViewsClass(View):
    def get(self,request):
        return HttpResponse("这是get请求")
    def post(self,request):
        return HttpResponse("这是post请求")
    def put(self,request):
        return HttpResponse("这是put请求")


class LoginUserApi(View):
    def get(self,request):
        result={"static":"400","data":""}
        data=request.GET
        if data:
            types=data.get("type")
            if types =="get":
                id=data.get("id")
                if id:
                    try:
                        user=User.objects.get(id=int(id))
                        db_data=[{"username":user.username,"password":user.password}]
                        result["status"]=200
                        result["data"]=db_data
                    except Exception as e:
                        result["data"]=str(e)
                else:
                    result["data"]="id为空"
            elif types=="select":
                db_data=[{"username":user.username,"password":user.password}for user in User.objects.all()]
                result["status"]=200
                result["data"]=db_data
            else:
                result["data"]="不是合法请求"
        else:
            result["data"]="请求数据为空"
        return JsonResponse(result)

def onlyHtml(requset):
    return render(requset,"app01/onlyHtml.html")


def VueHtml(request):
    return render(request, "app01/vueHtml.html")