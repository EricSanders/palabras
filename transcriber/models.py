from django.db import models

class WordOriginal(models.Model):
    wordid = models.IntegerField()
    word = models.CharField(max_length=20)
    def __unicode__(self):
        return self.word

class WordTranscription(models.Model):
    wordoriginal = models.ForeignKey(WordOriginal)
    transcription = models.CharField(max_length=20)
    speakerid = models.IntegerField()
    speakersessionid = models.IntegerField()
    userid = models.IntegerField()
    sessionid = models.IntegerField()
    begintime = models.DateTimeField()
    endtime = models.DateTimeField()
    def __unicode__(self):
        return self.transcription
