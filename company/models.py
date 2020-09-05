from django.db import models
from accounts.models import Item
from django.utils import timezone
from users.models import User

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    text = models.TextField("備考")
    created_date = models.DateTimeField(default=timezone.now)
    target = models.ForeignKey(Item,on_delete=models.CASCADE)


    def __str__(self):
        return self.name



