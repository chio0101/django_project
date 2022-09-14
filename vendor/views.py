from django.shortcuts import render
from .models import Vendor
# from .forms import VendorForm
from .forms import RawVendorForm
# from django.http import Http404
from django.shortcuts import get_list_or_404 

# Create your views here.
def vendor_index(request):
    vendor_list = Vendor.objects.all() # 把所有 Vendor 的資料取出來
    context = {'vendor_list': vendor_list} # 建立 Dict對應到Vendor的資料，
    return render(request, 'vendors/vendor_index.html', context)

# 針對 vendor_create.html
def vendor_create_view(request):
    # form = VendorForm(request.POST or None)
    form = RawVendorForm(request.POST or None)
    if form.is_valid():
        # form.save()
        # form = VendorForm() # 清空 form
        Vendor.objects.create(**form.cleaned_data)
        form = RawVendorForm()

    context = {
        'form' : form
    }
    return render(request, "vendors/vendor_create.html", context)

def singleVendor(request, id):
    vendor_list = get_list_or_404 (Vendor, id=id)
    # try:
    #     vendor_list = Vendor.objects.get(id=id)
    # except Vendor.DoesNotExist:
    #     raise Http404
    context = {
        'vendor_list': vendor_list
    }
    return render(request, 'vendors/vendor_detail.html', context)