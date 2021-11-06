from django.shortcuts import render


def home(request):
    template = "home.html"
    return render(request, template)


def customer_page(request):
    template = "customer.html"
    return render(request, template)


def courier_page(request):
    template = "courier.html"
    return render(request, template)
