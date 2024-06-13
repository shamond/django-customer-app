from rest_framework import viewsets
from .models import Client, Interaction, Order, Note, MarketingCampaign, Ticket, PotentialClient
from .serializer import ClientSerializer, InteractionSerializer, OrderSerializer, NoteSerializer, MarketingCampaignSerializer, TicketSerializer, PotentialClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class MarketingCampaignViewSet(viewsets.ModelViewSet):
    queryset = MarketingCampaign.objects.all()
    serializer_class = MarketingCampaignSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class PotentialClientViewSet(viewsets.ModelViewSet):
    queryset = PotentialClient.objects.all()
    serializer_class = PotentialClientSerializer