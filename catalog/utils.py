from .models import Product, PriceHistory
from catalog.scraper import scrape_amazon, scrape_flipkart, scrape_myntra, scrape_ajio
from django.utils import timezone

def update_product_price(product_url, site):
    if site == 'Amazon':
        name, price, image = scrape_amazon(product_url)
    elif site == 'Flipkart':
        name, price, image = scrape_flipkart(product_url)
    elif site == 'Myntra':
        name, price, image = scrape_myntra(product_url)
    elif site == 'Ajio':
        name, price, image = scrape_ajio(product_url)
    else:
        return None, None

    if price is None:
        return None, None

    product, created = Product.objects.get_or_create(url=product_url, defaults={'name': name, 'site': site, 'image_url': image})
    if not created:
        product.name = name
        product.image_url = image
        product.save()
    PriceHistory.objects.create(product=product, price=price, checked_at=timezone.now())
    return product, price


from django.db.models import Min
from datetime import timedelta

def get_lowest_price(product):
    from django.utils import timezone
    year_ago = timezone.now() - timedelta(days=365)
    min_price = PriceHistory.objects.filter(product=product, checked_at__gte=year_ago).aggregate(Min('price'))['price__min']
    return min_price if min_price else 0


from django.core.mail import send_mail
from .models import PriceAlert

def check_price_alert(product, price):
    min_year_price = get_lowest_price(product)
    alerts = PriceAlert.objects.filter(product=product, notified=False)
    for alert in alerts:
        if price <= min_year_price and price <= alert.target_price:
            send_mail(
                'Price Drop Alert!',
                f'The product {product.name} has dropped to ₹{price}. Visit: {product.url}',
                'noreply@yourapp.com',
                [alert.user.email],
            )
            alert.notified = True
            alert.save()
