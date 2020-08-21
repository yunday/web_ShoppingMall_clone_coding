from django.shortcuts import render
from django.views import generic
from .models import ClothesTb

# Create your views here.
class Shop_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'shop_list/shop_list.html'
        shop_list = ClothesTb.objects.all()
        return render(request, template_name, {"shop_list": shop_list})