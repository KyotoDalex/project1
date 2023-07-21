import datetime
from .models import Advert


def date_vaditaion(request):
    advert = Advert.objects.filter(publish_date=datetime.datetime.now)
    return {'ads':advert}