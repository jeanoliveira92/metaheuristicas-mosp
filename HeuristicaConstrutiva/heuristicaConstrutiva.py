import math
import random
import numpy as np

from Datasource import dataFile as dt

def embaralhar():
    aux = list(range(0, dt.nrows))
    random.shuffle(aux)
    return aux

# Função para cálculo do MOSP (Número máximo de Pilhas Abertas)
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