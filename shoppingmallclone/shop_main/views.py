from django.shortcuts import render
from django.views import generic

# Create your views here.
class Shop_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'shop_main/index.html'
        return render(request, template_name)