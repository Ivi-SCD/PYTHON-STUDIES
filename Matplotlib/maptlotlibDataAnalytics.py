import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

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