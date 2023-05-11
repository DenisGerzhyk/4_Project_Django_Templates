from django.shortcuts import render, redirect
from .models import Calculates
from .forms import CalculatesForm


def index(request):
    if request.method == "POST":
        form = CalculatesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('display')
    else:
        form = CalculatesForm()
    context = {'form': form}
    return render(request, 'index.html', context)


def display(request):
    form = Calculates.objects.all()
    for calc in form:
        if calc.sign == '+':
            calc.result = calc.x + calc.y
        elif calc.sign == '-':
            calc.result = calc.x - calc.y
        elif calc.sign == '*':
            calc.result = calc.x * calc.y
        elif calc.sign == '/':
            calc.result = calc.x / calc.y
    context = {'form': form}
    return render(request, 'display.html', context)
