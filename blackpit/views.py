import json
from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .datastore import get_records, get_vaccinated
from .paginator import Pagination

paginator = Pagination()

# Create your views here.
def index(request):
    template = 'blackpit/index.html'
    context = dict()
    records = get_records("populated-african-countries-vs-total-vaccinated-population.csv")
    if len(records) > 0:
        fields = list(records[0].keys())
        formattedData = json.dumps(records)
        context = {
            'records': records, 
            "fields": fields, 
            "formattedData": formattedData
        }
    return render(request, template, context=context)

@api_view(['GET'])
def vaccinated(request):
    vaccinated_populations = json.dumps(get_vaccinated())
    return Response(vaccinated_populations, status=status.HTTP_200_OK)
        
    