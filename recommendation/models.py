from django.db import models
from user.models import CustomUser
from django.utils import timezone

class RecommendInformation(models.Model):
    post_title = models.CharField(max_length = 500, null = True, blank = True)
    title = models.CharField(max_length = 500, null = True, blank = True)
    artist = models.CharField(max_length = 500, null = True, blank = True)
    genre = models.CharField(max_length = 500, null = True, blank = True)
    reason = models.CharField(max_length = 500, null = True, blank = True)
    create_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, null=True)
