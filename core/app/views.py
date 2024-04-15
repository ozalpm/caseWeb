from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from app.models import MyData,FeedBacks,Bugs,Players
import json
import urllib.parse

def index(request):
    return HttpResponse("hello")

@csrf_exempt
def save_player(request,unity_player_id):
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            decoded_data = urllib.parse.unquote(body_unicode)
            json_data = json.loads(decoded_data)
            print(json_data)
            
            unity_name = json_data.get("key0")
            
            try:
                
                Players.objects.create(
                    name=unity_name,
                    player_id=unity_player_id)
                return JsonResponse({'message': 'Feedback data saved successfully'})
                
            except:
                return JsonResponse({'message': 'Feedback data did NOT save successfully'})
        else:
            return JsonResponse({'error': 'Only POST requests are allowed'})   

    
@csrf_exempt
def save_fb_data(request,unity_player_id):
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            decoded_data = urllib.parse.unquote(body_unicode)
            json_data = json.loads(decoded_data)

            print(json_data)
            
            unity_fb_id = str(json_data.get("key0"))
            unity_fb_title = str(json_data.get("key1"))
            unity_fb_var = str(json_data.get("key2") )
            unity_msg_lng = str(json_data.get("lng"))
            try:
                player = get_object_or_404(Players, player_id=unity_player_id)
                FeedBacks.objects.create(
                    msg_lng= unity_msg_lng,
                    fb_id=unity_fb_id,
                    fb_title=unity_fb_title,
                    fb_var=unity_fb_var,
                    player=player)
                return JsonResponse({'message': 'Feedback data saved successfully'})
                
            except:
                return JsonResponse({'message': 'Feedback data did NOT save successfully'})
        else:
            return JsonResponse({'error': 'Only POST requests are allowed'})   

@csrf_exempt
def save_b_data(request,unity_player_id):
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            decoded_data = urllib.parse.unquote(body_unicode)
            json_data = json.loads(decoded_data)

            print(json_data)
            
            unity_b_id = json_data.get("key0")
            unity_b_title = json_data.get("key1")
            unity_b_var = json_data.get("key2")
            unity_msg_lng = str(json_data.get("lng"))
            
            try:
                player = get_object_or_404(Players, player_id=unity_player_id)
                Bugs.objects.create(
                    msg_lng= unity_msg_lng,
                    b_id=unity_b_id,
                    b_title=unity_b_title,
                    b_var=unity_b_var,
                    player=player)
                return JsonResponse({'message': 'Bug data saved successfully'})
                
            except:
                return JsonResponse({'message': 'Bug data did NOT save successfully'})
        
        else:
            return JsonResponse({'error': 'Only POST requests are allowed'})   
             
        # name = json_data.get('name')
        # score = json_data.get('score')
        # player_id = json_data.get("player_id")
        # MyData.objects.create(name=name, score=score, player_id = player_id)
    

@csrf_exempt
def send_data(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        decoded_data = urllib.parse.unquote(body_unicode)
        json_data = json.loads(decoded_data)

        print(json_data)
        
        name = json_data.get('name')
        score = json_data.get('score')
        player_id = json_data.get("player_id")
        MyData.objects.create(name=name, score=score, player_id = player_id)
    
        
        return JsonResponse({'message': 'Data received successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})

@csrf_exempt
def get_data(request):
    if request.method == 'GET':
        data = MyData.objects.all().values()
        return JsonResponse(list(data), safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'})

@csrf_exempt
def player_detail_get(request,player_unity_id):
    if request.method == 'GET':
        
        
        data = MyData.objects.filter(player_id=player_unity_id).all().values()
        return JsonResponse(list(data), safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}) 
    
@csrf_exempt
def get_version_data(request):
    
    if request.method == "GET":
        return JsonResponse({'version': '0.012','msg':'herkese iyi oyunlar'})
    
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'})
    
        
            
    
    