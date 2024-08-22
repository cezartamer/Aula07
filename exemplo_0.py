from typing import List

# def soma(numero1:int, numero2:int)->int:
#     """
#     Uma função de somar inteiros
#     """
#     return numero1+numero2

# print(soma(1,2))


# def calcular_media(valor: list) -> float:
#     media = sum(valor)/len(valor)
#     return media



# lista = [1,6,7.8,9,4.5]
# print(calcular_media(lista))

##Contar valores únicos em uma lista

# lista: list = [1,2,3,4,5,6,7,8,5,4,9,9,4,6,8]

# def contar_valores_unicos(lista:list) -> list:
#     return len(set(lista))


# print(contar_valores_unicos(lista))

##Filtrar resultado acima de um limite

# lista: List[int] = [1,2,3,4,5,6,7,8,5,4,9,9,4,6,8]

# limite:int = 5

# def filtrar_resultado_acima_de_um_limite(valores: List[int], limite: int) -> List[int]:
#     """
#     Função para filtrar resultados acima de um limite
#     """
#     valores_resultado: List[int] = []
#     for i in valores:
#         if i > limite:
#             valores_resultado.append(i)
#     return valores_resultado

# print(filtrar_resultado_acima_de_um_limite(lista, limite))


## Converter graus Celcius para Fahrenheit

# graus_celcius: List[float] = [33.6,40.3,20.5,22.6,16]

# def converter_graus_celcius_para_fahrenheit(graus_celcius: List[float]) -> List[float]:
#     resultado: List[float] = list()
#     for i in graus_celcius:
#         resultado.append(i*1.8+32)
#     return resultado

# #if __name__ == "exemplo_0":
# print(converter_graus_celcius_para_fahrenheit(graus_celcius))



##Calcular o Desvio padrao

# lista_de_valores: List[float] = [1,2,5,10,70,1.5,7,4.8,55.7,39.1,16,-10]

# def calcular_desvio_padrao1(valores: List[float]) -> float:
#     n = len(lista_de_valores)
#     media_aritimetica = sum(lista_de_valores)/ n
#     aux:List[float] = []

#     for x in lista_de_valores:
#         aux.append((x - media_aritimetica)**2)

#     variavel:float = (sum(aux)/n) ** 0.5
    
#     return variavel




# def calcular_desvio_padrao2(valores: List[float]) -> float:
#     media = sum(valores) / len(valores)
#     variancia = sum((x - media) ** 2 for x in valores) / len(valores)
#     return variancia ** 0.5

# print(f"O desvio padrão é: {calcular_desvio_padrao1(lista_de_valores)}")
# print(f"O desvio padrão é: {calcular_desvio_padrao2(lista_de_valores)}")


##Encontrar Valores Ausentes em uma Sequência
def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))


print(encontrar_valores_ausentes([1,4,7,8]))