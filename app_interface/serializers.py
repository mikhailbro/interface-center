from rest_framework import serializers
from app_interface.models import Interface
from django.contrib.auth.models import User


class InterfaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interface
        fields = ['owner', 'interface_id', 'major_version', 'name', 'description',
                  'owned_interface', 'doc_link', 'workend_date', 'restriction', 'restriction', 'restriction_text',
                  'restriction_code', 'status', 'info_classification', 'infoflow_direction', 'domain_name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
