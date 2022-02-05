from django.http import HttpResponse, HttpResponseServerError, JsonResponse
from django.shortcuts import render
from django.template import RequestContext, Template
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def update_tracker_location(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
    try:
        data = json_data['latitude'], json_data['longitude'], json_data['tracker_id']
        return JsonResponse({'status': 'OK', 'message': 'Location updated'})
    except KeyError:
        return JsonResponse({'status': 'Incomplete data'}, status=400)
    except Exception as e:
        return HttpResponseServerError(e)
