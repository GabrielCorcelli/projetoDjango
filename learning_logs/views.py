from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """Página principal do learning_log"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Mostra todos os assuntos"""
    topic = Topic.objects.order_by('date_added')