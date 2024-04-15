from django.db import models

class MyData(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    player_id = models.IntegerField()


class Players(models.Model):
 
    name = models.CharField(max_length=100)
    player_id = models.CharField(max_length=50,unique=True) #unique value

    def __str__(self):
        return self.name

    
class Extras(models.Model):
    msg_lng = models.CharField(max_length=3)
    ex_id = models.CharField(max_length=50,unique=True)
    ex_title = models.CharField(max_length=100)  
    ex_var = models.TextField()
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ex_title

    
class Bugs(models.Model):
    msg_lng = models.CharField(max_length=3)
    b_id = models.CharField(max_length=50,unique=True)
    b_title = models.CharField(max_length=100)
    b_var = models.TextField()
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    def __str__(self):
        return self.b_title

    

class FeedBacks(models.Model):
    msg_lng = models.CharField(max_length=3)
    fb_id = models.CharField(max_length=50,unique=True)
    fb_title = models.CharField(max_length=100)
    fb_var = models.TextField()
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.fb_title
  

