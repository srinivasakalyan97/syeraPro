from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Artists, Customers
from .serializer import Someserializer, Someserializertwo, Someserializerthree


def database_router_vc(requestData):
    try:
        if (requestData):
            database_to_use = 'default'
            return database_to_use
        else :
            return None
    except Exception as error:
        pass


class SendFirstResponse(APIView):
    def post(self,request):
        value = None
        try:
            active_database = database_router_vc('request')
            company = Customers.objects.using(active_database).filter(company=request.data['company'])
            user_customer = Artists.objects.using(active_database).get(artistid=request.data['artistid'])
            customer_data=Customers.objects.using(active_database).filter(country=request.data['country'])
            serializerdata=Someserializer(user_customer).data
            serializerdatatwo=Someserializertwo(customer_data,many=True).data
            serializerdatathree=Someserializerthree(company,many=True).data
            print("company",company)
            message = 'inside post method'
            value='xyz'
            return Response({"message":message,"value":value,"user_customer":serializerdata,"serializerdatatwo":serializerdatatwo,"companies":serializerdatathree})
        except Exception as error:
            print("Error: ", error)
            user_customer="Not Valid data"
            message = 'inside get exception method'
            return Response({"message":message,"value":value,"user_customer":None,"serializerdatatwo":None})
