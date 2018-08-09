from django.db import models

class Category(models.Model):
    categoryId = models.AutoField(primary_key=True, editable=False)
    categoryName = models.CharField(verbose_name=u"Category", max_length=70)
    categorySlug = models.SlugField(unique=True)

    def __str__(self):
        return self.categoryName

    class Meta:
        ordering = ["categoryName"]


class Featured(models.Model):
    featured_id = models.AutoField(primary_key=True, editable=False)
    product_id = models.CharField(verbose_name=u"product_id", max_length=70)
    username = models.CharField(verbose_name=u"username", max_length=70, blank=True)

    # def __str__(self):
    #     return self.

    class Meta:
        ordering = ["featured_id"]


class Brand(models.Model):
    brandId = models.AutoField(primary_key=True, editable=False)
    brandName = models.CharField(verbose_name=u"Brand Name", max_length=70)
    brandSlug = models.SlugField(unique=True)
    brandContactNz = models.CharField(verbose_name=u"Contact NZ", max_length=70, blank=True)
    brandContactAu = models.CharField(verbose_name=u"Contact Australia", max_length=70, blank=True)

    def __str__(self):
        return self.brandName

    class Meta:
        ordering = ["brandName"]


class Allergy(models.Model):
    allergyId = models.AutoField(primary_key=True, editable=False)
    allergyName = models.CharField(verbose_name=u"Allergy", max_length=70)
    allergySlug = models.SlugField(unique=True)

    def __str__(self):
        return self.allergyName

    class Meta:
        ordering = ["allergyName"]


class Product(models.Model):
    productId = models.AutoField(primary_key=True, editable=False)
    productCategory = models.ForeignKey('products.Category', verbose_name=u"Category")
    productBrand = models.ForeignKey('products.Brand', verbose_name=u"Brand")
    productName = models.CharField(verbose_name=u"Product Name", max_length=150)
    productFlavour = models.CharField(verbose_name=u"Product Flavour", max_length=150, blank=True)
    productAllergies = models.ManyToManyField('products.Allergy', blank=True, verbose_name=u"Allergies")
    productImage = models.ImageField(verbose_name=u"Product Image", upload_to = 'media/products', blank=True)

    def __str__(self):
        return '%s %s %s' % (self.productBrand, self.productName, self.productFlavour)

    class Meta:
        ordering = ["productBrand", "productName", "productFlavour"]


class VerificationCode(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    email = models.CharField(verbose_name=u"user email", max_length=150)
    code = models.CharField(verbose_name=u"code", max_length=150)
    used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ["created_at"]
