from .views import Product,ProductItem,ProductCategory
from django.urls.conf import path

urlpatterns = [
    path('products/',Product.as_view()),
    path('products/<int:item_id>', ProductItem.as_view()),
    path('products/category/<str:category_id>', ProductCategory.as_view())
]