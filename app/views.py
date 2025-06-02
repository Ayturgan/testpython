from django.shortcuts import render

def notifications_test(request):
    return render(request, 'app/notifications_test.html')