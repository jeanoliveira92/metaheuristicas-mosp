import random
import numpy as np
from Datasource import dataFile as dt

# Cria uma lista a partir do embaralhamento dos indices da matriz
def embaralhar():
    aux = list(range(0, dt.nrows))
    random.shuffle(aux)
    return aux

# Recebe a lista de posições e alterna a posição entre duas linhas. Vizinho mais próximo.
def trocarPosicao(LP):
    LPNovo = LP
    a = random.randint(0, dt.nrows-1)
    while True:
        b = random.randint(0, dt.nrows-1)
        if a != b:
            break

    LPNovo[a], LPNovo[b] = LPNovo[b],LPNovo[a]
    return LPNovo

# Função para cálculo do MOSP (Número máximo de Pilhas Abertas)
def PilhasAbertas(LP):
    if len(LP) > 1:
        Q = dt.matPaPe[LP, :]
        Q = np.maximum.accumulate(Q, axis=0) & np.maximum.accumulate(Q[::-1, :], axis=0)[::-1, :]
        pa = np.sum(Q, 1)
        return pa
       #else: # Para o caso de uma matriz com uma só coluna.
       # Q = ds.matPaPeC[LP, :]
       #pa = [np.sum(Q)]
       #return pa'''

def RandonShuffle():
    ordemPilhas      = embaralhar()  # RANDOMIZA O VETOR
    quantidadePilhas = PilhasAbertas(ordemPilhas)  # REALIZA A CONTAGEM DAS PILHAS
    return ordemPilhas, quantidadePilhas
