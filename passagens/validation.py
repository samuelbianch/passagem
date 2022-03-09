def verifica_campo_numerico(valor_campo, nome_campo, lista_de_erros):
    """Verifica a existência de números no input"""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números neste campo'

def verifica_campo_iguais(origem, destino, lista_de_erros):
    """Verifica se os campos são iguais"""
    if origem == destino:
        lista_de_erros[destino] = 'Destino e origem não podem ser iguais'

def data_ida_maior_data_volta(data_ida, data_volta, lista_de_erros):
    """Verifica se a data de ida é maior que a data da volta"""
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de volta não pode ser menor que a data de ida'

def data_ida_menor_data_compra(data_ida, today, lista_de_erros):
    """Verifica se a data da passagem de ida não é de um dia anterior"""
    if data_ida < today:
        lista_de_erros['data_ida'] = 'A data de ida não pode ser menor do que o dia atual da compra'
