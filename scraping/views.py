import json

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Vacancy
from .forms import FindForm, VForm


def home_view(request):
    form = FindForm()
    context = {'form': form}
    return render(request, 'scraping/home.html', context)


# def list_view(request):
#     form = FindForm()
#     city = request.GET.get('city')
#     language = request.GET.get('language')
#     context = {'city': city, 'language': language, 'form': form}
#     if city or language:
#         _filter = {}
#         if city:
#             _filter['city__slug'] = city
#         if language:
#             _filter['language__slug'] = language
#         qs = Vacancy.objects.filter(**_filter)
#         paginator = Paginator(qs, 10)  # Show 25 contacts per page.
#
#         page_number = request.GET.get("page")
#         page_obj = paginator.get_page(page_number)
#         context['objects_list'] = page_obj
#     return render(request, 'scraping/list.html', context)


def v_detail(request, pk):
    object_ = get_object_or_404(Vacancy, pk=pk)
    return render(request, 'scraping/detail.html', {'object': object_})


class VDetail(DetailView):
    queryset = Vacancy.objects.all()
    template_name = 'scraping/detail.html'
    context_object_name = 'object'


class VList(ListView):
    model = Vacancy
    template_name = 'scraping/list.html'
    form = FindForm()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city'] = self.request.GET.get('city')
        context['language'] = self.request.GET.get('language')
        context['form'] = self.form
        return context

    def get_queryset(self):
        city = self.request.GET.get('city')
        language = self.request.GET.get('language')
        qs = []
        if city or language:
            _filter = {}
            if city:
                _filter['city__slug'] = city
            if language:
                _filter['language__slug'] = language
            qs = Vacancy.objects.filter(**_filter).select_related('city', 'language')
        return qs


class VCreate(CreateView):
    model = Vacancy
    form_class = VForm
    template_name = 'scraping/create.html'
    success_url = reverse_lazy('scraping:home')


class VUpdate(UpdateView):
    model = Vacancy
    form_class = VForm
    template_name = 'scraping/create.html'
    success_url = reverse_lazy('scraping:home')


class VDelete(DeleteView):
    model = Vacancy
    template_name = 'scraping/delete.html'
    success_url = reverse_lazy('scraping:home')


def handler400(request, exception):
    return render(request, 'scraping/400.html', status=400)


def handler403(request, exception):
    return render(request, 'scraping/403.html', status=403)


def handler404(request, exception):
    return render(request, 'scraping/404.html', status=404)


def handler500(request):
    return render(request, 'scraping/500.html', status=500)