import math
import random
import numpy as np;

def heuristicaConstrutivaEmbaralhar(container, data):
    aux = data
    aux = random.shuffle(aux)
    return aux

# Função para cálculo do MOSP (Número máximo de Pilhas Abertas)
# Estratégia: 1s consecutivos
# Entrada: Sequencia de Padrões (LP)

# Saída: MOSP (NMPA)
'''
def PilhasAbertas(LP):

    if len(LP) > 1:

        Q = ds.matPaPe[LP, :]

        Q = np.maximum.accumulate(Q, axis=0) & np.maximum.accumulate(Q[::-1, :], axis=0)[::-1, :]

        pa = np.sum(Q, 1)

        return pa

    else: # Para o caso de uma matriz com uma só coluna.

        Q = ds.matPaPeC[LP, :]

        pa = [np.sum(Q)]

       return pa'''