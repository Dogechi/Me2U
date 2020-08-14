from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib import admin

app_name = 'me2ushop'

urlpatterns = [

    url(r'^$', views.HomeView.as_view(), name='home'),
    # url(r'^seller/<str:username>', views.SellerView.as_view(), name='seller_page'),
    url('seller/(?P<id>[-\w]+)/$', views.SellerView.as_view(), name='seller_page'),

    url(r'^add_cart/(?P<slug>[\w-]+)/$', views.add_cart, name='add_cart'),
    url(r'^remove_cart/(?P<slug>[\w-]+)/$', views.remove_cart, name='remove_cart'),
    url(r'^remove_single_item_cart/(?P<slug>[\w-]+)/$', views.remove_single_item_cart, name='remove_single_item_cart'),


    url(r'^product/(?P<slug>[\w-]+)/$', views.ProductDetailedView.as_view(), name='product'),
    url('new/', views.ProductCreateView.as_view(), name='product-create'),

    url(r'^product/(?P<slug>[\w-]+)/update$', views.ProductUpdateView.as_view(), name='product-update'),
    url(r'^product/(?P<slug>[\w-]+)/delete$', views.ProductDeleteView.as_view(), name='product-delete'),

    url(r"^product-images/(?P<slug>[\w-]+)/$", views.show_product_image, name="product_images", ),
    url(r'^product-images/(?P<slug>[\w-]+)/create$', views.ProductImageCreateView.as_view(), name='product_image_create'),
    url("^image-(?P<pk>[\w-]+)/update/$", views.ProductImageUpdateView.as_view(), name="product_image_update"),
    url('^image-(?P<pk>[\w-]+)/delete/$', views.ProductImageDeleteView.as_view(), name="product_image_delete"),

    url(r'^order_summary/', views.Order_summary_view.as_view(), name='order_summary'),
    url(r'^order_dashboard/', views.OrderView.as_view(), name='order_dashboard'),
    url(r'^address_select/', views.AddressSelectionView.as_view(), name='address_select'),

    url(r'^checkout/', views.Checkout_page.as_view(), {'SSL': True}, name='checkout'),
    url(r'^add_coupon/', views.add_coupon, name='add_coupon'),

    url(r'payment/(?P<payment_option>[\w-]+)/$', views.PaymentView.as_view(), {'SSL': True}, name='payment'),
    url('request_refund/', views.RefundView.as_view(), name='request_refund'),
    url('add/review', views.add_review),
    url('add/tag', views.add_tag),
    url('tag/(?P<tag>[\w-]+)/$', views.tag),
    url('tag_cloud', views.tag_cloud, name='tag_cloud'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
