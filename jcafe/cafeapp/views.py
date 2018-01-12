from django.shortcuts import render
from .models import Menu, Offer, Booking, Feedback
from rest_framework import generics, status
from .serializers import MenuSerializers, OfferSerializers, BookingSerializers, FeedbackSerializers
from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from django.core.mail import EmailMessage

today = date.today()

# Create your views here.

class MenuCard(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

class MenuUpdate(generics.DestroyAPIView):
        queryset = Menu.objects.all()
        serializer_class = MenuSerializers

# class Offer(generics.ListCreateAPIView):
#     queryset = Offer.objects.filter(expiry_date__year__gte=today.year)
#     serializer_class = OfferSerializers

class Feedbacks(generics.ListCreateAPIView):
        queryset = Feedback.objects.all()
        serializer_class = FeedbackSerializers

'''
class Booking(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
'''

@api_view(['GET', 'POST'])
def offers(request):
    if request.method =='GET':
        offer_object = Offer.objects.filter(expiry_date__year__gte=today.year)
        serializer = OfferSerializers(offer_object, many=True)
        return Response(serializer.data)

    elif request.method =='POST':
            serializer = OfferSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = request.POST.get('title', "")
                message = message+"\n Description:"+request.POST.get('description', "")+"\n Offer Valid Till:"+request.POST.get('expiry_date', "")
                emails = Feedback.objects.all()
                email_list = []
                for ob in emails:
                    email_list.append(ob.email)
                email = EmailMessage('Jcafe_Offer', message, to=email_list)
                email.send()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def booking_list(request):
    if request.method =='GET':
        bookings = Booking.objects.all()
        serializer = BookingSerializers(bookings, many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        total_tables = 2
        if Booking.objects.filter(date__day=today.day).count() < total_tables :
            serializer = BookingSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = "Dear "+request.POST.get('name', "")+"\n Your table has booked"
                email = EmailMessage('Table Booking', message, to=[request.POST.get('email', "")])
                email.send()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return  Response({"errorname": "full"}, status=205)

@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    # email = EmailMessage('test', 'sample text', to=['vaibhavj42@gmail.com'])
    # email.send()
    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})
