from django.urls import path
from . import views

urlpatterns = [
    path("", views.PurchaseOrderView.as_view(), name="orders"),
    path("<str:po_id>/", views.PurchaseOrderDetailView.as_view()),
    path(
        "<str:po_id>/acknowledge/",
        views.AcknowledgePurchaseOrderView.as_view(),
    ),
]
