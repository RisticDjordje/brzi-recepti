from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Jela
from .forms import UserForm, DodajRecept
from django.http import HttpResponseRedirect
from django.contrib import messages

class IndexView(generic.ListView):  # pocetna
    template_name = 'recepti/index.html'

    def get_queryset(self):
        return Jela.objects.all()

    def param(self):
        tags = self.request.GET.get('tags')
        return tags


class ReceptiView(generic.ListView):  # recepti koje mozete napraviti sa vasim sastojcima
    context_object_name = 'sva_jela'
    template_name = 'recepti/recepti.html'

    def get_queryset(self):
        return Jela.objects.all()


class DetailView(generic.DetailView):  # detalji recepta
    context_object_name = 'jelo'
    model = Jela
    template_name = 'recepti/detail.html'


class DodajView(View):
    template_name = 'recepti/dodajrecept.html'
    def get(self, request):
        return render(request, self.template_name, {'form': DodajRecept()})

    def post(self, request):
        if request.method == 'POST':
            form = DodajRecept(request.POST, request.FILES)
            if form.is_valid():
                    form.save(commit=True)
                    return redirect('recepti')
            else:
                messages.error(request, form)
        return render(request, self.template_name, {'form': DodajRecept()})


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


# def pdf_generation(request):  nesto za pdf
#     html_template = get_template('recepti/<int:pk>/')
#     pdf_file = HTML(string=html_template).write_pdf()
#     response = HttpResponse(pdf_file, content_type='application/pdf')
#     response['Content-Disposition'] = 'filename="{{Jela.ime}}"'
#     return response

