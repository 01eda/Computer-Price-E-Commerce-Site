from django.shortcuts import render
from django.http import HttpResponse
from home.models import Setting
from product.models import Product
from product.models import Category
from product.models import Images


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    dayproducts=Product.objects.all()

    product=Product.objects.all().order_by('?')[:7]
    context ={'setting':setting, 'page': 'home','dayproducts':dayproducts,
        'product':product     }
    return render(request,'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context ={'setting':setting , 'page':'hakkimizda'}
    return render(request,'hakkimizda.html', context)

def products(request):
    setting = Setting.objects.get(pk=1)
    product=Product.objects.all()
    query =request.GET.get('q')
    if query:
        product=product.filter(title__icontains=query)


    sort_by = request.GET.get("sort", "l2h")
    if sort_by == "l2h":
        product =product.order_by("price")
    elif sort_by == "h2l":
        product =product.order_by("-price")
    elif sort_by == "2lh":
        product = product.order_by("-puan")
    context ={'setting':setting , 'page':'products','product':product,}
    return render(request,'products.html', context)

def ayrinti(request,id):
    setting = Setting.objects.get()
    product = Product.objects.get(id=id)
    """images = Images.object.filter(product_id=id)"""
    context ={'setting':setting,'page':'ayrinti','product':product,


             }
    return render(request,'ayrinti.html', context)

def category(request,id):
    setting = Setting.objects.get()
    category = Category.object.all()
    categorydate = Category.objects.get(pk=id)
    product= Product.objects.filter(category_id=id)
    context ={'page':'ayrinti','product':product,
              'category':category,
              'categorydate':categorydate,
              'setting':setting,
              }
    return render(request,'product.html', context)

