from django.shortcuts import render

# Create your views here.


def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')

def server_list_view(request):
    return render(request, 'dashboard/server_list.html')

def client_list_view(request):
    return render(request, 'dashboard/client_list.html')