from django.views.generic import ListView, DetailView

from .models import Cheese


class CheeseListView(ListView):
    model = Cheese

    def get_queryset(self):
        return Cheese.objects.filter(firmness=Cheese.Firmness.SEMI_HARD)


class CheeseDetailView(DetailView):
    model = Cheese

