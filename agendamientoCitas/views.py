from django.shortcuts import render

def render_citas(request):
    return render(request, 'citas.html')
