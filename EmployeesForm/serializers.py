from jobs.models import Entry
from rest_framework import fields, serializers


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        # filds =['i', 'id','name', 'number']
        fields = '__all__'