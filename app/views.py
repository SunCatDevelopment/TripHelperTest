from django.shortcuts import render, get_object_or_404
from .models import Place

def place(request):
    places = Place.objects.filter().order_by('visit_date')
    return render(request, 'places.html', {'places': places})

def detail(request, pk):
    plac = get_object_or_404(Place, pk=pk)
    return render(request, 'detail.html', {'place': plac})