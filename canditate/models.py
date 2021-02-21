from django.db import models
from elector.models import Elector


class Candidate(models.Model):
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    picture = models.ImageField(upload_to='candidates',null=True)
    political_party = models.CharField(max_length=255,null=True)
    date_add = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    votes = models.PositiveIntegerField(null=True, default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name + " from " + self.political_party


class Vote(models.Model):
    """
    the vote class defines votes and voters and candidates interaction with them.
    """
    vote_title = models.CharField(verbose_name='Election',max_length=25,null=True,blank=True)
    vote_description = models.TextField(verbose_name='Purpose',null=True,blank=True)
    voters = models.ManyToManyField(Elector)
    candidates = models.ManyToManyField(Candidate)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edites = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Election'
        verbose_name_plural = 'Elections'

    def __str__(self):
        return self.vote_title


class ElectorsVote(models.Model):
    election = models.ForeignKey(Vote,on_delete=models.CASCADE,null=True,blank=True)
    voter = models.ForeignKey(Elector,on_delete=models.CASCADE,null=True,blank=True)
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.election)
