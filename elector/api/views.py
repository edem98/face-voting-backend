from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# import models
from elector.models import Elector
from elector.api.serializers import ElectorSerializer
# import serializer

@api_view(['GET', ])
def api_detail_elector_view(request, id):
    try:
        print(id)
        elector = Elector.objects.get(elector_id=id)
    except Elector.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ElectorSerializer(elector)
        return Response(serializer.data)


@api_view(['PUT' ])
def api_elector_vote_view(request,id):
    id = request.data['id']
    candidate_id = request.data['candidate_id']
    print(request.data['id'])
    print(request.data['candidate_id'])
    try:
        elector = Elector.objects.get(elector_id=id)
    except Elector.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        if elector.has_vote:
            data = {
                'message': 'You have already voted'
            }
            return Response(data)
        elector.has_vote = True
        elector.candidate_id = candidate_id
        elector.save()

        data = {
            'eletor': elector.elector_id,
            'success': 'Your vote was registered with succes'
        }
        return Response(data)

