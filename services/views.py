from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import ContactClientForm


# Главная страница
def main_page(request):
    services = Services.objects.all()
    portfolio = Portfolio.objects.all()[:3]
    production = Production.objects.all()
    price = Price.objects.all()
    customer = Customer.objects.all()[:8]
    command = Staff.objects.all()
    if request.method == 'POST':
        form = ContactClientForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'Новая заявка! Armada.'
            name = form.cleaned_data['name'].title()
            phone_number = form.cleaned_data['phone']
            message = 'Имя клиента: {} \n\n Номер телефона : {}'.format(name, phone_number)
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

            context = {'name': form.cleaned_data['name']}
            return render(request, 'contact_form.html', context)
    else:
        form = ContactClientForm()
    context = {
        'services': services,
        'portfolio': portfolio,
        'production': production,
        'price': price,
        'customer': customer,
        'command': command,
        'form': form
    }
    return render(request, 'index.html', context)


# Вкладка "Услуги-категории"
def service_list(request):
    list_items = ServiceListCategory.objects.all()
    if request.method == 'POST':
        form = ContactClientForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'Новая заявка! Armada.'
            name = form.cleaned_data['name'].title()
            phone_number = form.cleaned_data['phone']
            message = 'Имя клиента: {} \n\n Номер телефона : {}'.format(name, phone_number)
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

            context = {'name': form.cleaned_data['name']}
            return render(request, 'contact_form.html', context)
    else:
        form = ContactClientForm()

    context = {'list_items': list_items,
               'form': form,
               }
    return render(request, 'service_list.html', context)


# Вкалдка "Услуги"
def service_panel(request, item_slug):
    category = get_object_or_404(ServiceListCategory, slug=item_slug)
    panel_items = ServicePanel.objects.filter(category=category)
    if request.method == 'POST':
        form = ContactClientForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'Новая заявка! Armada.'
            name = form.cleaned_data['name'].title()
            phone_number = form.cleaned_data['phone']
            message = 'Имя клиента: {} \n\n Номер телефона : {}'.format(name, phone_number)
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

            context = {'name': form.cleaned_data['name']}
            return render(request, 'contact_form.html', context)
    else:
        form = ContactClientForm()

    context = {'panel_items': panel_items,
               'form': form,
               }
    return render(request, 'service_panel.html', context)


# Вкладка "О нас"
def about_us_panel(request):
    history_carousel = Work.objects.all()
    command = Staff.objects.all()
    services = Services.objects.all()
    customer = Customer.objects.all()
    if request.method == 'POST':
        form = ContactClientForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'Новая заявка! Armada.'
            name = form.cleaned_data['name'].title()
            phone_number = form.cleaned_data['phone']
            message = 'Имя клиента: {} \n\n Номер телефона : {}'.format(name, phone_number)
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

            context = {'name': form.cleaned_data['name']}
            return render(request, 'contact_form.html', context)
    else:
        form = ContactClientForm()

    context = {'history_carousel': history_carousel,
               'command': command,
               'form': form,
               'services': services,
               'customer': customer,
               }
    return render(request, 'about-us_panel.html', context)


# Вкладка "Портфолио"
def portfolio_panel(request):
    portfolio_items = Portfolio.objects.all()

    return render(request, 'portfolio_panel.html', context={'portfolio_items': portfolio_items})


def contacts(request):
    return render(request, 'contacts_panel.html')


# Вкладка "Производство"
def production_panel(request):
    production = Production.objects.all()
    equipment_carousel = Equipment.objects.all()
    context = {
        'production': production,
        'equipment_carousel': equipment_carousel
    }
    return render(request, 'production_panel.html', context)
