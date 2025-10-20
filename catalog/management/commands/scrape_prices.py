from django.core.management.base import BaseCommand
from catalog.models import Product
from catalog.utils import update_product_price, check_price_alert

class Command(BaseCommand):
    help = "Scrape current prices for all products and update database."

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for product in products:
            self.stdout.write(f"Scraping {product.site}: {product.name}")
            updated_product, new_price = update_product_price(product.url, product.site)
            if updated_product and new_price:
                self.stdout.write(self.style.SUCCESS(f"Updated {product.name} ({product.site}) to price ₹{new_price}"))
                check_price_alert(updated_product, new_price)
            else:
                self.stdout.write(self.style.WARNING(f"Failed to update {product.name} ({product.site})"))
        self.stdout.write(self.style.SUCCESS("Price scraping finished."))
