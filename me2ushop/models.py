from django.conf import settings
from Me2U.settings import PRODUCTS_PER_ROW
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Count
from django.db.models.signals import post_save
from django.utils import timezone
from django.shortcuts import reverse
from django_countries.fields import CountryField
from categories.models import Category, Department
from users.models import Profile, SellerProfile, STATUSES, UNDER_REVIEW
from utils.models import CreationModificationDateMixin
from sellers.models import Sellers
from PIL import Image
from django.db import models
from stdimage import StdImageField, JPEGField
import collections
from tagging.registry import register
from tagging.models import Tag
import itertools
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.functional import cached_property

CATEGORY_CHOICES = (
    ('At', 'Arts, Crafts'),
    ('Bk', 'Books'),
    ('Bb', 'Baby Care'),
    ('Be', 'Beautiful 2'),
    ('Ca', 'Camera & Photo'),
    ('S', 'Shirt'),
    ('Sw', 'Sport wear'),
    ('Ow', 'Outwear'),
    ('Am', 'Automotive & Motorcycle'),
    ('Ca', 'Cell Phones & Accessories'),
    ('El', 'Electronics'),
    ('Fa', 'Fashion'),
    ('Fu', 'Furniture'),
    ('So', 'Sokoni'),
    ('Wo', 'Women Fashion')
)
LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),

)
ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping')
)

PAYMENT_CHOICES = {

    ('M', "M-Pesa"),
    ('P', "Paypal"),
    ('S', "Stripe"),

}

SUBSCRIPTION_TYPE_CHOICE = (
    ('Fr', 'Free'),
    ('Bs', 'Basic'),
    ('Pr', 'Premium')
)

BUSINESS_TYPE_CHOICE = (
    ('Co', 'Company'),
    ('Sol', 'Sole Proprietorship/Personal')
)

CONDITION_CHOICES = {

    ('N', "New"),
    ('R', "Refurbished"),
    ('U', "Used"),

}
SHIPPING_CAPABILITY = (
    ('Cd', 'Can Ship Abroad and Deliver Locally'),
    ('Cl', 'Can Deliver Locally'),
    ('CO', 'Not Able to Deliver')
)
from django_countries import Countries


class AfrikanCountries(Countries):
    only = [
        'DZ', 'AO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD',
        'KM', 'CG', 'CD', 'CI', 'DJ', 'EG', 'GQ', 'ER', 'ET', 'GA',
        'GM', 'GH', 'GN', 'GW', 'KE', 'LS', 'LR', 'LY', 'MG', 'ML',
        'MW', 'MR', 'MU', 'YT', 'MA', 'MZ', 'NA', 'NE', 'NG', 'RE',
        'RW', 'ST', 'SN', 'SC', 'SL', 'SO', 'ZA', 'SS', 'SD', 'SZ',
        'TZ', 'TG', 'TN', 'UG', 'EH', 'ZM', 'ZW'
    ]


