from django.shortcuts import render, redirect
from django.conf import settings

def protected_view(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'protected_page.html')
