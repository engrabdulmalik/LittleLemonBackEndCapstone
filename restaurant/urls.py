from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'booking', views.BookingViewSet)
urlpatterns = [
    path('', views.index, name='index'),

    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),

]
