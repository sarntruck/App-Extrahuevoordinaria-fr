from django.shortcuts import render
from .models import Contador
def contador_clicks(request):
    contador, creado = Contador.objects.get_or_create(pk=1)
    if request.method == 'POST':
        contador.value +=1
        contador.save()
        return redirect('juego.html')
    return render(request, 'juego.html', {'contador:', contador})
# Create your views here.
