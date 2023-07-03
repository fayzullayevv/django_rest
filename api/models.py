from django.db import models

class BotUser(models.Model):
    user_id = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    user_id = models.CharField(max_length=120,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=120,null=True,blank=True)
    age = models.PositiveBigIntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.body
