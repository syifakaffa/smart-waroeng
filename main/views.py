from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app' : 'Smart Waroeng',
        'name': 'Syifa Kaffa Billah',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
