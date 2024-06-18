from django.db import models

# Create your models here.

class VotingTurnOn(models.Model):
    status = models.CharField(max_length=100)
    cDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.status

    class Meta:
        db_table = 'VotingIS'