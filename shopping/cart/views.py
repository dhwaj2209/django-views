from django.http import HttpResponse
from django.shortcuts import render
import datetime
from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from .models import CartModel


def dtl_view(request):
  template = loader.get_template('dtl_view.html')
  context = {
    'today':  datetime.datetime.now().date(),
    'lst': []
  }
  return HttpResponse(template.render(context, request))

def center_view(request):
    return render(request, 'layout/center-area.html')

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def item_detail(request, item_id):
    item = CartModel.objects.get(id=item_id)
    context = {'data': item }
    return render(request, "item_details.html", context)

def item_create(request):
    CartModel.objects.create(title="Chess", description="Sports")
    new_item_id = 5  
    return redirect(reverse('item_detail', kwargs={'item_id': new_item_id}))

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