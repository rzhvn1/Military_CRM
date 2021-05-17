from django.contrib.auth.models import User
from django.core.mail import EmailMessage
import re

def mailing(username):
    super_users = User.objects.filter(is_superuser=True)
    email_lst = []
    for user in super_users:
        email_lst.append(user.email)
    subject = 'Salam Aleikum!'
    body = f'User {username} registered in military database, please check him!'
    email = EmailMessage(subject=subject, body=body, to=email_lst)
    email.send()


def validate_password(password):
    while True:
        if(len(password) <= 8):
            flag = False
            break
        elif not re.search("[a-z]", password):
            flag = False
            break
        elif not re.search("[A-Z]", password):
            flag = False
            break
        elif not re.search("[0-9]", password):
            flag = False
            break
        elif re.search("\s", password):
            flag = False
            break
        else:
            flag = True
            break

    if flag == False:
        return flag
    else:
        return flag


