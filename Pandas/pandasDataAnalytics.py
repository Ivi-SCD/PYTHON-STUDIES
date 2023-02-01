import pandas as pd
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

# Importando Data

aluguel = pd.read_csv("aluguel_amostra.csv", sep = ";")
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

# Removendo e agrupando Outliers

grupoTipo = aluguel.groupby('Tipo')['Valor']

Q1 = grupoTipo.quantile(.25)
Q3 = grupoTipo.quantile(.75)
IIQ = Q3 - Q1
limiteInferior = Q1 - 1.5 * IIQ
limiteSuperior = Q3 + 1.5 * IIQ

aluguel_new = pd.DataFrame()
for tipo in grupoTipo.groups.keys():
    ehTipo = aluguel['Tipo'] == tipo
    ehDentroLimite = (aluguel['Valor'] >= limiteInferior[tipo]) & (aluguel['Valor'] <= limiteSuperior[tipo])
    selecao = ehDentroLimite & ehTipo
    aluguel_selecao = aluguel[selecao]
    aluguel_new = pd.concat([aluguel_new, aluguel_selecao])
    
aluguel_new.to_csv('aluguel_residencial_sem_outliers.csv', sep=',', index=False)

# Extra: Montando gráficos com Matplot

plt.rc('figure', figsize = (15,8))
area = plt.figure()
g1 = area.add_subplot(2,2,1)
g2 = area.add_subplot(2,2,2)
g3 = area.add_subplot(2,2,3)
g4 = area.add_subplot(2,2,4)

g1.scatter(aluguel_new.Valor, aluguel_new.Area)
g1.set_title('Valor X Área')

g2.hist(aluguel_new.Valor)
g2.set_title('Histograma')

aluguelg3 = aluguel_new.Valor.sample(100)
aluguelg3.index = [i+1 for i in range(len(aluguelg3))]
g3.plot(aluguelg3)
g3.set_title('Amostra (Valor)')

grupo = aluguel_new.groupby('Tipo')['Valor']
label = grupo.mean().index
valores = grupo.mean().values
g4.bar(label, valores)
g4.set_title('Valor Médio Por Tipo')

area = ''