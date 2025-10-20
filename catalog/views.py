from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product, PriceHistory, PriceAlert
from django.contrib.auth.decorators import login_required
from .utils import update_product_price, get_lowest_price, check_price_alert
from .scraper import search_and_scrape
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import time


def register(request):
    """
    User registration view
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome {user.first_name}! Registration successful!")
            return redirect("home")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegisterForm()
    return render(request, "catalog/register.html", {"form": form})



def user_login(request):
    """
    User login view
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "catalog/login.html", {"form": form})


def user_logout(request):
    """
    User logout view
    """
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect("login")


def home(request):
    """
    Home page - Shows saved products or search results
    """
    search_query = request.GET.get('q', '')
    
    if search_query:
        # Live search and scrape across all websites
        messages.info(request, f"Searching for '{search_query}' across all websites...")
        scraped_results = search_and_scrape(search_query)
        return render(request, "catalog/search_results.html", {
            "products": scraped_results, 
            "search_query": search_query
        })
    
    # Show saved products from database
    products = Product.objects.all().order_by('-id')  # Latest first
    product_list = []
    for product in products:
        latest_price_obj = PriceHistory.objects.filter(product=product).order_by('-checked_at').first()
        latest_price = latest_price_obj.price if latest_price_obj else "-"
        lowest_price = get_lowest_price(product)
        product_list.append({
            "id": product.id,
            "name": product.name,
            "site": product.site,
            "latest_price": latest_price,
            "lowest_price": lowest_price,
            "url": product.url,
            "image_url": product.image_url,
        })
    return render(request, "catalog/product_list.html", {
        "products": product_list, 
        "search_query": search_query
    })


@login_required
def set_alert(request, product_id):
    """
    Set price alert for a product
    """
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == "POST":
        target_price = float(request.POST.get("target_price"))
        
        # Check if alert already exists for this user and product
        existing_alert = PriceAlert.objects.filter(user=request.user, product=product, notified=False).first()
        
        if existing_alert:
            existing_alert.target_price = target_price
            existing_alert.save()
            messages.info(request, f"Price alert updated to ₹{target_price} for {product.name}")
        else:
            PriceAlert.objects.create(
                user=request.user,
                product=product,
                target_price=target_price,
                notified=False
            )
            messages.success(request, f"Price alert set at ₹{target_price} for {product.name}!")
        
        return redirect("home")
    
    return render(request, "catalog/set_alert.html", {"product": product})


@csrf_exempt
def save_product(request):
    """
    Save a product from search results to the database (AJAX endpoint)
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get('name')
            url = data.get('url')
            site = data.get('site')
            price = data.get('price')
            
            # Validate data
            if not all([name, url, site, price]):
                return JsonResponse({
                    'status': 'error', 
                    'message': 'Missing required fields'
                })
            
            # Create or update product
            product, created = Product.objects.get_or_create(
                url=url,
                defaults={
                    'name': name,
                    'site': site,
                }
            )
            
            # Update product name if it changed
            if not created and product.name != name:
                product.name = name
                product.save()
            
            # Add price history
            PriceHistory.objects.create(
                product=product,
                price=float(price)
            )
            
            if created:
                return JsonResponse({
                    'status': 'success', 
                    'message': 'Product saved successfully!'
                })
            else:
                return JsonResponse({
                    'status': 'success', 
                    'message': 'Product already exists. Price updated!'
                })
                
        except json.JSONDecodeError:
            return JsonResponse({
                'status': 'error', 
                'message': 'Invalid JSON data'
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error', 
                'message': f'Error: {str(e)}'
            })
    
    return JsonResponse({
        'status': 'error', 
        'message': 'Invalid request method'
    })


@login_required
def delete_product(request, product_id):
    """
    Delete a saved product (also deletes related price history and alerts)
    """
    product = get_object_or_404(Product, id=product_id)
    product_name = product.name
    
    # Delete product (cascades to PriceHistory and PriceAlert due to ForeignKey)
    product.delete()
    
    messages.success(request, f"Product '{product_name}' deleted successfully!")
    return redirect("home")
