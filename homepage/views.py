from django.shortcuts import render

def home(request):
    """The view for the start page. Renders the index.html
    page which also extends the base.html
    """
    return render(request, 'index.html')

def inner_page(request):
    """The view for the inner page. Renders the inner-page.html
    page which also extends the base.html
    """
    return render(request, 'inner-page.html')