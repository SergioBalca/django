from django.shortcuts import render

def simple(request):
    """ There is three arguments in render:
            1 the request
            2 the template to render
            3 context. In this case it is an empty dictionary, because we are rendering
                       an static template in this example. 
    """
    return render(request, 'simple.html', {})

def dinamico(request, name):
    categories = ['code', 'design', 'marketing']
    context = {'name': name, 'categories': categories}
    return render(request, 'dinamico.html', context)