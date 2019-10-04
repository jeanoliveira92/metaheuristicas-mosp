import numpy as np
import random
import globals as g
from HeuristicaConstrutiva import heuristicaConstrutiva as hc
from HeuristicaRefinamento import heuristicaRefinamento as hr

def perturbacoes(historico, LPNovo):
    hc.trocarPosicao(LPNovo)
    while (len( [ True for i in historico if i == LPNovo]) > 0):
        hc.trocarPosicao(LPNovo)

    historico.append(list(LPNovo))



def IteratedLocalSearch(LP, Method):
    LPNovo = LP
    PilhasAbertas, QtdPilhasAbertas = hc.PilhasAbertas(LPNovo)
    resultadoBom = np.max(QtdPilhasAbertas)
    resultadoMelhor = resultadoBom
    historico = []
    tentativas = 0

    LPFINAL = LPNovo
    PILHASABERTASFINAL = PilhasAbertas
    QTDPILHASFINAL = QtdPilhasAbertas

    while (tentativas < 100):
        perturbacoes(historico, LPNovo)
        PilhasAbertas, QtdPilhasAbertas = hc.PilhasAbertas(LPNovo)
        if(Method == 0):
            LPNovo, PilhasAbertas, QtdPilhasAbertas = hr.FirstImprovementMethod(QtdPilhasAbertas, LPNovo)
        else:
            LPNovo, PilhasAbertas, QtdPilhasAbertas = hr.RandonUpHillMethod(QtdPilhasAbertas, 100)
        resultadoMelhor = np.max(QtdPilhasAbertas)

        if (resultadoBom > resultadoMelhor) and (len( [ True for i in historico if i == LPNovo]) == 0):
            resultadoBom = resultadoMelhor
            LPFINAL = list(LPNovo)
            PILHASABERTASFINAL = PilhasAbertas
            QTDPILHASFINAL = QtdPilhasAbertas
            # s  -> criterioAceitacao(s, s'', historico)
        else:
            tentativas = tentativas + 1
            #print("tentativas " + str(tentativas));

    return LPFINAL, PILHASABERTASFINAL, QTDPILHASFINAL