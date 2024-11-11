from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils_file_reader import process_request
# Create your views here.

@api_view(['POST'])
def post_data_transfer(request):
    dicData = request.data

    lstdictEmployees = dicData['lstFilenames']
    strEnum = dicData['strEnum']

    serlzSerializer = process_request(lstdictEmployees, strEnum)

    if serlzSerializer.is_valid():
       serlzSerializer.save()
       return Response(serlzSerializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serlzSerializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    