class Brand(CreationModificationDateMixin):
    user = models.ForeignKey(SellerProfile, on_delete=models.CASCADE, null=True, default=1)
    title = models.CharField(max_length=100, unique=True, help_text='Unique business title to identify Your store and '
                                                                    'your product line')

    business_phone = models.CharField(max_length=20, blank=True, null=True,
                                      help_text='Business Phone Number . i.e +250785....')
    business_email = models.EmailField(blank=True, null=True, max_length=254,
                                       help_text='Business Phone Number . i.e +250785....')
    business_description = models.TextField(help_text="Tell us what you do and the kind of products you sell")

    website_link = models.CharField(max_length=255, blank=True, null=True,
                                    help_text='If you have a website by which buyers can find out more about your '
                                              'services.e.g. https://www.facebook.com')
    facebook = models.CharField(max_length=255, blank=True, null=True,
                                help_text='Do you have a facebook page. Copy paste your page link here '
                                          'e.g..https://www.facebook.com/Me2UAfrika')
    instagram = models.CharField(max_length=255, blank=True, null=True,
                                 help_text='Do you have a instagram page. Copy paste your page link here '
                                           'eg..https://www.instagram.com/me2u_afrika/')
    twitter = models.CharField(max_length=255, blank=True, null=True,
                               help_text='Do you have a Telegram Channel. Copy paste your page link here. '
                                         'e.g..https://t.me/me2uafrika')
    business_type = models.CharField(choices=BUSINESS_TYPE_CHOICE, max_length=4)
    # date_of_registration = models.DateField
    country = CountryField(multiple=False)
    subscription_type = models.CharField(max_length=2, choices=SUBSCRIPTION_TYPE_CHOICE,
                                         help_text='Select a monthly recurring subscription fees')
    shipping_status = models.CharField(choices=SHIPPING_CAPABILITY, max_length=2, blank=True, null=True,
                                       help_text='Is Your company able to ship or deliver your products once they '
                                                 'buyers order online?')
    valid_payment_method = models.BooleanField(default=False, null=True, blank=True)
    active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False, blank=True, null=True)
    image = StdImageField(upload_to='images/brands/brand_background', blank=True, null=True,
                          help_text='wallpaper for your store.Leave blank if you don\'t have one',
                          default='images/brands/brand_background/default.jpg', variations={
            'large': (415, 470,), }, delete_orphans=True)

    logo = StdImageField(upload_to='images/brands/brand_logo', blank=True, null=True,
                         help_text='logo for your store, Leave blank if you don\'t have one',
                         variations={
                             'medium': (150, 150, True),

                         }, delete_orphans=True)
    application_status = models.IntegerField(choices=STATUSES, default=UNDER_REVIEW, blank=True, null=True)

    def __str__(self):
        return str(self.title)


class ActiveProductManager(models.Manager):
    def all(self):
        return super(ActiveProductManager, self).all().filter(is_active=True).prefetch_related('productimage_set')


class ProductManager(models.Manager):
    def get_by_natural_key(self, slug):
        return self.get(slug=slug)

