
from django.shortcuts import render, redirect
from jobs.models import Entry
from PIL import Image
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework import serializers, status
from EmployeesForm.serializers import EntrySerializer
from django.views.decorators.csrf import csrf_exempt 
# Create your views here.

@csrf_exempt
def add(request):
    if request.method == 'POST':
        prod = Entry()
        prod.name=request.POST.get('name')
        prod.number=request.POST.get('number')
        prod.address=request.POST.get('address')
        prod.image=request.POST.get('images')

        if len(request.FILES) != 0:
            prod.image = request.FILES['images']        
        prod.save()
        
        
        return redirect('/totalentrys')

    else:
        return render(request,'add.html')  

@csrf_exempt
def totalentrys(request):
    # if request == 'GET':
    exicative = Entry.objects.all()
    # print(exicative)
    # context = {'exicative':exicative}
    # print(context)
    return render(request, 'totalentrys.html', {'exicative':exicative})
    
def number(request):
    
    return render(request,'phoneno.html',{"number":'880061196123'})

@csrf_exempt
class EntryList(APIView):

    @csrf_exempt
    def get(request):
        Entry1=Entry.objects.all()
        serializer = EntrySerializer(Entry1, many = True)
        abc1 = json.dumps(serializer.data)
        abc = json.loads(abc1)
        data = {'Entry': abc}
        return JsonResponse(data)

    @csrf_exempt
    def post(request):
        if request.method == 'POST':
            prod = Entry()
            prod.name=request.POST.get('name')
            prod.number=request.POST.get('number')
            prod.address=request.POST.get('address')
            prod.image=request.POST.get('images')

            if len(request.FILES) != 0:
                prod.image = request.FILES['images']        
            
            
                prod.save();
                queryset = Entry.objects.order_by('id').last()
                serializer = EntrySerializer(queryset)
                abc1 = json.dumps(serializer.data)
                abc = json.loads(abc1)
                print(abc)
                data = {'Entry': abc}
            
                return JsonResponse(data)