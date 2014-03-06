from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
    mymessage = "It works"
    return render_to_response('transcriber/index.html', {'message': mymessage})


def transcribe(request, session_id, user_id, speaker_id, speakersession_id, word_id):
    return render_to_response('transcriber/transcribe.html', {'session_id': session_id, 'user_id': user_id, 'speaker_id': speaker_id, 'speakersession_id': speakersession_id, 'word_id': word_id})
