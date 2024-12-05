from django.db import models
from restaurant.models import MenuItem, Restaurant
from django.contrib.auth.models import User
from django.utils.timezone import now

# Customer Model
class Customer(models.Model):
    emailId = models.EmailField(max_length=200, unique=True)  # Use snake_case for consistency
    password = models.CharField(max_length=128)  # Increased to 128 for better password handling
    name = models.CharField(max_length=200)
    street = models.TextField()
    description = models.TextField(null=True, blank=True)
    pincode = models.IntegerField()
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Cart Item Model
class CartItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="cart_items")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        # Calculate total price automatically based on quantity
        self.total_price = self.menu_item.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} (Customer: {self.customer.name})"

# Order Model
class Order(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Preparing", "Preparing"),
        ("Delivered", "Delivered"),
        ("Canceled", "Canceled"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="orders")
    ordered_items = models.JSONField()  # Holds details of ordered items
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="Pending")
    ordered_at = models.DateTimeField(auto_now_add=True)
    delivery_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.name} at {self.restaurant.name}"
