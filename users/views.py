from typing import Any
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterPage(FormView):
   template_name = 'users/register.html'
   form_class = UserCreationForm
   redirect_authenticated_user = True
   success_url = reverse_lazy('tasks')

   def form_valid(self, form):
      user = form.save()
      if user is not None:
         login(self.request, user)
      return super(RegisterPage, self).form_valid(form)
   
   def get(self, *args, **kwargs):
      if self.request.user.is_authenticated:
         return redirect('task')
      return super(RegisterPage, self).get(*args, **kwargs)
   
class CustomLoginView(LoginView):
   template_name = 'users/login.html'
   fields = '__all__'
   redirect_authenticated_user = True
   
   def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, 'Please login to username: admin, password: admin123 for demo, or register to create new user.')
            print("message added")
        return super().get(request, *args, **kwargs)

   def get_success_url(self):
      return reverse_lazy('tasks')

class ProfileUpdateForm(forms.ModelForm):
   class Meta:
      model = Profile
      fields = ['image']

class ProfileUpdateView(LoginRequiredMixin, FormView):
   form_class = ProfileUpdateForm
   success_url = reverse_lazy('profile')
   template_name = 'users/profile.html'
   
   def form_valid(self, form):
      form.save()
      
      return super().form_valid(form)
   
   def get_form_kwargs(self):
      kwargs = super().get_form_kwargs()
      if self.request.method == 'POST':
         kwargs.update({
            'instance': self.request.user.profile,
            'files': self.request.FILES,
         })
      else:
         kwargs.update({
            'instance': self.request.user.profile,
         })
      
      return kwargs
   
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['p_form'] = self.get_form()
      
      return context
   
@login_required
def profile(request):
   return render(request, 'users/profile.html')