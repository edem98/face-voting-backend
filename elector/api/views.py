from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# import models
from canditate.models import ElectorsVote, Candidate, Vote
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


@api_view(['POST', ])
def api_elector_new_vote_view(request, electorId):
    try:
        voter = Elector.objects.get(elector_id=electorId)
        candidate = Candidate.objects.get(id=int(request.POST.get('candidateId')))
        election = Vote.objects.get(id=int(request.POST.get('voteId')))
    except Elector.DoesNotExist:
        data = {
            'message': 'Voters not found'
        }
        return Response(data,status=status.HTTP_404_NOT_FOUND)
    except Candidate.DoesNotExist:
        data = {
            'message' : 'Candidate not found'
        }
        return Response(data,status=status.HTTP_404_NOT_FOUND)
    except Vote.DoesNotExist:
        data = {
            'message' : 'Election not found'
        }
        return Response(data,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        new_vote = ElectorsVote(voter=voter,election=election,candidate=candidate)
        new_vote.save()
        election.voters.add(voter)
        election.save()
        return Response({'message': 'Vote register successfully'},status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def api_elector_has_vote_view(request,electorId,voteId):
    try :
        voter = Elector.objects.get(elector_id=electorId)
        election = Vote.objects.get(id=int(voteId))
    except Elector.DoesNotExist:
        data = {
            'message': 'Voters not found'
        }
        return Response(data,status=status.HTTP_404_NOT_FOUND)
    except Vote.DoesNotExist:
        data = {
            'message' : 'Election not found'
        }
        return Response(data,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        has_vote = ElectorsVote.objects.filter(voter=voter,election=election).exists()
        if has_vote:
            data = {
                'message': 'You have already voted in this election'
            }
            return Response(data,status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message': 'You can proceed to vote'},status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)