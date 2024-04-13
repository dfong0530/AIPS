# use django to create an endpoint for ebay account access/authentication

import hashlib
import json
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ebay_webhook_endpoint(request):
    challenge_code = request.GET.get('challenge_code')
    if challenge_code is not None:
        verification_token = ""
        endpoint_url = "https://aipsbydot.com/ebay-webhook"
        hash_object = hashlib.sha256((challenge_code + verification_token + endpoint_url).encode('utf-8'))
        return JsonResponse({"challengeResponse": hash_object.hexdigest()}, status=200)

    elif request.method == 'POST':
        try:
            order_details = json.loads(request.body)
            # Implement verification, process listing

            return HttpResponse(status=200)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON format")
    else:
        return HttpResponseBadRequest("Invalid request method")