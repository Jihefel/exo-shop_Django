from django.shortcuts import render

# Create your views here.
products = [
    {
        "id": 1,
        "name": "Apple",
        "price": 0.5,
        "in_stock": True
    },
    {
        "id": 2,
        "name": "Banana",
        "price": 0.25,
        "in_stock": True
    },
    {
        "id": 3,
        "name": "Orange",
        "price": 0.35,
        "in_stock": False
    },
    {
        "id": 4,
        "name": "Grapes",
        "price": 0.15,
        "in_stock": True
    },
    {
        "id": 5,
        "name": "Watermelon",
        "price": 2.0,
        "in_stock": True
    }
]


def home(request):
    return render(request, "app_shop/home.html", {"products": products})

def cart(request):
    return render(request, "app_shop/cart.html")

def productDetails(request, id):
    return render(request, "app_shop/product_detail.html",{"product":products[id-1]})