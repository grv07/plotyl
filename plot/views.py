from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from plot.models import Phone, PhoneForm

import json 

# Get data of phone ...
def get_live_data(request):
	try:
		# In a case offset and limit not given default offset=0, limit=100
		my_queryset = Phone.objects.all().order_by('id')[
			int(request.GET.get('offset', 0)):int(request.GET.get('limit', 100))]
		result_list = list(my_queryset.values('pos_x', 'pos_y', 'imsi', 'rssi', 'time'))
		# If Update json accor..
		# result_list = [{'x':data.pos_x, 'y':data.pos_y, 'name':data.imsi, 'z':2} for data in  my_queryset]
		return JsonResponse(json.dumps(result_list), safe=False)
	except Exception as e:
		return JsonResponse({'msg': 'Out of data'}, safe=False, status=500)	

@csrf_exempt
def plot_data(request):
	# Save data on POST call ..
	if request.method == 'POST':
		pf = PhoneForm(json.loads(request.body.decode("utf-8")))
		# Validate all POST data user send
		if pf.is_valid():
			obj = pf.save()
			return JsonResponse({'msg': 'Success', 'id': obj.id})
		else:
			return JsonResponse({'msg': 'Fail to save.','errors': dict(pf.errors.items())}, status=500)	
	else:
		return render(request, 'plot_data.html')

# Create your views here.
