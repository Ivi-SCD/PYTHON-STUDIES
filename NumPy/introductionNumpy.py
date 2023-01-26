'''
Introdução ao NumPy
'''

import numpy as np

# Construção de uma P.A de 100 termos com NumPy
# Com r = 2 e a1 = 0

pa_cem_com_arange = np.arange(0, 200, 2)

# Com linspace foi necessário informar o último membro
# E a quantidade de termos totais

pa_cem_com_linspace = np.linspace(0, 198, 100, dtype=int)
    
# Soma de todos os termos dessa mesma Pa
# Sn = ((a1 + an) * n )/2

def somaDosTermosPA(n, a_um, array):
    somaDosTermos = (a_um + array[n-1])*n/2
    return somaDosTermos;

print(somaDosTermosPA(100, pa_cem_com_arange[0], pa_cem_com_arange))

# Definição do cálculo IMC

pesos = np.array([106.0, 69.5, 83.6, 63.5])
alturas = np.array([1.98, 1.56, 1.72, 1.80])

def calculoIMC(peso, altura):
    return peso/altura**2

print(calculoIMC(pesos, alturas).round(2))

# Arrays Booleanos

arr_bool = np.arange(11)
print(arr_bool[arr_bool%2==0])

carros_arr_bool = np.array(
    [
         [44410, 5712, 37123, 0, 25757], 
         [2003, 1991, 2019, 2006]
    ])

'''
Adicionando, removendo e sorteando elementos
'''

names_arr_one = np.array(['João', 'Ivisson', 'Maria', 'Albert', 'Junior', 'Cauã'])
names_arr_two = np.array(['Julio', 'Kleber', 'Leticia', 'Bruna'])

print(np.sort(np.concatenate((names_arr_one, names_arr_two), axis = 0)))