import random
import globals as g
import numpy as np
from Datasource import dataFile as dt

# Cria uma lista a partir do embaralhamento dos indices da matriz
def embaralhar(ordemDasPilhas):
    return random.sample(ordemDasPilhas, len(ordemDasPilhas))

# Recebe a lista de posições e alterna a posição entre duas linhas. Vizinho mais próximo.
def trocarPosicao(LP):
    a = random.randint(0, len(LP)-1)
    b = a
    while True:
        b = random.randint(0, len(LP)-1)
        if a != b:
            break
    LP[a], LP[b] = LP[b],LP[a]
    return LP

# Função para cálculo do MOSP (Número máximo de Pilhas Abertas)
def PilhasAbertas(LP):
    if len(LP) > 1:
        Q = g.matPaPe[LP, :]
        Q = np.maximum.accumulate(Q, axis=0) & np.maximum.accumulate(Q[::-1, :], axis=0)[::-1, :]
        pa = np.sum(Q, 1)
        return pa

def RandonShuffle(ordemDasPilhas):
    return embaralhar(ordemDasPilhas)  # RANDOMIZA O VETOR


''' Função para obtenção do MOSP (Número máximo de Pilhas Abertas)

    Entrada: Sequencia de Padrões (LP)

    Saída: MOSP (NMPA)'''


def MOSP(LP):
    vetor = PilhasAbertas(LP)
    return np.amax(vetor)  # Obtem a maior pilha do vetor


''' Função para cálculo do MMOSP
    Entrada: Sequencia de Padrões (LP)
    Saída: MMOSP'''
def MMOSP(LP):
    vetor = PilhasAbertas(LP)
    mosp = np.amax(vetor)  # Obtem a maior pilha do vetor
    somatorioMOSP = np.sum(vetor)
    MMOSP = mosp + (somatorioMOSP / (len(vetor) * mosp))
    return MMOSP