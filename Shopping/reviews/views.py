from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from shop.models import Product

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        review_text = request.POST.get('review_text', '')
        review, created = Review.objects.update_or_create(
            user=request.user, product=product,
            defaults={'rating': rating, 'review_text': review_text}
        )
        return redirect('product', id=product.id)
    return render(request, 'reviews/add_review.html', {'product': product})

def product_reviews(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)
    return render(request, 'reviews/product_reviews.html', {'product': product, 'reviews': reviews})

