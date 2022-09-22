from rest_framework import routers
from DashboardApp.views import FirmViewSet, UserViewSet, ProductViewSet, TransactionViewSet


router = routers.SimpleRouter()
router.register(r'firm', FirmViewSet)
router.register(r'user', UserViewSet)
router.register(r'product', ProductViewSet)
router.register(r'transaction', TransactionViewSet)
