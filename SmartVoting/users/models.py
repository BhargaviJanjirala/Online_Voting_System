from django.db import models


# Create your models here.
class VoterRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    aadhar = models.CharField(max_length=100)
    age = models.IntegerField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'VoterRegistrations'


# Create your models here.
class PartiesRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    partysymbol = models.FileField(upload_to='uploads/')
    partyname = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'PartiesRegistrations'


class VotingPollModel(models.Model):
    aadhar = models.CharField(unique=True, max_length=100)
    candidate_id = models.IntegerField()
    candidateName = models.CharField(max_length=100)
    constituency = models.CharField(max_length=100)
    partyname = models.CharField(max_length=100)
    vote = models.IntegerField()

    def __str__(self):
        return self.aadhar

    class Meta:
        db_table = 'VotingTable'
