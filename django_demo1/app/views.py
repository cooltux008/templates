from django.shortcuts import render   
from django.http import HttpResponse
import time
# Create your views here.   
   
def hello(request):                                                                                                                                  
    return HttpResponse('%s\n%s' % ('hello world!',time.strftime('%Y-%m-%d')))

def index(request):                                                                                                                                  
    return render(request, 'index.html') 
