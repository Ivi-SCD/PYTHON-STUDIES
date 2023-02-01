import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("monitoramento_tempo.csv")
df['data'] = pd.to_datetime(df['data'])

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