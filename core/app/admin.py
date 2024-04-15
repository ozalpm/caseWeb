from django.contrib import admin
from .models import Players,FeedBacks,Bugs  # Player modelinizin import edildiğinden emin olun

class PlayerAdmin(admin.ModelAdmin):
    search_fields = ['name']  # Aramak istediğiniz alanları burada belirtin
    

class FeedBacksAdmin(admin.ModelAdmin):
    search_fields = ['fb_title','fb_var']  # Aramak istediğiniz alanları burada belirtin
    list_filter = ['msg_lng'] 
    
class BugsAdmin(admin.ModelAdmin):
    search_fields = ['b_title','b_var']  # Aramak istediğiniz alanları burada belirtin
    list_filter = ['msg_lng'] 
    
admin.site.register(Players, PlayerAdmin)
admin.site.register(FeedBacks, FeedBacksAdmin)
admin.site.register(Bugs, BugsAdmin)
