from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Breed,Cat

#this is cats home page view with list of cats
class MainView(LoginRequiredMixin, View):
    def get(self, request):
        breed_count = Breed.objects.all().count()
        cat_list = Cat.objects.all()

        context = {'breed_count':breed_count, 'cat_list':cat_list}
        return render(request, 'cats/cat_list.html', context)

#this is breed page view when you click "view breeds"
class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        breed_list = Breed.objects.all()
        context = {'breed_list': breed_list}
        return render(request,'cats/breed_list.html', context)


#Cat list "create, delete and update view"
class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy('cats:all')


#breed list "create, delete and update view"
class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

