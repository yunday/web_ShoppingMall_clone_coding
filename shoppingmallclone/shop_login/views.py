from django.shortcuts import render
from .models import UserInfo

from django.views import generic

# Create your views here.
class Shop_login(generic.TemplateView)/:
    def get(self, request, *args, **kwargs):
        template_name = 'shop_login/login.html'
        user_info = UserInfo.objects.all()
        return render(request, template_name, {"user_info":user_info})
