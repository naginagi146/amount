import json

from django.core.mail import send_mail
from django.template.loader import get_template

import mysite.settings as settings

def send_email(message):
    subject = 'データ更新'
    from_address = 'from@gmail.com'
    to_address = ['to@gmail.com']
    send_mail(subject, message, from_address, to_address)


def get_message(item, action):
    template = get_template('accounts/message.txt')
    context = {
        "item": item, "action": action,
    }
    message = template.render(context)
    return message


# 通知処理
def send_notification(item, action):
    message = get_message(item, action)
    send_email(message)