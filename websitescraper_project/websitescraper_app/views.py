from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from .models import Links
# Create your views here.
def home(request):
     if request.method=='POST':
          enterlink=request.POST.get('data','')
          urls=requests.get(enterlink)
          bs=BeautifulSoup(urls.text,'html.parser')
          for i in bs.find_all('a'):
               linkaddress=i.get('href')
               linkname=i.string
               Links.objects.create(linkaddress=linkaddress,linkname=linkname)
          return redirect('/')
     else:
          data=Links.objects.all()
          return render(request,'home.html',{'data':data})
