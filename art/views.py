from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "艺术创想.html")
