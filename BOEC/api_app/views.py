from django.views import View
from django.http import JsonResponse
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from api_app import models

class Product(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        p_title = data.get('title')
        p_des = data.get('description')
        p_price = data.get('price')
        p_category = data.get('category')

        product_data = {
            'title' : p_title,
            'description' : p_des,
            'price' : p_price,
            'category' : p_category
        }

        product = models.Product.objects.create(**product_data)
        data = {
            "message": f"New product added with id: {product.id}"
        }
        return JsonResponse(data,status=201)

    def get(self, request):
        items = models.Product.objects.all()

        items_data = []
        for item in items:
            items_data.append({
                'id' : item.id,
                'title': item.title,
                'description': item.description,
                'price': item.price,
                'category' : item.category
            })
        return JsonResponse(items_data,safe=False)  #Trả về json array -> ko có key -> set safe=false

class ProductItem(View):
    def patch(self, request, item_id):
        data = json.loads(request.body.decode("utf-8"))
        item = models.Product.objects.get(id=item_id)
        item.quantity = data['quantity']
        item.save()

        data = {
            'message': f'Product {item_id} has been updated'
        }
        return JsonResponse(data)

    def get(self, request, item_id):
        item = models.Product.objects.get(id=item_id)
        product_data = {
            'id' : item.id,
            'title' : item.title,
            'description' : item.description,
            'price' : item.price,
            'category' : item.category
        }
        return JsonResponse(product_data)


class ProductCategory(View):
    def get(self, request, category_id):
        items = models.Product.objects.filter(category=category_id)
        items_data = []
        for item in items:
            items_data.append({
                'id' : item.id,
                'title': item.title,
                'description': item.description,
                'price': item.price,
                'category' : item.category
            })
        return JsonResponse(items_data,safe=False)  #Trả về json array -> ko có key -> set safe=false

