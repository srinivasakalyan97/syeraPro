from rest_framework import serializers

from syeraproject.models import Artists, Customers, Invoices


class Someserializer(serializers.ModelSerializer):
    class Meta :

        model = Artists
        fields = ('artistid' , 'name' ,)

class Someserializertwo(serializers.ModelSerializer):
    class Meta :

        model = Customers
        fields = "__all__"

class Someserializerthree(serializers.ModelSerializer):
    class Meta :

        model = Customers
        fields = "__all__"

class Someserializerfour(serializers.ModelSerializer):
    lastname=serializers.SerializerMethodField()
    phone=serializers.SerializerMethodField()

    def get_phone(self,obj):
        try:
            return obj.customerid.phone
        except Exception as error:
            print("Inside serializer phone exception".format(str(error)))
            return None

    def get_lastname(self , obj):
        try:
            return obj.customerid.lastname
        except Exception as error:
            print("Exception in AppointmentReceipt serializer for get_lastname" \
                  " AppointmentReceiptDetailsSerializer| {}".format(str(error)))
            return None

    class Meta :
        model = Invoices
        fields = ('lastname' ,'billingaddress', 'billingpostalcode' , 'billingcountry' , 'invoiceid' , 'phone')
