from django.views import View
from django.http import JsonResponse
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from api_app import models

class Product(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        p_name = data.get('name')
        p_des = data.get('description')
        p_price = data.get('price')
        p_quantity = data.get('quantity')

        product_data = {
            'name' : p_name,
            'description' : p_des,
            'price' : p_price,
            'quantity' : p_quantity
        }

        product = models.Product.objects.create(**product_data)
        data = {
            "message": f"New product added with id: {product.id}"
        }
        return JsonResponse(data,status=201)

    def get(self, request):
        items_count = models.Product.objects.count()
        items = models.Product.objects.all()

        items_data = []
        for item in items:
            items_data.append({
                'id' : item.id,
                'name': item.name,
                'description': item.description,
                'price': item.price,
                'quantity' : item.quantity
            })

        data = {
            'items': items_data,
            'count': items_count,
        }
        return JsonResponse(data)

class ProductUpdate(View):
    def patch(self, request, item_id):
        data = json.loads(request.body.decode("utf-8"))
        item = models.Product.objects.get(id=item_id)
        item.quantity = data['quantity']
        item.save()

        data = {
            'message': f'Product {item_id} has been updated'
        }

        return JsonResponse(data)

