from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from .models import *
from .serializer import *
import decimal
from rest_framework import generics
from rest_framework import viewsets, status

###hello

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


from rest_framework.views import APIView


class Transaction(APIView):  # allowed only post and option
    def post(self, request):
        accountNumber = request.data.get("accountNumber")
        transactionAmount = decimal.Decimal(request.data.get("transactionAmount"))
        transactionMethod = request.data.get("transactionMethod")
        customerAccount = Account.objects.filter(accountNumber=accountNumber)
        customerAmount = customerAccount[0].accountBalance
        print(customerAmount)
        if transactionMethod == "D":
            customerAmount = customerAmount + transactionAmount
        elif transactionMethod == "W":
            customerAmount = customerAmount - transactionAmount

        account_serializer = AccountSerializer(customerAccount[0],
                                         data={"accountBalance": customerAmount, "accountType": "SB", "customer": 1})

        if account_serializer.is_valid():
            account = account_serializer.save()
            return Response(account_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        '''
        return Response(customerAmount, status=status.HTTP_201_CREATED)
        '''