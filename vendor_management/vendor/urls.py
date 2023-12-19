from django.urls import path
from . import views
urlpatterns = [
    path("", views.VendorListView.as_view(), name='vendors-list'),
    path("<str:vendor_id>/", views.VendorDetailView.as_view(), name="vendor"),
    path("<str:vendor_id>/performance/", views.VendorPerformanceView.as_view()),


]
