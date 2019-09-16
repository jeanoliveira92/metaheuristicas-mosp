import numpy as np
from HeuristicaConstrutiva import heuristicaConstrutiva as hc
from Datasource import dataFile as dt

def DescidaRandomica(quanidadePilhas):
    resultadoBom = np.sum(quanidadePilhas, 0)
    resultadoMelhor = resultadoBom

    while(resultadoMelhor >= resultadoBom):
        ordemPilhas = hc.embaralhar()
        quantidadePilhasNovo = hc.PilhasAbertas(ordemPilhas)
        resultadoMelhor = np.sum(quantidadePilhasNovo)

    return ordemPilhas, quantidadePilhasNovo