from django.db import models

class PodioApiKey(models.Model):
    application_name = models.CharField(max_length=50)
    client_id = models.CharField(max_length=50)
    client_secret = models.CharField(max_length=64)
    

class PodioApplication(models.Model):
    application_name = models.CharField(max_length=50)
    application_id = models.PositiveIntegerField()
    auth_token = models.CharField(max_length=128)
