import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("monitoramento_tempo.csv")
df['data'] = pd.to_datetime(df['data'])

fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0, 0, 1, 1])
eixo.plot(df['data'], df['temperatura'], color = "c")
eixo.set_ylabel('Temperatura', fontsize=20)
eixo.set_xlabel('Data', fontsize=20)
eixo.set_title("Temperatura no momento", fontsize=20)
eixo.legend(['temperatura'], loc = "lower right", fontsize=15)
