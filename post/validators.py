# from rest_framework import serializers
# from rest_framework.validators import UniqueForDateValidator
# from .models import PostPage
#
#
# class ExampleSerializer(serializers.Serializer):
#     # ...
#     class Meta:
#         # Blog posts should have a slug that is unique for the current year.
#         validators = [
#             UniqueForDateValidator(
#                 queryset=PostPage.objects.all(),
#                 field='slug',
#                 date_field='pub_date'
#             )
#         ]
