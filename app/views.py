from django.shortcuts import render, redirect
from django.db.models import Q
from django.template import RequestContext
from app.forms import SupplierForm
from app.models import Supplier
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    
    if search:
        query = Q()
        for field in Supplier._meta.fields:
            if field.get_internal_type() in ["CharField", "TextField"]:
                query |= Q(**{f"{field.name}__icontains": search})
        data['database'] = Supplier.objects.filter(query)
    else:
        all = Supplier.objects.all()
        paginator = Paginator(all, 7)
        pages = request.GET.get('page')
        data['database'] = paginator.get_page(pages)
        
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = SupplierForm()
    return render(request, 'form.html', data)

def create(request):
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['database'] = Supplier.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['database'] = Supplier.objects.get(pk=pk)
    data['form'] = SupplierForm(instance=data['database'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['database'] = Supplier.objects.get(pk=pk)
    form = SupplierForm(request.POST or None, instance=data['database'])
    if form.is_valid():
            form.save()
            return redirect('home')
    
def delete(request, pk):
     database = Supplier.objects.get(pk=pk)
     database.delete()
     return redirect('home')