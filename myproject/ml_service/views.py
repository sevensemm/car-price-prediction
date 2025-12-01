from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .ml_model.predictor import predict_car_price  

def index(request):
    return render(request, 'ml_service/index.html')

@csrf_exempt
def predict(request):
    data = json.loads(request.body)
    price = predict_car_price({
        'seller': data.get('seller'),
        'vehicleType': data.get('vehicleType'),
        'fuelType': data.get('fuelType'),
        'brand': data.get('brand'),
        'notRepairedDamage': data.get('notRepairedDamage'),
        'gearbox': data.get('gearbox'),
        'model': data.get('model'),
        'powerPS': int(data.get('powerPS')),
        'kilometer': int(data.get('kilometer')),
        'age': int(data.get('age')),
        'nrOfPictures': int(data.get('nrOfPictures'))
    })
    
    return JsonResponse({
        'success': True,
        'prediction': float(price)
    })
