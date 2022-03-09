from cProfile import label
from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from datetime import datetime
from passagens.classe_viagem import tipo_de_classe
from passagens.validation import *
from passagens.models import Passagem, ClasseViagem, Pessoa

class PassagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data da Pesquisa', disabled=True, initial=datetime.today())
    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {
            'data_ida': 'Data de ida',
            'data_volta': 'Data de volta',
            'informacoes': 'Informações',
            'classe_viagem': 'Classe do vôo'
        }
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker()
        }
    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_de_erros = {}
        verifica_campo_iguais(origem, destino, lista_de_erros)
        verifica_campo_numerico(origem, 'origem', lista_de_erros)
        verifica_campo_numerico(destino, 'destino', lista_de_erros)
        data_ida_maior_data_volta(data_ida, data_volta, lista_de_erros)
        data_ida_menor_data_compra(data_ida, data_pesquisa, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data

class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']
        