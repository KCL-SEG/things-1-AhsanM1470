from django.shortcuts import render

def init_view(request):
    return render(request, 'things.html')