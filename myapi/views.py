from datetime import datetime
import logging
logger = logging.getLogger(__name__)


from django.shortcuts import render

from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero

class HeroViewSet(viewsets.ModelViewSet):
    logger.info(f'{datetime.now()}: Responding to /hero')
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
