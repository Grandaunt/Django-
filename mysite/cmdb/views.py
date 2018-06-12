from django.shortcuts import render
from cmdb import models
from django.shortcuts import HttpResponse
# Create your views here.
user_list = [
    {"user":"jack","pwd":"abc"},
    {"user":"tom","pwd":"ABC"},
]
def index(request):
    # request.POST
    # request.GET
    # return HttpResponse("Hello world!")

    if request.method == "POST":
         username = request.POST.get("username",None)
         password = request.POST.get("password",None)
         # 添加到数据库
         models.UserInfo.objects.create(user=username,pwd=password)

         # temp = {"user":username,"pwd":password}
         # user_list.append(temp)
         # print(username,password)
    # 从数据库中读取数据
    user_list = models.UserInfo.objects.all()
    return render(request,"index.html",{"data":user_list})
