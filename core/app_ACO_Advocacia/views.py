from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from .models import ContactPerson
from .forms import FormContact


# Create your views here.
def index(request):
    if request.method == 'GET':
        form = FormContact()

        context = {
            'method': 'GET',
            'form': form,
        }
        return render(request, 'navigation/index.html', context)

    elif request.method == 'POST':

        form = FormContact(request.POST)
        context = {
            'method': 'POST',
            'form': form,
        }
        if form.is_valid():
            form.save()
            contact_form(request)
            return redirect('navigation/index.html', context)
        else:
            context = {
                'form': form,
            }
        return render(request, 'navigation/index.html', context)
    return render(request, 'navigation/index.html')


def agency(request):
    return render(request, 'navigation/agency.html')


def solutions(request):
    return render(request, 'navigation/solutions.html')


def politics(request):
    return render(request, 'navigation/politics.html')


def contact(request):
    if request.method == 'GET':
        form = FormContact
        context = {
            'method': 'GET',
            'form': form,
        }
        return render(request, 'e-mail_page/contact_form_page.html', context)
    elif request.method == 'POST':
        form = FormContact(request.POST)
        # context = {
        #     'method': 'POST',
        #     'form': form,
        # }
        if form.is_valid():
            form.save()
            data_contact = ContactPerson.objects.latest('id')
            context_mail = {
                'method': 'POST',
                'data_contact': data_contact,
            }
            return render(request, 'e-mail_page/thanks_page.html', context_mail)
    from_mail = settings.EMAIL_HOST_USER
    data_contact = ContactPerson.objects.latest('id')
    context_mail = {
        'method': 'POST',
        'data_contact': data_contact,
    }
    subject_mail = data_contact.subject
    to_mail = [data_contact.email, ]
    html_content = render_to_string('e-mail_page/thanks_page.html', context_mail)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject_mail,
                                   text_content, from_mail,
                                   [to_mail])
    email.send()
    return render(request, 'navigation/contact.html')


def contact_form(request):
    form = FormContact(request.POST)
    if form.is_valid():
        form.save()
        from_mail = settings.EMAIL_HOST_USER
        data_contact = isinstance(form)
        # data_contact
        context_mail = {
            'method': 'POST',
            'data_contact': data_contact,
        }
        subject_mail = data_contact.subject
        to_mail = [data_contact.email, ]
        html_content = render_to_string('e-mail_page/thanks_page.html', context_mail)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(subject_mail,
                                       text_content, from_mail,
                                       [to_mail])
        email.attach_alternative(html_content, 'text/html')
        email.send()
        return render(request, 'e-mail_page/thanks_page.html', context_mail)


def layoutp(request):
    #     if request.method == 'GET':
    #         form = FormContact
    #         context = {
    #             'method': 'GET',
    #             'form': form,
    #         }
    #         return render(request, 'e-mail_page/contact_form_page.html', context)
    #     elif request.method == 'POST':
    #         form = FormContact(request.POST)
    #         context = {
    #             'method': 'POST',
    #             'form': form,
    #         }
    #         if form.is_valid():
    #             form.save()
    #         # from_mail = settings.EMAIL_HOST_USER
    #         # text_contact = ContactPerson.objects.latest('id')
    #         # context_mail = {
    #         #     'method': 'POST',
    #         #     'text_contact': text_contact,
    #         #     }
    #         # subject_mail = text_contact.subject
    #         # to_mail = [text_contact.email, ]
    #         # html_content = render_to_string('email-user.html', context_mail)
    #         # text_content = strip_tags(html_content)
    #         # email = EmailMultiAlternatives(subject_mail,
    #         #                                text_content, from_mail,
    #         #                                [to_mail])
    #         # email.attach_alternative(html_content, 'text/html')
    #         # email.send()
    #         return render(request, 'e-mail_page/thanks_page.html', context)
    pass
