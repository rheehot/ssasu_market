from django.shortcuts import render, redirect, get_object_or_404
from .models import VisitoRecord, Market, Review, Openhour, Visitor
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET
from datetime import datetime
from .serializers import MarketSerializer, VisitorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from qr_code.qrcode.utils import ContactDetail, QRCodeOptions
from django.contrib.auth import get_user_model
User = get_user_model()

# market 관련 api
@api_view(['GET'])
@permission_classes([AllowAny])
def info(request):
    markets = Market.objects.all()
    serializer = MarketSerializer(markets, many=True)
    return Response(serializer.data)


# VisitorRecord 정보 저장 api
@api_view(['POST'])
@permission_classes([AllowAny])
def make_visitor_record(request, market_pk):
    serializer = VisitorSerializer(data = request.data)
    user_id = request.data.get('user_id')
    if serializer.is_valid(raise_exception=True):
        serializer.save(market = market_pk)
    return Response(serializer.data)


# Visitor 정보 저장 api
@api_view(['POST'])
@permission_classes([AllowAny])
def makevisitor(request):
    serializer = VisitorSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return HttpResponse('Sucess Visitor')


# qrcode 보여주는 api
DEMO_OPTIONS = QRCodeOptions(size='t', border=6, error_correction='L')

def qrcode_page(request, market_pk):
    user_id = get_object_or_404(User, pk=userid)
    market_id = get_object_or_404(Market, pk=market_pk)
    context = dict(
        options_example=DEMO_OPTIONS,
        user=user_id["user_id"],
        market=market_id["name"]
    )

    return render(request, 'market/qrcode_page.html', context=context)
