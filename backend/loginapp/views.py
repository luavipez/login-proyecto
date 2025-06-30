from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(username= username, password= password)
        if user is not None:
            return json.response({'status': 'ok'})
        else:
            return json.response({'status': 'fail'}, status=401) 