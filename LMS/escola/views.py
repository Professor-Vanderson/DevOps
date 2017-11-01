from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'lista1':[1,2,3,4],
	    'lista2':['item1','item2','item3']
        } 
    return render(request, 'index.html', context)
