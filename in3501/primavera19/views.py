from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'home.html')

def inputs(request):
	return render(request, 'inputs.html')


def recuperar(request):
	texto=request.POST["inputText"]
	texto_largo=request.POST["textA"]
	diccionario={}
	diccionario["comentario"]=texto
	diccionario["comentario2"]=texto_largo
	return render(request, "mostrar_resultado.html", diccionario)
