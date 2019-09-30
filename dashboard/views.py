from django.shortcuts import render, get_object_or_404


def dashboard(request):
    return render(request, "dashboard.html")


def error_404(request):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')
