from django.shortcuts import render, get_object_or_404
from .models import Category

def category_list(request):
    categories = Category.objects.filter(parent__isnull=True)  # Top-level categories
    return render(request, 'category/category_list.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    subcategories = category.get_children()  # Get subcategories of this category
    return render(request, 'category/category_detail.html', {
        'category': category,
        'subcategories': subcategories
    })
