from django.urls import path
from elector.api.views import api_detail_elector_view, api_elector_new_vote_view, api_elector_has_vote_view

app_name = 'elector'

urlpatterns = [
    path('<str:id>/', api_detail_elector_view, name="info"),
    path('vote/<str:electorId>/', api_elector_new_vote_view, name="new_vote"),
    path('has-vote/<str:electorId>/<str:voteId>/', api_elector_has_vote_view, name="new_vote"),
]
