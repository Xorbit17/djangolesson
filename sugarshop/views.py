from django.shortcuts import render


# Create your views here.
from sugarshop.models import Product, Composition


def home(request):
    return render(request, "home.html", {})

def catalog(request):
    allproducts = Product.objects.all()

    context = {
        "product_list": allproducts,
    }

    return render(request,"catalog.html", context)

