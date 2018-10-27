from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('customers', CustomerViewSet, base_name='customers')
#router.register('transaction', transaction, base_name='transaction')
urlpatterns = [
    path('transaction/', Transaction.as_view()),
]


urlpatterns += router.urls