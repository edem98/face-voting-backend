import json

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

# import models
from canditate.models import Candidate, Vote
from canditate.api.serializers import CandidateSerializer, VoteSerializer

@api_view(['GET', ])
def api_detail_candidate_view(request, id):
    try:
        candidate = Candidate.objects.get(id=id)
    except candidate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data)


class ApiCandidateListView(ListAPIView):
    serializer_class = CandidateSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['first_name', 'last_name', 'political_party']
    queryset = Candidate.objects.all()


@api_view(['GET', ])
def api_vote_list(request, electorId):
    try:
        votes = Vote.objects.exclude(voters__elector_id=electorId)
        print(votes)
    except Vote.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VoteSerializer(votes,many=True)
        return Response(serializer.data)