class Product(CreationModificationDateMixin):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,
                            default='',
                            editable=False,
                            max_length=50,
                            )
    brand_name = models.ForeignKey('Brand', on_delete=models.SET_NULL, blank=True, null=True,
                                   help_text='Your store name')
    stock = models.IntegerField(default=1)
    sku = models.CharField(max_length=120, default='',
                           editable=False, )
    in_stock = models.BooleanField(default=True, editable=False)
    # condition = models.CharField(choices=CONDITION_CHOICES, max_length=2,
    #                              help_text='Choose the current condition for the product'
    #                              )
    price = models.DecimalField(max_digits=9, decimal_places=2, help_text="Please note that the default currency is "
                                                                          "USD. Converty your product price to "
                                                                          "US dollar before listing")
    discount_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True,
                                         help_text="Please note that the default currency is "
                                                   "USD. Converty your product price to "
                                                   "US Dollar before listing")
    # made_in_afrika = models.BooleanField(default=False, help_text="Is the product you adding produced and "
    #                                                               "manufactured in Afrika? If so, check this box")

    is_active = models.BooleanField(default=True, editable=False)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_bestrated = models.BooleanField(default=False)

    description = models.TextField()
    additional_information = RichTextField(blank=True, null=True,
                                           help_text='Provide additional information about '
                                                     'your product. Buyers mostly buy from'
                                                     ' well detailed products and '
                                                     'specifications')
    meta_keywords = models.CharField("Meta Keywords",
                                     max_length=100,
                                     help_text='Comma-delimited set of SEO keywords that summarize the type of '
                                               'product above max 4 words. This keywords will help buyers find your '
                                               'product easily. Read more https://ads.google.com/home/tools/keyword'
                                               '-planner/')
    meta_description = models.CharField("Meta Description",
                                        max_length=255,
                                        help_text='Give a simple short '
                                                  'description on the information you have provided on the page this '
                                                  'page. i.e This product is used '
                                                  'for cleaning, cooking and it was recently released by it\'s '
                                                  'manufacturer. Google uses this keywords and description to index '
                                                  'your product for it to be found easily '
                                        )

    product_categories = models.ManyToManyField(Department,

                                                help_text='Check the box of the category where your product belongs. '
                                                          'Please note that different categories attract different Ad '
                                                          'charges. Be specific to one or two categories where your '
                                                          'product '
                                                          'belongs on the provided tree. Contact us for help')

    objects = ProductManager()
    active = ActiveProductManager()

    # made_in_afrika = ActiveAfricaProductManager()

    def __str__(self):
        return str(self.title)

    # def clean(self):
    #     # Don't allow draft entries to have a pub_date.
    #     if self.seller != settings.AUTH_USER_MODEL:
    #         print(self.seller)
    #         print(settings.AUTH_PROFILE_MODULE)
    #
    #         raise ValidationError('Please select your seller email prior to adding. Make sure the selected email '
    #                               'belongs to you.')

    def natural_key(self):
        return (self.slug,)

    class Meta:
        db_table = 'Products'
        ordering = ['-created']
        verbose_name_plural = 'Products'

    def get_category(self):
        pass

    def sale_price(self):
        if self.discount_price:
            return self.discount_price
        else:
            return self.price

    def total_items_ordered(self):
        orders = self.orderitem_set.all()
        total = 0
        for order_item in orders:
            if order_item.ordered:
                total += order_item.quantity

        return total

    def total_discount(self):
        # orders = self.orderitem_set.all()
        diff = ((self.price - self.discount_price) / self.price) * 100
        return round(diff)

    @cached_property
    def get_absolute_url(self):

        return reverse('me2ushop:product', kwargs={'slug': self.slug})

    @cached_property
    def get_add_cart_url(self):
        return reverse('me2ushop:add_cart', kwargs={'slug': self.slug})

    @cached_property
    def get_images(self):
        return self.productimage_set.all()

    @cached_property
    def get_image_in_display(self):
        image = self.productimage_set.filter(in_display=True)
        if image:
            return image[0]

    def get_remove_cart_url(self):
        return reverse('me2ushop:remove_cart', kwargs={'slug': self.slug})

    def get_order_summary_url(self):
        return reverse('me2ushop:order_summary')

    @cached_property
    def cross_sells(self):
        orders = Order.objects.filter(items__item=self)
        order_items = OrderItem.objects.filter(order__in=orders).exclude(item=self)
        products = Product.active.filter(orderitem__in=order_items).filter().distinct()
        return products

    @cached_property
    def cross_sells_user(self):
        from users.models import User

        users = User.objects.filter(order__items__item=self)
        items = OrderItem.objects.filter(order__user__in=users).exclude(item=self)
        products = Product.active.filter(orderitem__in=items).distinct()
        return

    @cached_property
    def cross_sells_sellers(self):
        from search.search import _prepare_words
        from users.models import User
        from django.db.models import Q

        category = self.product_categories
        name = self.title
        # print('category:', category)
        # print('name:', name)
        # print('other sellers:', users)
        # print('self', self.slug)
        words = _prepare_words(self.title)
        # print('words:', words)

        for word in words:
            products = Product.active.filter(
                Q(title__icontains=self) |
                Q(title__startswith=self) |
                Q(title__icontains=word) |
                Q(title__startswith=word) |
                Q(title__endswith=self) |
                Q(title__endswith=word)
            ).exclude(slug=self.slug)
            # print('from sellers', products)
            return products

    @cached_property
    def cross_sells_hybrid(self):
        from users.models import User

        from django.db.models import Q
        orders = Order.objects.filter(items__item=self)
        users = User.objects.filter(order__items__item=self)
        # print('users', users)
        items = OrderItem.objects.filter(Q(order__user__in=users) |
                                         Q(order__in=orders)
                                         ).exclude(item=self)

        products = Product.active.filter(orderitem__in=items)

        matching = []

        for product in products:
            matching.append(product)

        most_products = []

        c = collections.Counter(matching)

        for product, count in c.most_common(3):
            # print('%s: %7d' % (product, count))
            most_products.append(product)
        # print('most_products:', most_products)

        return most_products

    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        value = self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Product.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        return slug_candidate

    def _generate_sku(self):
        # Brand > Product > Category > Productcondition >

        brand = str(self.brand_name)[:3]
        title = str(self.title)[:3]
        # category = str(self.product_categories.all()[0])[:3]
        condition = str(self.created)

        sku = '{}-{}-{}'.format(brand, title, condition)

        for i in itertools.count(1):
            if not Product.objects.filter(sku=sku).exists():
                break
            sku = '{}-{}-{}-{}'.format(brand, title, condition, i)
        return sku

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = self._generate_slug()
            self.sku = self._generate_sku()

        if self.stock < 1:
            print('we came to check stock')
            self.in_stock = False

        image = self.productimage_set.filter(in_display=True)
        # print('image', image.exists())
        if image.exists() and self.in_stock:
            self.is_active = True
        else:
            self.is_active = False

        super().save(*args, **kwargs)


