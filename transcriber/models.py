from django.db import models

class WordOriginal(models.Model):
    wordid = models.IntegerField()
    word = models.CharField(max_length=20)
    def __unicode__(self):
        return self.word

class WordSpoken(models.Model):
    wordid = models.IntegerField()
    speakerid = models.CharField(max_length=20)
    datetime = models.CharField(max_length=20)
    nrtranscribed = models.IntegerField()
    def __unicode__(self):
        return self.experttranscription

class WordTranscription(models.Model):
    wordspokenid = models.IntegerField()
    userid = models.IntegerField()
    transcription = models.CharField(max_length=20)
    datetime = models.CharField(max_length=40)
    def __unicode__(self):
        return self.transcription
