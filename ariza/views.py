
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404

from .models import Application, Qabul

class ApplicationListView(ListView):
    model = Application
    template_name = 'ariza/application.html'


class ApplicationDetailView(DetailView):
    model = Application
    template_name = 'ariza/application_detail.html'
    context_object_name = 'application'
    

# class ApplicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Application
#     fields = ('title','summary', 'body','photo',)
#     template_name = 'ariza/application_edit.html'

#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user

# class ApplicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Application
#     template_name = 'ariza/application_delete.html'
#     success_url = reverse_lazy('yangiliklar')

#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user

class ApplicationCreateView(CreateView):
    model = Application
    template_name = 'ariza/application_new.html'
    fields = ('Ismi', 'email', 'telfon_raqami', 'lavozimi', 'body',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser
    def get_success_url(self):
        return reverse_lazy('application_detail', args=[str(self.object.id)])
    

class QabulDetailView(DetailView):
    model = Qabul
    template_name = 'ariza/qabul_detail.html'

class QabulCreateView(CreateView):
    model = Qabul
    template_name = 'ariza/qabul_new.html'
    fields = ('javob', 'status')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def form_valid(self, form):
        form.instance.PK = get_object_or_404(Application, pk=self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('application_detail', kwargs={'pk': self.kwargs['pk']})
