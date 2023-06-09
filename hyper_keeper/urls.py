from django.urls import path
from .views import HomeAppliancesList, HomeAppliancesDetail, EdiblesList, EdiblesDetail, ClothesList, ClothesDetail

urlpatterns = [
    path('homeAppliances-list/', HomeAppliancesList.as_view(), name='homeAppliances-list'),
    path('homeAppliances-list/<int:pk>/', HomeAppliancesDetail.as_view(), name='homeappliancesmodel-detail'),

    path('edibles-list/', EdiblesList.as_view(), name='edibles-list'),
    path('edibles-list/<int:pk>/', EdiblesDetail.as_view(), name='ediblesmodel-detail'),

    path('clothes-list/', ClothesList.as_view(), name='clothes-list'),
    path('clothes-list/<int:pk>/', ClothesDetail.as_view(), name='clothesmodel-detail'),
]