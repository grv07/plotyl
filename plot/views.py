from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# from django.core import serializers

from plot.models import Phone

import json 

def get_live_data(request):
	my_queryset = Phone.objects.all().order_by('id')[int(request.GET.get('offset')):int(request.GET.get('limit'))]
	result_list = list(my_queryset.values('pos_x', 'pos_y', 'imsi', 'rssi', 'time'))
	return JsonResponse(json.dumps(result_list), safe=False)

@csrf_exempt
def plot_data(request):
	if request.method == 'POST':
		values = request.POST.dict()
		try:
			Phone.objects.create(**values)
			return JsonResponse({'status-msg': 'Success'})
		except Exception as e:
			print(e.args)
			return JsonResponse({'status-msg': 'Fail', 'status':500})
	else:
		return render(request, 'plot_data.html')

# Create your views here.
