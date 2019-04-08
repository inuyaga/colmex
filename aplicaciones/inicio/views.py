from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class Inicio(LoginRequiredMixin, TemplateView):
    template_name = 'admin/base_colmex.html'
    login_url = '/admincolmex/'
    redirect_field_name = 'redirect_to'