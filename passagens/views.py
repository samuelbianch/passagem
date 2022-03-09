from django.shortcuts import render
from passagens.forms import PassagemForms, Pessoa, PessoaForms

def index(request):
    form = PassagemForms()
    pessoa_form = PessoaForms()

    contexto = {
        'form': form,
        'pessoa_form': pessoa_form
    }

    return render(request, 'index.html', contexto)

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        pessoa_form = PessoaForms(request.POST)
        if form.is_valid():
            dados = {
                'form': form,
                'pessoa_form': pessoa_form
            }
            return render(request, 'minha_consulta.html', dados)
        else:
            print('Formulário inválido')
            dados = {
                'form': form,
                'pessoa_form': pessoa_form
            }
            return render(request, 'index.html', dados)
