from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from autos.models import Auto, Make
# from autos.forms import MakeForm


# Create your views here.

#this is autos view/home page view with list of autos and make link
class MainView(LoginRequiredMixin, View):
	def get(self, request):
		mc = Make.objects.all().count()
		al = Auto.objects.all()

		ctx = {'make_count':mc, 'auto_list':al}
		return render(request, 'autos/auto_list.html', ctx)

#this is make view when you click make in home page of autos view
class MakeView(LoginRequiredMixin, View):
	def get(self, request):
	    ml = Make.objects.all()
	    ctx = {'make_list': ml}
	    return render(request, 'autos/make_list.html', ctx)

# #We use reverse_lazy() because we are in "constructor attribute" code
# #that is run before urls.py is completely loaded
# #this is hard-coded version of "Make"
# class MakeCreate(LoginRequiredMixin, View):
#     template = 'autos/make_form.html'
#     success_url = reverse_lazy('autos:all')

#     def get(self, request):
#         form = MakeForm()
#         ctx = {'form': from}
#         return render(request, self.template, ctx)

#     def post(self, request):
#         form = MakeForm(request.POST)
#         if not form.is_valid():
#             ctx = {'form': form}
#             return render(request, self.template, ctx)

#         make = form.save()
#         return redirect(self.success_url)


# # MakeUpdate has code to implement the get/post/validate/store flow
# # AutoUpdate (below) is doing the same thing with no code
# # and no form by extending UpdateView
# #this is to edit form for "Make"
# class MakeUpdate(LoginRequiredMixin, View):
#     model = Make
#     success_url = reverse_lazy('autos:all')
#     template = 'autos/make_form.html'

#     def get(self, request, pk):
#         make = get_object_or_404(self.model, pk=pk)
#         form = MakeForm(instance=make)
#         ctx = {'form': from}
#         return render(request, self.template, ctx)

#     def post(self, request, pk):
#         make = get_object_or_404(self.model, pk=pk)
#         form = MakeForm(request.POST, instance=make)
#         if not form.is_valid():
#             ctx = {"form":form}
#             return render(request, self.template, ctx)

#         form.save()
#         return redirect(self.success_url)


# #this is to delete the form for "Make"
# class MakeDelete(LoginRequiredMixin, View)
#     model = Make
#     success_url = reverse_lazy('autos:all')
#     template = 'autos/make_confirm_delete.html'

#     def get(self, request, pk):
#         make = get_object_or_404(self.model, pk=pk)
#         form = MakeForm(instance=make)
#         ctx = {'make': make}
#         return render(request, self.template, ctx)

#     def post(self, request, pk):
#         make = get_object_or_404(self.model, pk=pk)
#         make.delete()
#         return redirect(self.success_url)

#this is easier way to write "make"
class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    field = '__all__'
    success_url = reverse_lazy('autos:all')

#Take the easy way out on the main table
#These views do not need a form because CreateView, etc.
#Build a form object dynamically based on the fields
#value in the constructor attributes
#this is the easier way to create "Auto"
class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
