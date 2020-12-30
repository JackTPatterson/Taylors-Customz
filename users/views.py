from django.template.loader import render_to_string, get_template
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage

from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import request, HttpResponse

from .forms import ProductCreationForm, AcceptForm, DenyForm, EmailForm, GalleryForm
from .models import Product
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from random import randint
# Create your views here.


def index(request):
    return render(request, 'users/index.html')


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

#TODO:
#!Error checking is needed to make sure there are no duplicates of orderId and orderNumber
def request(request):
    form = ProductCreationForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.orderId = random_with_N_digits(10)
            obj.orderNumber = random_with_N_digits(10)
            form.save()
            
            return redirect("index")
    else:
        form = ProductCreationForm()
    return render(request, "users/request.html", {"form": form})


class AdminListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Product
    template_name = 'users/product_list'  # <app>/<model>_<viewtype>.html
    context_object_name = 'product'
    ordering = ['-date_submitted']
    paginate_by = 20
    



def requestDetail(request, orderId):
    instance = Product.objects.get(orderId=orderId)
    return render(request, 'users/product_detail.html', {'instance': instance})


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'users/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

#!This shit dont work
def handler404(request, exception):
    data = {}
    return render(request, 'users/404.html', data)


def accept(request, orderId):
    instance = Product.objects.get(orderId=orderId)
    form = AcceptForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            price = obj.price
            message = obj.message
            Product.objects.filter(orderId=orderId).update(
                price=price,
                message=message,
                accepted=True,
                denied=False
            )
            ctx = {
                'orderNum': instance.orderNumber,
                'price': instance.price,
                'url': instance.orderId,
                'message': message
            }
            message = get_template('users/emails/accept.html').render(ctx)
            msg = EmailMessage(
                'Order Accepted',
                message,
                'jpattersonservices@gmail.com',
                ['jpattersonservices@gmail.com'],
            )
            msg.content_subtype = "html" 
            msg.send()
            redirect('list')

    context = {
        'instance': instance,
        'form': form
    }

    return render(request, 'users/accept.html', context)


def deny(request, orderId):
    instance = Product.objects.get(orderId=orderId)
    form = DenyForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            message = obj.message
            Product.objects.filter(orderId=orderId).update(
                message=message,
                accepted=False,
                denied=True
            )
            ctx = {
                'url': instance.orderId,
                'message': message
            }
            message = get_template('users/emails/deny.html').render(ctx)
            msg = EmailMessage(
                'Order Denied',
                message,
                'jpattersonservices@gmail.com',
                ['jpattersonservices@gmail.com'],
            )
            msg.content_subtype = "html"
            msg.send()
            redirect('list')

    context = {
        'instance': instance,
        'form': form
    }

    return render(request, 'users/deny.html', context)


def email(request, orderId):
    instance = Product.objects.get(orderId=orderId)
    form = EmailForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            message = obj.message
            Product.objects.filter(orderId=orderId).update(
                message=message
            )
            ctx = {
                'orderNum': instance.orderNumber,
                'url': instance.orderId,
                'message': message
            }
            message = get_template('users/emails/email.html').render(ctx)
            msg = EmailMessage(
                'Order Message',
                message,
                'jpattersonservices@gmail.com',
                ['jpattersonservices@gmail.com'],
            )
            msg.content_subtype = "html"
            msg.send()
            redirect('list')

    context = {
        'instance': instance,
        'form': form
    }

    return render(request, 'users/email.html', context)


def admin(request):
    return render(request, 'users/admin.html')

def displayDetail(request):
    return render(request, 'users/display.html')

def gallery(request):
    return render(request, 'users/gallery.html')

def delete(request, orderId):
    instance = Product.objects.get(orderId=orderId)
    instance.delete()
    redirect('list')
    return HttpResponse("Data has been deleted")

def dashboard(request):
    form = GalleryForm(request.POST)
    return render(request, 'users/admin.html')