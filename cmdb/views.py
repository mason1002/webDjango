from django.shortcuts import render
# from django.shortcuts import HttpResponse
from cmdb import models
# Create your views here.
#
# user_list = [
#     {"user": "jack", "pwd": "abc"},
#     {"user": "tom", "pwd": "ABC"},
# ]


def index(request):
    # return HttpResponse("hi")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # temp = {"user": username, "pwd": password}
        # user_list.append(temp)
        # print(username, password)
        models.UserInfo.objects.create(user=username, pwd=password)
    user_list = models.UserInfo.objects.all()

    return render(request, "index.html", {"data": user_list})
