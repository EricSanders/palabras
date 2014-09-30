import random, datetime
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from transcriber.models import WordTranscription, WordSpoken, WordOriginal
from django.contrib.auth.decorators import login_required

@login_required

def index(request):
    #mymessage = "It works"
    #return render_to_response('transcriber/index.html', {'message': mymessage})
    return render_to_response('transcriber/index.html',context_instance=RequestContext(request))

def transcribe(request):

    try:
        userid = request.POST['userid']
    except:
         return render_to_response('transcriber/index.html', {
            'message': "form input error",
            }, context_instance=RequestContext(request))
       
    if not userid or userid == '':
        # Redisplay the userid input form.
        return render_to_response('transcriber/index.html', {
            'message': "empty userid",
            }, context_instance=RequestContext(request))

    try:
        wsid = request.POST['wsid']
        transcription = request.POST['transcription']
        # save data
        wt = WordTranscription(wordspokenid=wsid,userid=userid,transcription=transcription,datetime=str(datetime.datetime.now()))
        try:
            wt.save()
        except:
            return render_to_response('transcriber/index.html', {
                'message': "saving failed",
                }, context_instance=RequestContext(request))
        
    except:
        # niets aan de hand
        return render_to_response('transcriber/index.html', {
            'message': "id or transcription not received",
            }, context_instance=RequestContext(request))

    wtlist = WordTranscription.objects.all().filter(userid=userid)
    if wtlist:
        # Select random word
        wslist = WordSpoken.objects.all()
        count = wslist.count()
        ws = wslist[int(random.random() * count)]
    else:
        # Select random word
        wslist = WordSpoken.objects.all()
        count = wslist.count()
        ws = wslist[int(random.random() * count)]
        #return render_to_response('transcriber/index.html', {
        #    'message': "wrong userid",
        #}, context_instance=RequestContext(request))

    return render_to_response('transcriber/transcribe.html', { 'userid': userid,  'ws': ws, 'MEDIA_ROOT':  settings.MEDIA_ROOT}, context_instance=RequestContext(request))

#def transcribe(request, session_id, user_id, speaker_id, speakersession_id, word_id):
#    return render_to_response('transcriber/transcribe.html', {'session_id': session_id, 'user_id': user_id, 'speaker_id': speaker_id, 'speakersession_id': speakersession_id, 'word_id': word_id})
