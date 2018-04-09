from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Jela
from .forms import UserForm


class IndexView(generic.ListView):  # pocetna
    template_name = 'recepti/index.html'

    def get_queryset(self):
        return Jela.objects.all()

    def param(self, request):
        message = request.GET.get('tags', '')
        return message


class ReceptiView(generic.ListView):  # recepti koje mozete napraviti sa vasim sastojcima
    context_object_name = 'sva_jela'
    template_name = 'recepti/recepti.html'

    def get_queryset(self):
        return Jela.objects.all()


class DetailView(generic.DetailView):  # detalji recepta
    context_object_name = 'jelo'
    model = Jela
    template_name = 'recepti/detail.html'


class UserFormView(View):
    form_class = UserForm
    template_name = 'recepti/registration_form.html'

    def get(self, request):  # display blank form
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):  # process form data
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User objects if credentials are correct

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form})
