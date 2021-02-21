from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
import json


# Create your views here.
from elector.api.serializers import FileSerializer


def index(request):
    return render(request,'index.html')


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(request.POST, request.FILES)
        if file_serializer.is_valid():
            print("we got it")
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                'file_serializer': file_serializer,
                'message': 'Ca ne ne marche pas',
                'donnes': request.data
            }
            print(file_serializer.errors)
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

def upload(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
            print(data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message': "Thanks for your feedback on this survey."},status=status.HTTP_201_CREATED)
