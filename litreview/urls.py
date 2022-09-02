from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
import flux.views
from user.views import signup
import user.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/', flux.views.home, name='home'),
    path('', LoginView.as_view(
        template_name='user/login.html',
        redirect_authenticated_user=True),
        name='login'),
    path("logout", user.views.logout_user, name="logout"),
    path('signup/', authentication.views.signup_page, name='signup'),
]
