from django.urls import path
from . import views
urlpatterns = [
    path('',views.login),
    path("Signup.html",views.signup,name="signup"),
    path("Login.html",views.login,name="login"),
    path("ReadJson.html",views.read,name="read")
    #path('admin/', admin.site.urls),
]
