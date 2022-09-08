from django.shortcuts import render
from store.models import Product

def say_hello(request):
    # queryset = TaggedItem.objects.get_tags_for(Product, 1)
     

    return render(request, "hello.html", {"name": "Mosh", "Products": list(products)})