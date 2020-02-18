from rest_framework import serializers

from syeraproject.models import Artists, Customers


class Someserializer(serializers.ModelSerializer):
    class Meta :

        model = Artists
        fields = ('artistid' , 'name' ,)

class Someserializertwo(serializers.ModelSerializer):
    class Meta :

        model = Customers
        fields = "__all__"