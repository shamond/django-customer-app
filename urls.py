from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, InteractionViewSet, OrderViewSet, NoteViewSet, MarketingCampaignViewSet, TicketViewSet, PotentialClientViewSet
#routers are used to automatically generate URLs for ViewSets.
#routers simplify the process of creating standard URL paths for CRUD

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'interactions', InteractionViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'marketing_campaigns', MarketingCampaignViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'potential_clients', PotentialClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]