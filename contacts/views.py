# -*- coding: utf-8 -*-
from models import Contact
from rest_framework import viewsets
from contacts.serializers import ContactSerializer
from django.shortcuts import render
from django.core.management import call_command
from django.http import HttpResponse
from models import Contact
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from permissions import WholeWorld
from django.db.models import Q


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed.
    """
    queryset = Contact.objects.all().order_by('lastname')
    serializer_class = ContactSerializer


@api_view(['GET', ])
@permission_classes((WholeWorld,))
def search(request):
    if request.method == 'GET':
        try:
            term = request.query_params['q'].strip()
        except:
            return Response('Required fields: q', status=status.HTTP_400_BAD_REQUEST)
        try:
            term_query = Q(firstname__icontains=term) \
                | Q(lastname__icontains=term) \
                | Q(street__icontains=term) \
                | Q(city__icontains=term) \
                | Q(zipcode__icontains=term)
            result = Contact.objects.filter(term_query)[:20]
        except:
            return Response("not found", status=status.HTTP_204_NO_CONTENT)
        serializer_class = ContactSerializer(result, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)


def index(request):
    contacts = Contact.objects.all()[:20]
    return render(request, 'contacts/contacts.html', {'contacts': contacts})


def readme(request):
    return render(request, 'contacts/readme.html')


def run_import(request):
    call_command('runimport')
    return HttpResponse()
