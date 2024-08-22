import csv

def ler_csv(nome_arquivo: str) -> list[dict]:
    """
    Função que le um csv e retorna uma lista de dicionario
    """
    lista = []
    with open (file=nome_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


def filtrar_produtos_por_entrega(lista: list[dict], filtro: bool) -> list[dict]:
    """
    Função que filtra os produtos entregues
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == str(filtro):
            lista_com_produtos_filtrados.append(produto)

    return lista_com_produtos_filtrados

def somar_valores_dos_produtos(lista: list[dict]) -> float:
    """
    Soma os produtos passados na lista
    """
    valor_total = 0
    for produto in lista:
        valor_total += float(produto.get("price"))
    return valor_total

