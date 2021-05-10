from django.contrib.auth.models import User
from django.core.mail import EmailMessage


def mailing(username):
    super_users = User.objects.filter(is_superuser=True)
    email_lst = []
    for user in super_users:
        email_lst.append(user.email)
    subject = 'Salam Aleikum!'
    body = f'User {username} registered in military database, please check him!'
    email = EmailMessage(subject=subject, body=body, to=email_lst)
    email.send()


