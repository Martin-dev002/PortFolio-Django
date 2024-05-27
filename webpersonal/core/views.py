from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web Personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/"> Acerca de</a></li>
    <li><a href="/portafolio/"> Portafolio</a></li>
    <li><a href="/contactos/"> Contacto</a></li>
</ul>
"""

# Create your views here.

def home (request):
    return render(request, "core/home.html")
    
def about (request):
    return render(request, "core/about.html")

def contactos (request):
    return render(request, "core/contact.html")
    



'''def home (request):
    return HttpResponse("<h1>Mi web Personal</h1><h2>Portada</h2>")
'''

'''def home (request):
    html_response = "<h1>Mi web Personal</h1>"
    for i in range(10):
        html_response += "<h2>Portada</h2>"
    return HttpResponse(html_response)'''