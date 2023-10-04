from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from main.models import Product
from main.forms import ProductForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    jumlah_product = len(products)  #untuk mengetahui jumlah product si user.

    context = {
        'name': request.user.username, # Nama kamu
        'class': 'PBP C', # Kelas PBP kamu
        'jumlah_item': jumlah_product,
        'products': products,
        'last_login': request.COOKIES.get('last_login'),
    }

    return render(request, "main.html", context)


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_one(request, product_id=None):
    if request.method == 'POST':
        # Tambah jumlah stok produk sebanyak 1
        product_id = request.POST.get('product_id')  # untuk dapat id product yang sesuai tombol
        product = Product.objects.get(id=product_id) #untuk dapat product

        product.amount += 1
        product.save()
        return redirect('main:show_main')
    
    return render(request, 'main.html')

def dec_one(request, product_id=None):
    if request.method == 'POST':
        # Tambah jumlah stok produk sebanyak 1
        product_id = request.POST.get('product_id')  # untuk dapat id product yang sesuai tombol
        product = Product.objects.get(id=product_id) #untuk dapat product

        if product.amount > 0:
            product.amount -= 1
            product.save()
        return redirect('main:show_main')
    
    return render(request, 'main.html')

def delete_product(request, product_id=None):
    if request.method == 'POST':
        #hapus product
        product_id = request.POST.get('product_id')  # untuk dapat id product yang sesuai tombol
        product = Product.objects.get(id=product_id) #untuk dapat product
        product.delete()    #otomatis hapus product
        return redirect('main:show_main')
    
    return render(request, 'main.html')

def edit_product(request, id):
    # Get product berdasarkan ID
    product = Product.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

