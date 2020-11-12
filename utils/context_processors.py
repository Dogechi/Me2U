from categories.models import Category, Department
from me2ushop.models import Product, ProductReview, Brand, WishList
import os

from django.conf import settings

from stats import stats
from marketing.models import Deals


def me2u(request):
    brand = None
    wish_list = None

    if request.user.is_authenticated and request.user.is_seller:
        brand = Brand.objects.get(user=request.user),
    if request.user.is_authenticated:
        wish_list = WishList.objects.filter(user=request.user)
    #
    # deals = Deals.objects.all(),
    # if deals:

    return {'active_categories': Category.active.all(),
            'active_departments': Department.active.all(),
            'reviews': ProductReview.objects.all().order_by('-date'),
            'recently_viewed': stats.get_recently_viewed(request),
            'brand': brand,
            'brands': Brand.objects.filter(active=True),
            'deals': Deals.objects.all(),
            'wish_list': wish_list,
            'site_name': settings.SITE_NAME,
            'meta_keywords': settings.META_KEYWORDS,
            'meta_description': settings.META_DESCRIPTION,
            'request': request
            }


def globals(request):
    data = {}
    data.update({
        'VERSION': os.environ.get("GIT_REV", ""),  # available on every Dokku deployment
        'GA_TRACKER_ID': settings.GA_TRACKER_ID,
    })

    return data
