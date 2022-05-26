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
    records = get_vaccinated()
    vaccinated = json.dumps(records)
    print(vaccinated)
    if len(records) > 0:
        context = {
            'records': records, 
            "fields": list(records[0].keys()), 
            "vaccinated": vaccinated
        }
    return render(request, template, context=context)

@api_view(['GET'])
def vaccinated(request):
    vaccinated_populations = json.dumps(get_vaccinated())
    return Response(vaccinated_populations, status=status.HTTP_200_OK)
        
    