# Product model class definition here
# tags register
register(Product)


class DisplayImageManager(models.Manager):
    def get_query_set(self):
        return super(DisplayImageManager, self).get_query_set().filter(in_display=True)


class ProductImage(CreationModificationDateMixin):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = StdImageField(upload_to='images/products', variations={
        'thumbnail': (180, 150),
        'medium': (365, 365),
        'deals_size': (365, 365, True),
        'large': (415, 430),

    }, delete_orphans=True)

    in_display = models.BooleanField(default=True)

    objects = ProductManager()
    displayed = DisplayImageManager()

    class Meta:
        ordering = ('-in_display',)

    def __str__(self):
        return str(self.item)

    def natural_key(self):
        return (self.item.slug,)

    @cached_property
    def get_absolute_url(self):
        return reverse('me2ushop:product_images', kwargs={'slug': self.item.slug})


#
class VariationsManager(models.Manager):
    def all(self):
        return super(VariationsManager, self).filter(active=True)

    def sizes(self):
        return self.all().filter(category='size')

    def colors(self):
        return self.all().filter(category='color')


VAR_CATEGORIES = (
    ('size', 'size'),
    ('color', 'color'),
    ('package', 'package'),
)


class ProductDetail(CreationModificationDateMixin):
    """    The ``ProductDetail`` model represents information unique to a
    specific product. This is a generic design that can be used
    to extend the information contained in the ``Product`` model with
    specific, extra details.
    """
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    attribute = models.CharField(max_length=50)
    value = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    def __str__(self):
        return u'%s: %s - %s' % (self.product,
                                 self.attribute,
                                 self.value)

    def get_absolute_url(self):
        return reverse('me2ushop:product', kwargs={'slug': self.product.slug})


class ProductAttribute(CreationModificationDateMixin):
    """
    The ``ProductAttribute`` model represents a class of feature found
    across a set of products. It does not store any data values related to the attribute,
    but only describes what kind of a product feature we are trying to capture. Possible attributes include things such 4
    as materials, colors, sizes, and many, many more.
    """

    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __str__(self):
        return u'%s' % self.name


class Rentals(CreationModificationDateMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    book_start = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    book_end = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    rental_price_day = models.DecimalField(max_digits=9, decimal_places=2)
    discount_per_week = models.IntegerField(blank=True, null=True)
    discount_per_month = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return u'%s' % self.product


class WishList(CreationModificationDateMixin):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.title)


