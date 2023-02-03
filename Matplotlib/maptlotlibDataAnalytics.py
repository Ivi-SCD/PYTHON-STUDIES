import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

#Gráfico Linear

df = pd.read_csv("monitoramento_tempo.csv")
df['data'] = pd.to_datetime(df['data'])
df_selecao = df[(df['data'] > datetime(2014,5,1)) & (df['data'] < datetime(2014,6,1))]

fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0, 0, 1, 1])
eixo2 = fig.add_axes([0.70, 0.70, 0.3, 0.3])

eixo.grid(True)
eixo.plot(df['data'], df['temperatura'], color = "mediumspringgreen")
eixo.set_xlim(datetime(2014,5,1), datetime(2014,6,1))
eixo.set_ylim(270, 320)
eixo.set_title("Temperatura - Maio 2014", fontsize=20)
eixo.legend(['temperatura'], loc = "lower right", fontsize=15)
eixo.set_ylabel('Temperatura Kelvin', fontsize=20)
eixo.set_xlabel('Data', fontsize=20)

x1 = df_selecao['data'][df_selecao['temperatura'].idxmax()]
y1 = max(df_selecao['temperatura'])

x2 = df_selecao['data'][df_selecao['temperatura'].idxmax()] - pd.Timedelta(hours=80)
y2 = max(df_selecao['temperatura']) - 5

eixo.annotate("Máximo", xy = (x1,y1), fontsize=20, xytext = (x2,y2), arrowprops=dict(facecolor='k'))
eixo.axhline(max(df_selecao['temperatura']), color = 'k', linestyle='--')
eixo.axhline(min(df_selecao['temperatura']), color = 'k', linestyle='--')

x3 = df_selecao['data'][df_selecao['temperatura'].idxmin()]
y3 = min(df_selecao['temperatura'])

x4 = df_selecao['data'][df_selecao['temperatura'].idxmin()] - pd.Timedelta(hours=80)
y4 = min(df_selecao['temperatura']) + 5

eixo.annotate("Mínimo", xy = (x3,y3), fontsize=20, xytext = (x4,y4), arrowprops=dict(facecolor='k'))
eixo.annotate("Máximo", xy = (x1,y1), fontsize=20, xytext = (x2,y2), arrowprops=dict(facecolor='k'))

azul_esquerda = df['data'] < datetime(2014,5,1)
azul_direita = df['data'] > datetime(2014,6,1)

eixo2.plot(df['data'], df['temperatura'], color = "mediumspringgreen")
eixo2.plot(df[azul_esquerda]['data'], df[azul_esquerda]['temperatura'], color = 'powderblue')
eixo2.plot(df[azul_direita]['data'], df[azul_direita]['temperatura'], color = 'powderblue')
eixo2.set_xlim(datetime(2014,1,1), datetime(2015,1,1))
eixo2.set_title("Temperatura em 2014")
eixo2.legend(['temperatura'], loc='best', fontsize = 8)
eixo2.set_ylabel('Temperatura')
eixo2.set_xlabel('Data')
eixo2.grid(True)


#Histograma

velocidade_do_vento_por_dia = df.groupby('dia_da_semana')['velocidade do vento'].mean()
nome_dias = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
velocidade_do_vento_por_dia = velocidade_do_vento_por_dia[nome_dias]

fig2 = plt.figure(figsize=(5,4))
eixo3 = fig2.add_axes([0,0,1,1])

indice = range(len(velocidade_do_vento_por_dia))

eixo3.bar(indice, velocidade_do_vento_por_dia)
eixo3.set_title('Velocidade por dia da semana', fontsize = 15, pad= 12)
eixo3.set_xlabel('Dia da semana', fontsize= 15)
eixo3.set_xticks(indice)
eixo3.set_xticklabels(nome_dias)
eixo3.set_ylabel('Velocidade do vento', fontsize=15)

#Pizza

fig3 = plt.figure(figsize=(5,4))
eixo4 = fig3.add_axes([0,0,1,1])
eixo4.pie(velocidade_do_vento_por_dia, labels=velocidade_do_vento_por_dia.index, autopct='%.1f%%')
eixo4.set_title('Velocidade por dia da semana', fontsize=15, pad=10)

#Dispersão

df2 = pd.read_csv('IRIS.csv')
fig4 = plt.figure(figsize=(15,8))
eixo5 = fig4.add_axes([0,0,1,1])

cores = {'Iris-setosa':'powderblue',
         'Iris-virginica':'mediumspringgreen',
         'Iris-versicolor':'b'}

marcadores = {'Iris-setosa':'x',
         'Iris-virginica':'o',
         'Iris-versicolor':'v'}

for especie in df2['species'].unique():
    tmp = df2[df2['species'] == especie]
    eixo5.scatter(tmp['sepal_length'], tmp['sepal_width'], 
                  color = cores[especie], marker=marcadores[especie],
                  s=100)
    
eixo5.set_title('Gráfico de dispersão', fontsize=25,pad=15)
eixo5.set_xlabel('Comprimento da Sépala', fontsize=15)
eixo5.set_ylabel('Largura da Sépala', fontsize=15)
eixo5.tick_params(labelsize=15)
eixo5.legend(cores, fontsize=20)

#Boxplot

fig5 = plt.figure(figsize=(8,5))
eixo6 = fig5.add_axes([0,0,1,1])

cores = ['mediumspringgreen', 'powderblue', 'b', 'pink']

caixas = eixo6.boxplot(df2.drop('species', axis=1).values, patch_artist=True)

for caixa, cor in zip(caixas['boxes'], cores):
    caixa.set(color=cor)

for outlier in caixas['fliers']:
    outlier.set(marker='x')

eixo6.set_title('Gráfico de Caixa', fontsize=15, pad=10)
eixo6.set_xticklabels(df2.drop('species', axis=1).columns)