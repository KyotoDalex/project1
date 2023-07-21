import logging

from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.shortcuts import render
from django.http import JsonResponse
import re

from django.views.generic import CreateView

from .models import SubscribedUsers
from .forms import SubscribeForm
from ugrainfo.settings.base import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, DEFAULT_FROM_EMAIL,EMAIL_BACKEND

from django.core import mail
from .service import send
from .tasks import send_spam


class SubView(CreateView):
    model = SubscribedUsers
    form_class = SubscribeForm
    success_url = '/'
    template_name = 'index.html'
    def form_valid(self, form):
        form.save()
        send_spam.delay(form.instance.email)
        return super().form_valid(form)
def validate_email(request):
    email = request.POST.get("email", None)
    if email is None:
        res = JsonResponse({'msg': 'Email is required.'})
    elif SubscribedUsers.objects.get(email=email):
        res = JsonResponse({'msg': 'Email Address already exists'})
    elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
        res = JsonResponse({'msg': 'Invalid Email Address'})
    else:
        res = JsonResponse({'msg': ''})
    return res



