from django.urls import path
from canditate.api.views import api_detail_candidate_view, ApiCandidateListView, api_vote_list

app_name = 'candidate'

urlpatterns = [
    path('<int:id>/', api_detail_candidate_view, name="detail"),
    path('candidates/', ApiCandidateListView.as_view(), name="candidates"),
    path('votes/<str:electorId>/', api_vote_list, name="votes"),
    path('votes/<str:electorId>/', api_vote_list, name="votes"),
]
