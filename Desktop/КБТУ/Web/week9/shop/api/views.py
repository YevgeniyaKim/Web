from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from .models import *


def categories(request):
    cat = Category.objects.all()
    cat_json = [c.to_json() for c in cat]
    return JsonResponse(cat_json, safe=False)


def category(request, category_id):
    try:
        cat = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(cat.to_json())


def category_products(request, category_id):
    try:
        cat = Category.objects.get(id=category_id)
        products = Product.objects.filter(category=cat)
        products_json = [p.to_json() for p in products]
        return JsonResponse(products_json, safe=False)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})


def products(request):
    prd = Product.objects.all()
    prd_json = [p.to_json() for p in prd]
    return JsonResponse(prd_json, safe=False)


def product(request, product_id):
    try:
        prd = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(prd.to_json())
