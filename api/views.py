from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .models import User

# Create your views here.
def users(request):
    if request.method == "GET":
        return JsonResponse(list(User.objects.all().values()), safe=False)

@csrf_exempt
def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        newUser = User(username=data["username"])
        newUser.save()
        return HttpResponse("Success")
    else:
        return HttpResponse("Invalid method")
    
@csrf_exempt
def delete(request):
    if request.method == "POST":
        data = json.loads(request.body)
        User.objects.filter(username = data["username"]).delete()
        return HttpResponse("Success")
    else:
        return HttpResponse("Invalid method")
    
@csrf_exempt
def match(request):
    if request.method == "POST":
        data = json.loads(request.body) 
        user1 = User.objects.filter(username = data["username1"])[0]
        user2 = User.objects.filter(username = data["username2"])[0]

        user1.wins += 1 if data["left"] == 5 else 0
        user1.losses += 1 if data["right"] == 5 else 0
        user1.kills += data["left"]
        user1.deaths += data["right"]

        user1.save()

        user2.wins += 1 if data["right"] == 5 else 0
        user2.losses += 1 if data["left"] == 5 else 0
        user2.kills += data["right"]
        user2.deaths += data["left"]

        user2.save()
        return HttpResponse("Success")
    else:
        return HttpResponse("Invalid method")