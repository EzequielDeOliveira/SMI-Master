from rest_framework import serializers, viewsets, mixins

from transductors.models import EnergyTransductor

from .models import Measurement
from .models import MinutelyMeasurement
from .models import QuarterlyMeasurement
from .models import MonthlyMeasurement

from .serializers import MinutelyMeasurementSerializer
from .serializers import QuarterlyMeasurementSerializer
from .serializers import MonthlyMeasurementSerializer
from .serializers import MinutelyVoltageThreePhase
from .serializers import MinutelyCurrentThreePhase
from .serializers import MinutelyActivePowerThreePhaseSerializer
from .serializers import MinutelyReactivePowerThreePhase
from .serializers import MinutelyApparentPowerThreePhase
from .serializers import MinutelyPowerFactorThreePhase
from .serializers import MinutelyDHTVoltageThreePhase
from .serializers import MinutelyDHTCurrentThreePhase
from .serializers import MinutelyFrequency
from .serializers import MinutelyTotalActivePower
from .serializers import MinutelyTotalReactivePower
from .serializers import MinutelyTotalApparentPower
from .serializers import MinutelyTotalPowerFactor


#  this viewset don't inherits from viewsets.ModelViewSet because it
#  can't have update and create methods so it only inherits from parts of it
class MeasurementViewSet(mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = None

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        serial_number = self.request.query_params.get('serial_number', None)

        if serial_number is not None:
            transductor = EnergyTransductor.objects.get(
                serial_number=serial_number
            )

            self.queryset = self.queryset.filter(transductor=transductor)

        if((start_date is not None) and (end_date is not None)):
            self.queryset = self.queryset.filter(
                collection_date__gte=start_date
            )
            self.queryset = self.queryset.filter(collection_date__lte=end_date)

        return self.queryset.reverse()


class MinutelyMeasurementViewSet(mixins.RetrieveModelMixin,
                                 mixins.DestroyModelMixin,
                                 mixins.ListModelMixin,
                                 viewsets.GenericViewSet):
    queryset = MinutelyMeasurement.objects.all()
    serializer_class = MinutelyMeasurementSerializer


class QuarterlyMeasurementViewSet(mixins.RetrieveModelMixin,
                                  mixins.DestroyModelMixin,
                                  mixins.ListModelMixin,
                                  viewsets.GenericViewSet):
    """
    Class responsible to define a serializer which convert transductor
    active power fields data to JSON

    Attributes:

        RetrieveModelMixin: The class that provide retrieve method
        DestroyModelMixin: The class that provide destroy method
        ListModelMixin: The class that provide list method
        GenericViewSet: The class that make mixin useful
    """
    queryset = QuarterlyMeasurement.objects.all()
    serializer_class = QuarterlyMeasurementSerializer


class MonthlyMeasurementViewSet(mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin,
                                mixins.ListModelMixin,
                                viewsets.GenericViewSet):
    queryset = MonthlyMeasurement.objects.all()
    serializer_class = MonthlyMeasurementSerializer


class MinutelyVoltageThreePhaseViewSet(MinutelyMeasurementViewSet):
    serializer_class = MinutelyVoltageThreePhase


class MinutelyCurrentThreePhaseViewSet(MinutelyMeasurementViewSet):
    serializer_class = MinutelyCurrentThreePhase


class MinutelyActivePowerThreePhaseViewSet(MinutelyMeasurementViewSet):
    serializer_class = MinutelyActivePowerThreePhaseSerializer


class MinutelyReactivePowerThreePhaseViewSet(MinutelyMeasurementViewSet):
    serializer_class = MinutelyReactivePowerThreePhase


class MinutelyApparentPowerThreePhaseViewSet(MinutelyMeasurementViewSet):
    serializer_class = MinutelyApparentPowerThreePhase


class MinutelyPowerFactorThreePhaseViewSet(MinutelyMeasurementViewSet):
    serializer_class = MinutelyPowerFactorThreePhase


class MinutelyDHTVoltageThreePhaseViewSet(MinutelyMeasurementViewSet):
    serializer_class = MinutelyDHTVoltageThreePhase


class MinutelyDHTCurrentThreePhaseViewSet(MinutelyMeasurementViewSet):
    serializer_class = MinutelyDHTCurrentThreePhase


class MinutelyFrequencyViewSet(MinutelyMeasurementViewSet):
    serializer_class = MinutelyFrequency


class MinutelyTotalActivePowerViewSet(MinutelyMeasurementViewSet):
    serializer_class = MinutelyTotalActivePower


class MinutelyTotalReactivePowerViewSet(MinutelyMeasurementViewSet):
    serializer_class = MinutelyTotalReactivePower


class MinutelyTotalApparentPowerViewSet(MinutelyMeasurementViewSet):
    serializer_class = MinutelyTotalApparentPower


class MinutelyTotalPowerFactorViewSet(MinutelyMeasurementViewSet):
    serializer_class = MinutelyTotalPowerFactor
