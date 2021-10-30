from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User


class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ('id', 'Advisor_name', 'advisor_img_url')
