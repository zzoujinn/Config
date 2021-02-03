from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection, connections
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
# Create your views here.

cursor = connection.cursor()


@csrf_exempt
def index(request):
    data = {"data": "all_data"}
    return redirect("/confcheck/key_to_values_project")


@csrf_exempt
def quick_query(request):
    if request.method == 'POST':
        print("======================================>")
        key = request.POST.get('key')
        value = request.POST.get('value')
        print(key, value)
        sql = 'SELECT n.AppId, i.`Key`, i.`Value` FROM `confcheck_item` AS i INNER JOIN confcheck_namespace AS n ON i.NamespaceId = n.Id WHERE i.`IsDeleted` = 0 and n.`IsDeleted` = 0 and `Key` like %s and `Value` like %s order by n.AppId'
        cursor.execute(sql, params=[key, value, ])
        result = cursor.fetchall()
        print(result)
        all_data = []
        for i in result:
            one_data = {}
            one_data["AppId"] = i[0]
            one_data["Key"] = i[1]
            one_data["Value"] = i[2]
            all_data.append(one_data)
        data = {
            "data": all_data
        }
        return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json;charset=utf-8")
    else:
        print("--------------------------------------->")
        data = {"data": "all_data"}
        return render(request, 'confcheck/quick_query.html', data)


@csrf_exempt
def key_to_values_project(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        print("key----->"+key)
        sql = 'SELECT n.AppId, i.`Key`, i.`Value` FROM `confcheck_item` AS i INNER JOIN confcheck_namespace AS n ON i.NamespaceId = n.Id WHERE i.`IsDeleted` = 0 and n.`IsDeleted` = 0 and `Key` like %s order by n.AppId'
        cursor.execute(sql, params=[key, ])
        result = cursor.fetchall()
        # print(result)
        all_data = []
        for i in result:
            one_data = {}
            one_data["AppId"] = i[0]
            one_data["Key"] = i[1]
            one_data["Value"] = i[2]
            all_data.append(one_data)
        data = {
            "data": all_data
        }
        # return render(request, 'confcheck/key_to_values_project.html', data)
        return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json;charset=utf-8")
    else:
        print("--------------------------------------->")
        data = {"data": "all_data"}
        return render(request, 'confcheck/key_to_values_project.html', data)


@csrf_exempt
def values_to_key_project(request):
    if request.method == 'POST':
        value = request.POST.get('value')
        print(value)
        sql = 'SELECT n.AppId, i.`Key`, i.`Value` FROM `confcheck_item` AS i INNER JOIN confcheck_namespace AS n ON i.NamespaceId = n.Id WHERE i.`IsDeleted` = 0 and n.`IsDeleted` = 0 and `Value` like %s order by n.AppId'
        cursor.execute(sql, params=[value, ])
        result = cursor.fetchall()
        print(result)
        all_data = []
        for i in result:
            one_data = {}
            one_data["AppId"] = i[0]
            one_data["Key"] = i[1]
            one_data["Value"] = i[2]
            all_data.append(one_data)
        data = {
            "data": all_data
        }
        return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json;charset=utf-8")
    else:
        print("--------------------------------------->")
        data = {"data": "all_data"}
        return render(request, 'confcheck/values_to_key_project.html', data)


@csrf_exempt
def config_check(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        print(key, value)
        sql = 'SELECT n.AppId, i.`Key`, i.`Value`, n.`DataChange_LastTime` FROM `confcheck_item` AS i INNER JOIN confcheck_namespace AS n ON i.NamespaceId = n.Id WHERE i.`IsDeleted` = 0 and n.`IsDeleted` = 0 and `Key` = %s order by n.AppId'
        cursor.execute(sql, params=[key, ])
        result = cursor.fetchall()
        print(result)
        all_data = []
        for i in result:
            one_data = {}
            one_data["AppId"] = i[0]
            one_data["Key"] = i[1]
            one_data["Value"] = i[2]
            if isinstance(i[3], datetime.datetime):
                LastChangeTime = i[3].strftime("%Y-%m-%d %H:%M:%S")
                one_data["LastChangeTime"] = LastChangeTime
            if one_data["Value"] == value:
                one_data["Check"] = "是"
            else:
                one_data["Check"] = "否"
            all_data.append(one_data)
        data = {
            "data": all_data
        }
        return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json;charset=utf-8")
    else:
        print("--------------------------------------->")
        data = {"data": "all_data"}
        return render(request, 'confcheck/config_check.html', data)






