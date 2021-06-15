from .views import Product,ProductUpdate
from django.urls.conf import path

urlpatterns = [
    path('products/',Product.as_view()),
    path('products/<int:item_id>', ProductUpdate.as_view())
]