from rest_framework import serializers

class ExtractionSerializer(serializers.Serializer):
    profession = serializers.CharField()
    departements = serializers.ListField(
        child=serializers.CharField()
    )
    option = serializers.ChoiceField(choices=[1, 2])
