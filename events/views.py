from django.utils import timezone
import numpy as np
import os

from django.db.models.query import QuerySet

from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import mixins

from rest_framework.exceptions import APIException
from django.core.exceptions import ObjectDoesNotExist

from .models import *

from .serializers import VoltageRelatedEventSerializer
from .serializers import FailedConnectionSlaveEventSerializer
from .serializers import FailedConnectionTransductorEventSerializer

from django.utils import timezone


class EventViewSet(mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = None
    model = None

    def get_queryset(self):
        type = self.request.query_params.get('type')
        transductor = self.request.query_params.get('transductor')

        if type == 'active':
            self.queryset = self.model.objects.filter(
                ended_at__isnull=True
            )
        elif type == 'inactive':
            self.queryset = self.model.objects.filter(
                ended_at__isnull=False
            )
        elif type == 'period':
            # Initially defined to be filtered for 3 days
            now = timezone.now()
            initial = now - timezone.timedelta(days=3)

            self.queryset = self.model.objects.filter(
                created_at__gte=initial,
                created_at__lte=now
            )
        else:
            self.queryset = self.model.objects.all()

        return self.queryset

    def specific_query(self):
        pass


class VoltageRelatedEventViewSet(EventViewSet):
    model = VoltageRelatedEvent
    serializer_class = VoltageRelatedEventSerializer

    def specific_query(self):
        serial_number = self.request.query_params.get('serial_number')

        try:
            transductor = EnergyTransductor.objects.get(
                serial_number=serial_number
            )
            self.queryset = self.queryset.filter(
                transductor=transductor
            )
        except EnergyTransductor.DoesNotExist:
            raise APIException(
                'Serial number does not match with any transductor.'
            )


class FailedConnectionSlaveEventViewSet(EventViewSet):
    model = FailedConnectionSlaveEvent
    serializer_class = FailedConnectionSlaveEventSerializer

    def specific_query(self):
        ip_address = self.request.query_params.get('ip_address')

        try:
            slave = Slave.objects.get(ip_address=slave_ip)
            self.queryset = self.queryset.filter(
                slave=slave
            )
        except Slave.DoesNotExist:
            raise APIException(
                'IP Address does not match with any slave'
            )


class FailedConnectionTransductorEventViewSet(EventViewSet):
    model = FailedConnectionTransductorEvent
    serializer_class = FailedConnectionTransductorEventSerializer

    def specific_query(self):
        serial_number = self.request.query_params.get('serial_number')

        try:
            transductor = EnergyTransductor.objects.get(
                serial_number=serial_number
            )
            self.queryset = self.queryset.filter(
                transductor=transductor
            )
        except EnergyTransductor.DoesNotExist:
            raise APIException(
                'Serial number does not match with any transductor.'
            )