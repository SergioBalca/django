from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def herencia(request):
    """ render takes three arguments
            1. request
            2. template to render
            3. context. In this case is an empty dictionary.
    """
    return render(request, 'herencia.html', {})

def ejemplo(request):
    return render(request, 'ejemplo.html', {})

def otra(request):
    return render(request, 'otra.html', {})