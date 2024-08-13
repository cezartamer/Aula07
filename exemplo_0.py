# def soma(numero1:int, numero2:int)->int:
#     """
#     Uma função de somar inteiros
#     """
#     return numero1+numero2

# print(soma(1,2))


def calcular_media(valor: list) -> float:
    media = sum(valor)/len(valor)
    return media



lista = [1,6,7.8,9,4.5]
print(calcular_media(lista))