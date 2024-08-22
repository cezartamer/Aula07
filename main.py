from etl import ler_csv, filtrar_produtos_por_entrega, somar_valores_dos_produtos

path_arquivo = "vendas.csv"
entregue = False
csv_lido = ler_csv(path_arquivo)
produtos_filtrados = filtrar_produtos_por_entrega(csv_lido, entregue)
print(somar_valores_dos_produtos(produtos_filtrados))
