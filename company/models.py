from django.db import models
from accounts.models import Item
from django.utils import timezone
from users.models import User

class Reply(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='user')
    price = models.IntegerField(default=0)
    text = models.TextField("備考")
    created_date = models.DateTimeField(default=timezone.now)
    target = models.ForeignKey(Item, null=True, on_delete=models.CASCADE, related_name='reply')


    def __int__(self):
        return self.price



