from django.shortcuts import render, redirect
from django.http import HttpResponse
from noivos.models import Convidados,Presentes

# Create your views here.

def convidados(request):
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)
    presentes = Presentes.objects.filter(reservado=False).order_by('-importancia')
    return render(request, 'convidados.html', {'convidado': convidado, 'presentes': presentes})


from django.shortcuts import render, redirect
from django.http import HttpResponse
from noivos.models import Convidados

def responder_presenca(request):
    resposta = request.GET.get('resposta')
    token = request.GET.get('token')

    # Verifique se o token foi fornecido
    if not token:
        return HttpResponse("Token não fornecido", status=400)

    try:
        # Tente buscar o convidado com o token fornecido
        convidado = Convidados.objects.get(token=token)
    except Convidados.DoesNotExist:
        # Se não encontrar o convidado, retorne uma mensagem de erro
        return HttpResponse("Convidado não encontrado", status=404)

    # Verifique se a resposta é válida
    if resposta not in ['C', 'R']:
        return redirect(f'/convidados/?token={token}')

    # Atualize o status do convidado
    convidado.status = resposta
    convidado.save()

    return redirect(f'/convidados/?token={token}')

