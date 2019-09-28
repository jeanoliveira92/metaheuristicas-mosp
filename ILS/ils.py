import numpy as np
import random
import globals as g
from HeuristicaConstrutiva import heuristicaConstrutiva as hc

def perturbacoes(historico, LPNovo):
    hc.trocarPosicao(LPNovo)
    print(LPNovo)

    while (len( [ True for i in historico if i == LPNovo]) > 0):
        hc.trocarPosicao(LPNovo)

    historico.append(list(LPNovo))


def IteratedLocalSearch(LP):
    LPNovo = LP

    PilhasAbertas, QtdPilhasAbertas = hc.PilhasAbertas(LPNovo)
    resultadoBom = np.max(QtdPilhasAbertas)
    resultadoMelhor = resultadoBom
    historico = []

    while resultadoBom <= resultadoMelhor:
        perturbacoes(historico, LPNovo)

        PilhasAbertas, QtdPilhasAbertas = hc.PilhasAbertas(LPNovo)
        resultadoMelhor = np.max(QtdPilhasAbertas)
        ##s' -> buscaLocal(s')
        # s  -> criterioAceitacao(s, s'', historico)

    print(historico)
    return LPNovo, PilhasAbertas, QtdPilhasAbertas