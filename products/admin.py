from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from products.models import Category, Brand, Allergy, Product

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"categorySlug": ("categoryName",)}

admin.site.register(Category, CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"brandSlug": ("brandName",)}

admin.site.register(Brand, BrandAdmin)

class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('productAllergies',)

admin.site.register(Product, ProductAdmin)

class AllergyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"allergySlug": ("allergyName",)}

admin.site.register(Allergy, AllergyAdmin)