class StatusCode(CreationModificationDateMixin):
    """
    The StatusCode model represents the status of an order in the
    system.
    """
    NEW = 10
    PAID = 20
    PROCESSING = 30
    SENT = 40
    CANCELLED = 50
    IN_TRANSIT = 60
    DELIVERED = 70

    STATUSES = ((NEW, "New"),
                (PAID, "Paid"),
                (PROCESSING, "Processing"),
                (SENT, "Sent"),
                (CANCELLED, "Cancelled"),
                (IN_TRANSIT, "in_transit"),
                (DELIVERED, "Delivered"),
                )

    short_name = models.IntegerField(choices=STATUSES, default=NEW)
    name = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return str(self.short_name)


class OrderItem(CreationModificationDateMixin):
    # from stats.models import ProductView
    NEW = 10
    PROCESSING = 20
    SENT = 30
    CANCELLED = 40
    IN_TRANSIT = 45
    DELIVERED = 50

    STATUSES = ((NEW, "New"),
                (PROCESSING, "Processing"),
                (SENT, "Sent"),
                (CANCELLED, "Cancelled"),
                (IN_TRANSIT, "in_transit"),
                (DELIVERED, "Delivered"),
                )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    customer_order = models.ForeignKey('Order', blank=True, null=True, on_delete=models.SET_NULL)
    cart_id = models.CharField(max_length=40, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_ordered = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUSES, default=NEW)
    status_code = models.ForeignKey('StatusCode', on_delete=models.SET_NULL, blank=True, null=True)
    order_received = models.BooleanField(default=False)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.PROTECT, unique=False, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    comments = models.TextField(blank=True)
    delivered_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='dispatcher', on_delete=models.SET_NULL,
                                     blank=True, null=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_absolute_url(self):
        return reverse('users:order-details', kwargs={'order_id': self.id})

    def get_total_price(self):
        return self.quantity * self.item.price

    def get_total_discount_price(self):
        return self.quantity * self.item.discount_price

    def get_total_saved(self):
        return self.get_total_price() - self.get_total_discount_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_price()
        else:
            return self.get_total_price()

    def total_items_ordered(self):
        # total = self.orderitem_set.all().count()
        total = 0
        for order_item in self.filter(ordered=True):
            total += order_item.quantity

        return total

    @property
    def mobile_thumb_url(self):
        products = [self.item]
        # print('products:', products)
        if products:
            img = products[0].productimage_set.first()
            if img:
                return img.image.thumbnail.url

    @property
    def summary(self):
        pieces = ['%s x %s' % (self.quantity, self.item.title)]

        return ",".join(pieces)


