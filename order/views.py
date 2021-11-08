from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, resolve_url, reverse,redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Order
from .forms import UserOrderModelForm, AdminOrderModelForm

# Create your views here.

class OrderCreateView(LoginRequiredMixin, CreateView):
    
    def get(self, request, *args, **kwargs):
        if request.user.role == 0:
            form = UserOrderModelForm()
        else:
            form = AdminOrderModelForm()
        return render(request, 'order/order_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        if request.user.role == 0:
            form = UserOrderModelForm(request.POST)
            form.instance.user = request.user
            if form.is_valid():
                form.save()
                return redirect('order:order_list')
        else:
            form = AdminOrderModelForm(request.POST)
            if form.is_valid():
                order = form.save()
                return redirect('order:order_list', 
                    # message=f'Order id-{order.pk} created successfully.'
                    )
        return render(request, 'order/order_create.html')


class OrderList(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order_list.html'

    def get_queryset(self):
        if self.request.user.role == 0:
            return Order.objects.filter(user=self.request.user)
        else:
            return Order.objects.all()


class OrderDetailView(UserPassesTestMixin, DetailView):
    model = Order
    template_name = 'order/order_details.html'

    def test_func(self):
        return self.request.user == self.get_object().user

class OrderUpdateView(UserPassesTestMixin, UpdateView):
    model = Order
    template_name = 'order/order_update.html'
    fields = '__all__'

    def test_func(self):
        return self.request.user.role == 1

    def get_success_url(self):
        return reverse('order:order_detail', kwargs={'pk': self.object.pk})

class OrderDeleteView(UserPassesTestMixin, DeleteView):
    model = Order
    template_name = 'order/order_confirm_delete.html'

    def test_func(self):
        return self.request.user.role == 1

    def get_success_url(self):
        return reverse('order:admin_order_list')
