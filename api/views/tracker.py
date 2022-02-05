from django.http import HttpResponse, HttpResponseServerError, JsonResponse
from django.shortcuts import render
from django.template import RequestContext, Template
import json
from django.views.decorators.csrf import csrf_exempt
from geopy.geocoders import Nominatim

from api.models import Tracker, TrackerLocation


@csrf_exempt
def update_tracker_location(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            data = json_data['latitude'], json_data['longitude'], json_data['tracker_id']
            geolocator = Nominatim(user_agent="stevemosiori@gmail.com") # replace with your own user_agent
            location = geolocator.reverse(str(data[0]) + ',' + str(data[1]))

            try:
                tracker = Tracker.objects.get(tracker_id=data[2])
                tracker_location = TrackerLocation(latitude=data[0], longitude=data[1], tracker=tracker)
                tracker_location.save()
                
                return HttpResponse("Success")
            except Tracker.DoesNotExist:
                return HttpResponseServerError("Tracker does not exist")   
            # return JsonResponse({'status': 'OK', 'location': location.raw})
            # return JsonResponse({'status': 'OK', 'message': 'Location updated'})
        except KeyError:
            return JsonResponse({'status': 'Incomplete data'}, status=400)
        except Exception as e:
            return HttpResponseServerError(e)

@csrf_exempt
def register_tracker(request):
    json_data = json.loads(request.body)
    data = json_data['child_id'], json_data['tracker_id']
    try:
        tracker = Tracker.objects.get(tracker_id=data[1])
        return HttpResponseServerError("Tracker already exists")
    except Tracker.DoesNotExist:
        tracker = Tracker.objects.create(child_id=data[0], tracker_id=data[1])
        return JsonResponse(tracker, safe=False)
# if( bb.ix <= p.x && p.x <= bb.ax && bb.iy <= p.y && p.y <= bb.ay ) {
#     // Point is in bounding box
# }
