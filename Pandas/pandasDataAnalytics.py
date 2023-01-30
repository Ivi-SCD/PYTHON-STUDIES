import pandas as pd
import requests
from bs4 import BeautifulSoup

# Importando Data

databaseProdutividade = pd.read_csv('data.csv', sep=',')
index = [i + 1 for i in range(len(databaseProdutividade))]
databaseProdutividade.index = index

# Monta um DataFrame com os 10 primeiros elementos

dezPrimeirosDias  = databaseProdutividade.head(10)

tiposDeDados = pd.DataFrame(databaseProdutividade.dtypes, columns=['Tipos de Dados']) # Vai exibir os tipos das colunas
tiposDeDados.columns.name = 'Variáveis'

print(f"\n\nA base de dados apresenta {databaseProdutividade.shape[0]} registros e {databaseProdutividade.shape[1]} variáveis\n\n") # Primeiro item numero de linhas e segundo o numero de variaveis, colunas

# Lendo um DataFrame em uma tabela em site

'''
url = 'https://www.federalreserve.gov/releases/h3/current/default.htm'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
table = soup.findAll('table')
html_file = f'<html><body>{table}</body></html>'

df = pd.read_html(html_file)
'''

# Para redefinir um index de um dataframe
# Podemos fazer assim:
# (dataframe).index = range((dataframe).shape[0]) ou range(len(dataframe))

# Definindo um Index personalizavel

'''
data = [1,2,3,4,5]
index = ['Linha ' + str(i) for i in range(5)]
s = pd.Series(data, index=index)

Out:
    Linha 0    1
    Linha 1    2
    Linha 2    3
    Linha 3    4
    Linha 4    5


Obs* É possível alterar
'''

# Relatório de Análise Dos dados com selecoes

selecaoIngles = databaseProdutividade["🗺️ English"] == "Yes"
selecaoSono = databaseProdutividade["💤 8hrs Sleep"] == "Yes"
selecaoAcademia = databaseProdutividade["🏋🏼‍♂️Gym"] == "Yes"
selecaoLeitura = databaseProdutividade["📚 Lecture"] == "Yes"
selecaoCoding = databaseProdutividade["🖧 Coding"] == "Yes"

print("Gerando Relatório de Dados...")
print(f"\nFrequencia Ingles: {databaseProdutividade[selecaoIngles].shape[0]/len(databaseProdutividade)*100:.2f}%")
print(f"\nFrequencia Academia: {databaseProdutividade[selecaoAcademia].shape[0]/len(databaseProdutividade)*100:.2f}%")
print(f"\nFrequencia Sono: {databaseProdutividade[selecaoSono].shape[0]/len(databaseProdutividade)*100:.2f}%")
print(f"\nFrequencia Leitura: {databaseProdutividade[selecaoLeitura].shape[0]/len(databaseProdutividade)*100:.2f}%")
print(f"\nFrequencia Coding: {databaseProdutividade[selecaoCoding].shape[0]/len(databaseProdutividade)*100:.2f}%")