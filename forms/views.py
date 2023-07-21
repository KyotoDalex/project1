# from django.shortcuts import render
# from django.http import JsonResponse
# import re
# # from .forms import CatsForm
#
# from django.core.mail import send_mail
# from django.conf import settings
# # from .forms import SubscribeForm
# from .models import SubscribedUser
# from django.views.generic import CreateView
#
# # from .service import send
#
#
# def index(request):
#     if request.method == 'POST':
#         post_data = request.POST.copy()
#         email = post_data.get("email", None)
#         name = post_data.get("name", None)
#         subscribedUsers = SubscribedUser()
#         subscribedUsers.email = email
#         subscribedUsers.name = name
#         subscribedUsers.save()
#         # send a confirmation mail
#         subject = 'NewsLetter Subscription'
#         message = 'Hello ' + name + ', Thanks for subscribing us. You will get notification of latest articles posted on our website. Please do not reply on this email.'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [email, ]
#         send_mail(subject, message, email_from, recipient_list)
#         res = JsonResponse({'msg': 'Thanks. Subscribed Successfully!'})
#         return res
#     return render(request, 'subscribe.html')
#
#
# def validate_email(request):
#     email = request.POST.get("email", None)
#     if email is None:
#         res = JsonResponse({'msg': 'Требуется ввести email.'})
#     elif SubscribedUser.objects.get(email=email):
#         res = JsonResponse({'msg': 'Данный адрес email уже использован'})
#     elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
#         res = JsonResponse({'msg': 'Некорректный адрес email'})
#     else:
#         res = JsonResponse({'msg': ''})
#     return res
#
#
# # def choice(request):
# #     context = {}
# #     context['form'] = CatsForm()
# #     return render(request, 'subscribe.html', context)
#
# # class SubView(CreateView):
# #     model = SubscribedUser
# #     form_class = SubscribeForm
# #     success_url = '/'
# #
# #     def form_valid(self, form):
# #         form.save()
# #         send(form.instance.email)
# #         return super().form_valid(form)
