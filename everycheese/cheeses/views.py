from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView


from .models import Cheese


class CheeseListView(ListView):
    model = Cheese

    # def get_queryset(self):
    #     return Cheese.objects.filter(firmness=Cheese.Firmness.SEMI_HARD)


class CheeseDetailView(DetailView):
    model = Cheese


class CheeseCreateView(LoginRequiredMixin, CreateView):
    model = Cheese
    fields = ["name", "description", "firmness", "country_of_origin"]

