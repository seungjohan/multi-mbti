from django.shortcuts import render

# Create your views here.

def mbti(request):
    return render (request, 'mbti.html')