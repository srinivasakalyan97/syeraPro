from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Artists, Customers, Invoices
from .serializer import Someserializer, Someserializertwo, Someserializerthree, Someserializerfour


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
            customer_data=Customers.objects.using(active_database).filter(customerid=request.data['customerid'])
            invoicedata=Invoices.objects.using(active_database).filter(customerid=request.data['customerid'])
            serializerdatatwo=Someserializertwo(customer_data,many=True).data
            serializerdatafour=Someserializerfour(invoicedata,many=True).data
            message = 'inside post method'
            value='xyz'
            return Response({"message":message,"value":value,"serializerdatatwo":serializerdatatwo,"serializerdatafour":serializerdatafour})
        except Exception as error:
            print("Error: ", error)
            user_customer="Not Valid data"
            message = 'inside get exception method'
            return Response({"message":message,"value":value,"user_customer":None,"serializerdatatwo":None})

class UpdateCustomerDetails(APIView):
    def post(self,request):
        pass #Update the users address