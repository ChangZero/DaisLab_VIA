from django.shortcuts import render

# Create your views here.


def page_not_found(request, exception):
    '''
    404 Page not found
    '''
    return render(request, 'users/404.html', {})
