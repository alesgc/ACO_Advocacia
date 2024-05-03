from django.shortcuts import render, redirect
from app_ACO_Advocacia.forms import FormContact

# Create your views here.
def index(request):
   if request.method == 'GET':
      form = FormContact()

      context = {
         'form': form,
      }
      return render(request, 'navigation/index.html', context)

   elif request.method == 'POST':

      form = FormContact(request.POST)

      if form.is_valid():
         form.save()
         return redirect('navigation/index.html')
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
      form = FormContact()

      context = {
         'form': form,
      }
      return render(request, 'navigation/contact.html', context)

   elif request.method == 'POST':

      form = FormContact(request.POST)

      if form.is_valid():
         form.save()
         return redirect('navigation/contact.html')
      else:
         context = {
            'form': form,
         }
      return render(request, 'navigation/contact.html', context)

def layoutp(request):
   if request.method == 'GET':
      form = FormContact()

      context = {
         'form': form,
      }
      return render(request, 'navigation/layoutp.html', context)

   elif request.method == 'POST':

      form = FormContact(request.POST)

      if form.is_valid():
         form.save()
         return redirect('navigation/layoutp.html')
      else:
         context = {
            'form': form,
         }
      return render(request, 'navigation/layoutp.html', context)
   return render(request, 'navigation/layoutp.html')