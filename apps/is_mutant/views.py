"""is_mutant application endpoints."""

# RestFramework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Functions
from apps.is_mutant.functions import is_mutant

# Models
from apps.is_mutant.models import Adn

# Utils
import json

class IsMutant(APIView):
  """End-point to identify if it is a mutant or not."""
  def post(self, request):
    """Only post method allowed."""
    # dna = ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
    response = {}
    if not "dna" in request.data.keys():
      response['error'] = True
      response['message'] = "Missing dna in the request."
      return Response(response, status.HTTP_400_BAD_REQUEST)

    if type(request.data['dna']) != list:
      response['error'] = True
      response['message'] = "dna is not array."
      return Response(response, status.HTTP_400_BAD_REQUEST)

    [response['error'],  response['is_mutant'], response['message']] = is_mutant(request.data['dna'])

    if response['error']:
      response.pop('is_mutant')
      return Response(response, status.HTTP_400_BAD_REQUEST)
    
    if not response['is_mutant']:
      status_response = status.HTTP_403_FORBIDDEN
    status_response = status.HTTP_200_OK

    adn = json.dumps(request.data['dna'])

    try:
      Adn.objects.create(
        adn = adn,
        is_mutant = response['is_mutant']
      )
    except:
      pass

    return Response(response, status_response)

class Stats(APIView):
  """End point to get the stats"""
  def get(self, request):
    """Only get method allowed."""
    query = Adn.objects.all().values_list('is_mutant', flat=True)
    query = list(query)
    count_mutant_dna = query.count(True)
    count_human_dna = query.count(False)
    if count_human_dna == 0:
      if count_mutant_dna == 0:
        ratio = 0
      else :
        ratio = 1
    else:
      ratio = count_mutant_dna / count_human_dna
    response = {}
    response['count_mutant_dna'] = count_mutant_dna
    response['count_human_dna'] = count_human_dna
    response['ratio'] = ratio

    return Response(response, status.HTTP_200_OK)

