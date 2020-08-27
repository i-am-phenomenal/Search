from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json

@csrf_exempt
def returnSimpleResponse(request): 
    print("I AM HERE !!!!!!!!!!!!!!!")
    return JsonResponse("This is a simple response!", safe=False)