class Order(CreationModificationDateMixin):
    NEW = 10
    PAID = 20
    DONE = 30
    STATUSES = ((NEW, 'New'), (PAID, 'Paid'), (DONE, 'Done'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                             db_index=True)
    cart_id = models.CharField(max_length=40, blank=True, null=True)
    status = models.IntegerField(choices=STATUSES, default=NEW)
    status_code = models.ForeignKey('StatusCode', on_delete=models.SET_NULL, blank=True, null=True)
    items = models.ManyToManyField('OrderItem')
    ref_code = models.CharField(max_length=20)
    start_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField(auto_now=True)
    ordered = models.BooleanField(default=False)
    payment = models.CharField(max_length=2, blank=True, null=True)
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(blank=True, null=True)
    refund_granted = models.BooleanField(blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    name = models.CharField(max_length=60, blank=True, null=True)
    billing_address1 = models.CharField(max_length=60)
    billing_address2 = models.CharField(max_length=60, blank=True)
    billing_zip_code = models.CharField(max_length=12)
    billing_country = models.CharField(max_length=3)
    billing_city = models.CharField(max_length=12, blank=True, null=True)

    # shipping_name = models.CharField(max_length=60, blank=True, null=True)
    shipping_address1 = models.CharField(max_length=60)
    shipping_address2 = models.CharField(max_length=60, blank=True)
    shipping_zip_code = models.CharField(max_length=12)
    shipping_country = models.CharField(max_length=3)
    shipping_city = models.CharField(max_length=12, blank=True, null=True)
    comments = models.TextField(blank=True)

    last_spoken_to = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name="cs_chats",
                                       on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-modified']

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):

        return reverse('users:order-details', kwargs={'order_id': self.id})

    def get_coupon_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        total -= self.coupon.amount
        return total

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

    def total_items(self):
        # total = self.orderitem_set.all().count()
        total = 0
        for order_item in self.items.all():
            total += order_item.quantity

        return total

    def get_total_saved_coupon(self):
        return self.get_total() - self.get_coupon_total()

    @property
    def mobile_thumb_url(self):
        products = [i.item for i in self.items.all()]
        # print('products:', products)
        if products:
            img = products[0].productimage_set.first()
            if img:
                return img.image.thumbnail.url

    @property
    def summary(self):
        product_counts = self.items.values(
            'quantity', 'item__title'
        )
        pieces = []
        for pc in product_counts:
            pieces.append(
                '%s x %s' % (pc['quantity'], pc['item__title'])
            )
        return ",".join(pieces)


class ActiveProductReviewManager(models.Manager):
    def all(self):
        return super(ActiveProductReviewManager, self) \
            .all().filter(is_approved=True)


class ProductReview(models.Model):
    RATINGS = ((5, 5), (4, 4), (3, 3), (2, 2), (1, 1))
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # ordered_by_user = models.ForeignKey(Order, ordered=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(default=5, choices=RATINGS)
    is_approved = models.BooleanField(default=True)
    content = models.TextField()
    country = CountryField(multiple=False, blank=True, null=True)

    objects = models.Manager()
    approved = ActiveProductReviewManager()

    def __str__(self):
        return str(self.user.username)

    def get_images(self):
        return self.product.productimage_set.all()


class Address(models.Model):
    from stats.models import ProductView
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    # cart_id = models.ForeignKey(ProductView, max_length=70, blank=True, null=True, on_delete=models.CASCADE)
    cart_id = models.CharField(max_length=40, blank=True, null=True)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    city = models.CharField(max_length=60)
    zip = models.CharField(max_length=10)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    payment_option = models.CharField(max_length=2, choices=PAYMENT_CHOICES)
    default = models.BooleanField(default=False)
    name = models.CharField(max_length=60, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    # contact info

    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.street_address, self.country, self.city, self.zip, self.phone)

    class Meta:
        verbose_name_plural = 'Addresses'
        ordering = ['-date_updated']


class StripePayment(models.Model):
    from stats.models import ProductView
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    cart_id = models.ForeignKey(ProductView, max_length=70, blank=True, null=True, on_delete=models.CASCADE)
    stripe_charge_id = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stripe_charge_id


class Coupon(models.Model):
    code = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=20)
    valid = models.BooleanField(default=True)

    def __str__(self):
        return str(self.code)


class RequestRefund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(blank=True, null=True)
    # email = models.EmailField()
    ref_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.pk}"
# class OrderAnonymous(OrderInfo): from stats.models import ProductView cart_id = models.ForeignKey(ProductView,
# max_length=70, blank=True, null=True, on_delete=models.CASCADE) billing_address = models.ForeignKey('Address',
# related_name='billing_address_anonymous', on_delete=models.SET_NULL, blank=True, null=True) shipping_address =
# models.ForeignKey('Address', related_name='shipping_address_anonymous', on_delete=models.SET_NULL, blank=True,
# null=True)
#
#     class Meta:
#         ordering = ['-order_date']
#         verbose_name_plural = 'OrderAnonymous'
#
#     def __str__(self):
#         return str(self.cart_id)
#
#     def get_total(self):
#         total = 0
#         for order_item in self.items.all():
#             total += order_item.get_final_price()
#         return total
#
#     def total_items(self):
#         total = 0
#         for order_item in self.items.all():
#             total += order_item.quantity
#         return total
#
