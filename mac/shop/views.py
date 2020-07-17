from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Product
from math import ceil


# Create your views here.
def index(request):
    products=Product.objects.all()
    # n=len(products)
    # nSlides=(n//4)+ceil((n/4)-(n//4))

    # params={'product':products, 'no_of_slides':nSlides, 'range':range(1,nSlides)}

    # all_prods=[[products,nSlides,range(1,nSlides)],
    #            [products,nSlides,range(1,nSlides)]]

    all_prods=[]
    catprods=Product.objects.values('category','id')
    # print(f"catprods------{catprods}")    # o/p: catprods------<QuerySet [{'category': 'Electronics', 'id': 1}, {'category': 'Accessories', 'id': 2}, {'category': 'Computer', 'id': 3}, {'category': 'Electronics', 'id': 4}, {'category': 'Electronics', 'id': 5}, {'category': 'Electronics', 'id': 6}, {'category': 'T-shirt', 'id': 7}, {'category': 'Footwear', 'id': 8}]>
    cats={item['category'] for item in catprods}
    # print(f"cats------{cats}")   #o/p: cats------{'T-shirt', 'Footwear', 'Accessories', 'Electronics', 'Computer'}
    for cat in cats:
        prods=Product.objects.filter(category=  cat)
        # print(f"prods------{prods}")     # o/p:prods------<QuerySet [<Product: Levis>]>            prods------<QuerySet [<Product: SunGlass>]>            prods------<QuerySet [<Product: watch>, <Product: Bajaj Mixer Graner>, <Product: Jio Phone>, <Product: HP>]>              prods------<QuerySet [<Product: Mouse>]>                 prods------<QuerySet [<Product: Puma Shoes>]> 
        n=len(prods)
        nSlides=(n//4)+ceil((n/4)-(n//4))
        all_prods.append([prods, nSlides, range(1,nSlides)])
    # print(f"all_prods------{all_prods}")      # o/p: all_prods------[[<QuerySet [<Product: Levis>]>, 1, range(1, 1)], [<QuerySet [<Product: Puma Shoes>]>, 1, range(1, 1)], [<QuerySet [<Product: Mouse>]>, 1, range(1, 1)], [<QuerySet [<Product: watch>, <Product: Bajaj Mixer Graner>, <Product: Jio Phone>, <Product: HP>]>, 1, range(1, 1)], [<QuerySet [<Product: SunGlass>]>, 1, range(1, 1)]]
    params={"allProds":all_prods}
    return render(request,'shop/index.html', params)


def about(request):
    return render(request,'shop/about.html')


def contact(request):
    return render(request,'shop/contact.html')


def tracker(request):
    return render(request,'shop/tracker.html')


def search(request):
    return render(request,'shop/search.html')


def prodview(request):
    return render(request,'shop/prodview.html')


def checkout(request):
    return render(request,'shop/checkout.html')



