# D:\Django\Corelytix\dashboard\views.py

from django.shortcuts import render

# डैशबोर्ड पेज दिखाने के लिए
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')

# सर्वर लिस्ट पेज दिखाने के लिए
def server_list_view(request):
    return render(request, 'dashboard/server_list.html')

# क्लाइंट लिस्ट पेज दिखाने के लिए
def client_list_view(request):
    return render(request, 'dashboard/client_list.html')