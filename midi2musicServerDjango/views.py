from django.http import HttpResponse
from django.template import loader
from django.shortcuts import  render
def home_view(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    return  HttpResponse()

def test_html(request):

    # home_page=loader.get_template("主页.html")
    # #html=home_page.render()
    # return HttpResponse(home_page)

    return render(request,"主页.html")

def gallery(request):
    return render(request,"探索曲库.html")

def art(request):
    return render(request,"艺术创想.html")