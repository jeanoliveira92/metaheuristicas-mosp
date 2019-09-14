import math
import random
import numpy as np

from Datasource import dataFile as dt

def embaralhar(data):
    aux = list(range(0,len(data)-1))
    random.shuffle(aux)
    return aux

# Função para cálculo do MOSP (Número máximo de Pilhas Abertas)
# Entrada: Sequencia de Padrões (LP)
# Saída: MOSP (NMPA)
def PilhasAbertas(LP):
    if len(LP) > 1:
        Q = dt.matPaPe[LP, :]
        Q = np.maximum.accumulate(Q, axis=0) & np.maximum.accumulate(Q[::-1, :], axis=0)[::-1, :]
        pa = np.sum(Q, 1)
        return pa
    '''else: # Para o caso de uma matriz com uma só coluna.
        Q = ds.matPaPeC[LP, :]
        pa = [np.sum(Q)]
       return pa'''