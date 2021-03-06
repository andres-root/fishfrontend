
from django.shortcuts import render
from django.http import JsonResponse
from .classifier import Classifier
from .models import Fish


def index(request):
    context = {}
    return render(request, 'www/index.html', context)


def api(request):
    context = {}
    if request.method == 'GET':
        size = request.GET.get('size')
        color = request.GET.get('color')
        fish = Classifier()
        fish_name = fish.classify([size, color])
        context['fish'] = fish_name
        fish_object = Fish(name=fish_name, color=color, size=size)
        fish_object.save()

    return JsonResponse(context, safe=False)
