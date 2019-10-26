import numpy as np
import globals as g
import random
from HeuristicaConstrutiva import heuristicaConstrutiva as hc

#---------------------------- FirstImprovementMethod --------------------------------------#

def FirstImprovementMethod(ordemDasPilhas):
    resultadoBom     = np.max(hc.PilhasAbertas(ordemDasPilhas), 0) - 1
    itinerator = 0
    while resultadoBom < np.max(list(hc.PilhasAbertas(ordemDasPilhas)), 0):
        ordemDasPilhas = hc.trocarPosicao(ordemDasPilhas)

        if itinerator >= 100: break
        else: itinerator = itinerator+1

    return ordemDasPilhas

#-------------------------------- RandonUpHillMethod --------------------------------------#

def RandonUpHillMethod(ordemDasPilhas, iMax):
    resultadoBom        = np.max(hc.PilhasAbertas(ordemDasPilhas))
    ordemDasPilhasAtual = ordemDasPilhas
    i = 0
    while i < iMax:
        ordemDasPilhasAtual   = hc.embaralhar(ordemDasPilhasAtual)
        resultadoMelhor       = np.max(hc.PilhasAbertas(ordemDasPilhasAtual))

        if  resultadoMelhor < resultadoBom :
            ordemDasPilhas = ordemDasPilhasAtual
            resultadoBom = resultadoMelhor
            i = -1
        i = i+1

    return ordemDasPilhas

#------------------------------------------------------------------------------------------#

