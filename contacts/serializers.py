from models import Contact
from rest_framework import serializers


class ContactSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contact
        fields = ('firstname', 'lastname', 'street',
                  'zipcode', 'city', 'image_url', 'thumbnail')
