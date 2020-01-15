from rest_framework import serializers

from .models import MinutelyMeasurement
from .models import QuarterlyMeasurement
from .models import MonthlyMeasurement


class MinutelyMeasurementSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MinutelyMeasurement
        fields = ('id',
                  'transductor',
                  'collection_time',
                  'frequency_a',
                  'voltage_a',
                  'voltage_b',
                  'voltage_c',
                  'current_a',
                  'current_b',
                  'current_c',
                  'active_power_a',
                  'active_power_b',
                  'active_power_c',
                  'total_active_power',
                  'reactive_power_a',
                  'reactive_power_b',
                  'reactive_power_c',
                  'total_reactive_power',
                  'apparent_power_a',
                  'apparent_power_b',
                  'apparent_power_c',
                  'total_apparent_power',
                  'power_factor_a',
                  'power_factor_b',
                  'power_factor_c',
                  'total_power_factor',
                  'dht_voltage_a',
                  'dht_voltage_b',
                  'dht_voltage_c',
                  'dht_current_a',
                  'dht_current_b',
                  'dht_current_c',
                  'transductor',
                  'url')


class QuarterlyMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuarterlyMeasurement
        fields = ('id',
                  'collection_time',
                  'generated_energy_peak_time',
                  'generated_energy_off_peak_time',
                  'consumption_peak_time',
                  'consumption_off_peak_time',
                  'inductive_power_peak_time',
                  'inductive_power_off_peak_time',
                  'capacitive_power_peak_time',
                  'capacitive_power_off_peak_time',
                  'transductor',
                  'url')


class MonthlyMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MonthlyMeasurement
        fields = ('id',
                  'generated_energy_peak_time',
                  'generated_energy_off_peak_time',
                  'consumption_peak_time',
                  'consumption_off_peak_time',
                  'inductive_power_peak_time',
                  'inductive_power_off_peak_time',
                  'capacitive_power_peak_time',
                  'capacitive_power_off_peak_time',
                  'active_max_power_peak_time',
                  'active_max_power_off_peak_time',
                  'reactive_max_power_peak_time',
                  'reactive_max_power_off_peak_time',
                  'active_max_power_list_peak_time',
                  'active_max_power_list_off_peak_time',
                  'reactive_max_power_list_peak_time',
                  'reactive_max_power_list_off_peak_time',
                  'url')


class ThreePhaseSerializer(MinutelyMeasurementSerializer):
    """
    Class responsible to define a serializer which convert apparent
    three phase transductor fields data to JSON

    Attributes:

        model (MinutelyMeasurement): The model which defines the type of
        measurement.
        fields (tuple): Generic representation of all threephasic measurements.
            .. note::
                The tuple elements must be of str type.

    Example of use:

    >>> queryset = MinutelyMeasurement.objects.all()
        serializer_class = MinutelyApparentPowerThreePhase
    """
    phase_a = serializers.ListField(default=[])
    phase_b = serializers.ListField(default=[])
    phase_c = serializers.ListField(default=[])
    serial_number = serializers.CharField()

    class Meta:
        model = MinutelyMeasurement
        fields = (
            'id',
            'serial_number',
            'phase_a',
            'phase_b',
            'phase_c'
        )


class MeasurementSerializer(MinutelyMeasurementSerializer):
    measurements = serializers.ListField(default=[])
    serial_number = serializers.CharField()

    class Meta:
        model = MinutelyMeasurement
        fields = (
            'id',
            'serial_number',
            'measurements'
        )


class QuarterlySerializer(QuarterlyMeasurementSerializer):
    measurements = serializers.ListField(default=[])
    min = serializers.FloatField(default=0.0)
    max = serializers.FloatField(default=0.0)

    class Meta:
        model = QuarterlyMeasurement
        fields = (
            'id',
            # 'transductor',
            'measurements',
            'min',
            'max'
        )


class StackedQuarterlySerializer(QuarterlyMeasurementSerializer):
    class Meta:
        model = QuarterlyMeasurement
        fields = (
            'consumption',
            'generated_energy'
        )


class RealTimeMeasurementSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MinutelyMeasurement
        fields = ('id',
                  'transductor_id',
                  'collection_time',
                  'voltage_a',
                  'voltage_b',
                  'voltage_c',
                  'current_a',
                  'current_b',
                  'current_c',
                  'total_active_power',
                  'total_reactive_power',
                  'total_power_factor',
                  'url')
