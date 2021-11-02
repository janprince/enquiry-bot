from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from .bot_logic import generate_response
# Create your views here.


@csrf_exempt
@require_http_methods(['GET', "POST"])
def index(request):
    if request.method == "POST":
        t_data = json.loads(request.body)
        print(t_data)
        t_message = t_data['message']
        t_chat = t_message["chat"]

        chat_id = t_chat['id']
        msg_text = t_message['text']

        firstname = t_message['from']['first_name']

        generate_response(firstname, chat_id=chat_id, msg=msg_text)

    return HttpResponse("Success")
