from django.urls import path
from ecommerceapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from ecommerceapp.forms import LogInForm, MyPasswordRestForm, MySetPasswordForm, MyPasswordChangeForm
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # PROJECT URLS
    path('', views.Home, name='home'), 
    path('laptop/', views.Laptop, name='laptop'), 
    path('laptop/<slug:data>', views.Laptop, name='laptop'), 
    path('mobile/', views.Mobile, name='mobile'), 
    path('mobile/<slug:data>', views.Mobile, name='mobile'), 
    path('topwear/', views.Topwear, name='topwear'), 
    path('topwear/<slug:data>', views.Topwear, name='topwear'), 
    path('bottomwear/', views.Bottomwear, name='bottomwear'), 
    path('bottomwear/<slug:data>', views.Bottomwear, name='bottomwear'), 
    path('productdetails/<int:id>', views.Productdetails, name='productdetails'), 
    path('profile/', views.Profile.as_view(), name='profile'), 
    path('showaddress/', views.Address, name='showaddress'), 
    path('showcart/', views.Showcart, name='showcart'),
    path('pluscart/', views.Pluscart, name='pluscart'), # type: ignore
    path('minuscart/', views.Minuscart, name='minuscart'), # type: ignore
    path('removecart/', views.Removecart, name='removecart'), # type: ignore
    path('addtocart/<int:id>/', views.Addtocart, name='addtocart'), 
    path('checkout/', views.Checkout, name='checkout'),  # type: ignore
    path('buynow/<int:id>', views.Buynow, name='buynow'), 
    path('paymentdone/', views.Paymentdone, name='paymentdone'), 
    path('orders/', views.Orders, name='orders'), 

    # AUTH URLS
    path('login/', auth_views.LoginView.as_view(template_name="ecommerceapp/login.html", authentication_form = LogInForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = "/"), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('password_change/', login_required(auth_views.PasswordChangeView.as_view(template_name="ecommerceapp/passwordchange.html", form_class=MyPasswordChangeForm)), name='password_change'),
    path('password_change_done/', login_required(auth_views.PasswordChangeDoneView.as_view(template_name="ecommerceapp/passwordchangedone.html")), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="ecommerceapp/passwordreset.html", form_class=MyPasswordRestForm, email_template_name='ecommerceapp/passwordresetemail.html',), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="ecommerceapp/passwordresetdone.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="ecommerceapp/passwordresetconfirm.html", form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="ecommerceapp/passwordresetcomplete.html"), name='password_reset_complete'),
         
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
