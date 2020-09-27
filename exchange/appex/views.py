from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


import pandas_datareader as pdr
import json


bradesco = pdr.get_data_yahoo('BBDC4.SA')
result = bradesco.to_json(orient="table", date_format='iso')
parsed = json.loads(result)

#Itaú Unibanco Holding S.A. (ITUB4.SA)
itau = pdr.get_data_yahoo('ITUB4.SA')
result1 = itau.to_json(orient="table", date_format='iso')
parsed1 = json.loads(result1)

#Companhia de Transmissão de Energia Elétrica Paulista S.A.
cetep = pdr.get_data_yahoo('TRPL4.SA')
result2 = cetep.to_json(orient="table", date_format='iso')
parsed2 = json.loads(result2)


def home(request):
    if request.method == 'GET':
        data = '<html><body><h1>EXCHANGE API</h1><P>A simple api</P></body></html>'
        data2 = '<P>/bbdc, /itub, /trpl</P>'
        return HttpResponse(data+data2)

def bbdc(request):
    if request.method == 'GET':
        return JsonResponse(parsed)

def itub(request):
    if request.method == 'GET':
        return JsonResponse(parsed1)

def trpl(request):
    if request.method == 'GET':
        return JsonResponse(parsed2)

