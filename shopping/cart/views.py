from django.http import HttpResponse
from django.shortcuts import render
import datetime
from django.views.generic.list import ListView

from .models import CartModel

def index(request):
    #return HttpResponse("Hi, Django")
    context ={}
    context["item_model"] = CartModel.objects.all()
    return render(request, "list_view.html", context)


def date_view(request):
    now = datetime.datetime.now()
    html_code = '<html lang="en"><body>Current time is: %s.</body></html>' % now
    return HttpResponse(html_code)

class cart_list(ListView):
    model = CartModel
    template_name = 'cartmodel_list.html'