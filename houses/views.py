from django.shortcuts import render

# Create your views here.
def houseviewrenderer(request):
     return render(request,'house.html')
