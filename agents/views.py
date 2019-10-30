from django.shortcuts import render, get_object_or_404
from .models import Mock
from django.db.models import Q

def home(request):
    all=Mock.objects.all()
    return render(request,"home.html",{'all':all})
def market(request):
    all=Mock.objects.all()
    return render(request,"market.html",{'all':all})
def blog(request):
    return render(request,"blog.html")
def agent(request, id=None):
    print(id)
    ai=get_object_or_404(Mock, id=id)
    return render(request,"agents/agent.html",{"agent":ai})
def search(request):
    print(request.GET)
    params=request.GET
    query=params.get('q')
    queryset=Mock.objects.none()
    if query:
        queryset=Mock.objects.filter(Q(nume__icontains=query) | Q(description__icontains=query))
    context={'all':queryset}
    print("chiu este" +query)
    return render(request,"search.html",context)
def appmarket(request):
    all=Mock.objects.all()
    return render(request,"appmarket.html",{'all':all})
