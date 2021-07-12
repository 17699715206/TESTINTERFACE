from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from app.services import api

@csrf_exempt
def hello(request):
    # name = request.GET.get("name")
    # name = request.POST.get("name")
    data = request.body.decode("utf-8")
    json_data = json.loads(data)
    print(type(json_data))
    print(json_data["age"])
    age = str(json_data["age"])
    return HttpResponse("Hello,我的名字是："+json_data["name"]+age)

@csrf_exempt
def req_json(request):
    data = request.body.decode("utf-8")
    json_data = json.loads(data)
    # print(json_data)
    request_data = api().api_func(json_data)
    print(request_data)
    # return HttpResponse("接口响应时间：" +req_tima +"接口响应状态码："+req_ststus)
    return HttpResponse(str(request_data["code"])+","+str(request_data["total_seconds"]))