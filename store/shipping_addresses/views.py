from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import ListView

from .forms import ShippingAddressForm

from .models import ShippingAdrress


class ShippingAddressListView( LoginRequiredMixin, ListView):
    login_url = 'login'
    model = ShippingAdrress
    template_name = 'shipping_addresses/shipping_addresses.html'

    def get_queryset(self):
        return ShippingAdrress.objects.filter(user=self.request.user).order_by('-default')

@login_required(login_url='login')
def create(request):
    form = ShippingAddressForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        shipping_address = form.save(commit=False)
        shipping_address.user = request.user
        shipping_address.default = not ShippingAdrress.objects.filter(user=request.user).exists()

        shipping_address.save()

        messages.success(request, 'address created successfully')
        return redirect('shipping_addresses:shipping_addresses')

    return render(request, 'shipping_addresses/create.html', {
        'form': form 
    })