from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Item
from users.models import User

@receiver(post_save,)
def item_create_notification(sender, instance, created, **kwargs):
    """Itemが投稿されたら企業側にメールで通知する"""

    user = [u.user for u in Item.objects.filter(post=instance.post)]
    if created:
        subject = "投稿通知"
        message = "新規アイテムが投稿されました"
        from_email = settings.EMAIL_HOST_USER
        for u in user:
            recipient_list = [u.email]
            send_mail(subject, message, from_email, recipient_list)