from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from elector.models import File


def index(request):
    return render(request,'index.html')


class FileUploadView(View):

    def post(self, request, *args, **kwargs):
        _, file = request.FILES.popitem()
        # get file
        file = file[0]
        print(file.__dict__)
        # get elector
        elector_id = request.POST.get('electorId')
        print(elector_id)
        if elector_id and file:
            data = {
                'image': file._name,
                'electorId': elector_id
            }
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = {
                'message': 'An error occured while processing the file',
            }
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)

def upload(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
            print(data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message': "Thanks for your feedback on this survey."},status=status.HTTP_201_CREATED)
