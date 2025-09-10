from django.shortcuts import render
def click_counter(request):
    return render(request, 'counters/click_counters')
# Create your views here.
