from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='get_data'),
    path('save/p=<int:unity_player_id>/', views.save_player, name='save_player'),
    path('save/fb=<int:unity_player_id>/', views.save_fb_data, name='save_fb_data'),
    path('save/b=<int:unity_player_id>/', views.save_b_data, name='save_b_data'),
    
    path('send/', views.send_data, name='send_data'),
    path('get/', views.get_data, name='get_data'),
    
    path('get/version/', views.get_version_data, name='get_data'),
    path('get/<int:player_unity_id>/', views.player_detail_get, name='player_detail_get'),
    
    ]