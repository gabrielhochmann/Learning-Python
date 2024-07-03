import pandas as pd
from datetime import datetime, timedelta

# Lista de integrantes do laboratório
integrantes = ["Newton", "Huei e Wu", "Alexandre", "Anderson", "Weber", "Gabriel", "Angelo", "Henrique"]

# Data inicial
data_inicial = datetime.strptime("03/07/2024", "%d/%m/%Y")

# Intervalo de 7 dias
intervalo = timedelta(days=7)

# Lista para armazenar as linhas da tabela
tabela = []

# Geração das datas
for i, integrante in enumerate(integrantes):
    data_retirada = data_inicial + i * intervalo
    data_entrega = data_retirada + intervalo
    tabela.append([integrante, data_retirada.strftime("%d/%b/%Y"), data_entrega.strftime("%d/%b/%Y")])

# Criação do DataFrame
df = pd.DataFrame(tabela, columns=["Nome", "Dia de retirada", "Dia previsto para a entrega"])

# Adicionando a coluna "Dia real de entrega" vazia
df["Dia real de entrega"] = ""

# Exportação para Excel
file_path = '/mnt/data/Rodizio_de_Panos.xlsx'
df.to_excel(file_path, index=False)

file_path
