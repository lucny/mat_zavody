from django.shortcuts import render

# Create your views here.
from .models import Cyklista


def index(request):
    context = {
        'nadpis': 'BikeWeb',
        'cykliste': Cyklista.objects.order_by('-narozeni')[:4]
    }
    return render(request, 'index.html', context=context)