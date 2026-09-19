from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return render(request, "index.html")

@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"detail": "POST required"}, status=405)
    data = json.loads(request.body or "{}")
    user = authenticate(username=data.get("username"), password=data.get("password"))
    if not user:
        return JsonResponse({"detail": "Invalid username or password"}, status=400)
    login(request, user)
    return JsonResponse({"id": user.id, "username": user.username, "role": user.role})

def me(request):
    if not request.user.is_authenticated:
        return JsonResponse({"authenticated": False}, status=401)
    return JsonResponse({"authenticated": True, "id": request.user.id, "username": request.user.username, "role": request.user.role})

@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"success": True})
