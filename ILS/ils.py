import numpy as np
from HeuristicaConstrutiva import heuristicaConstrutiva as hc
from HeuristicaRefinamento import heuristicaRefinamento as hr

def perturbacoes(historico, ordemDasPilhas):
    hc.trocarPosicao(ordemDasPilhas)
    while (len( [ True for i in historico if i == list(ordemDasPilhas)]) > 0):
        hc.trocarPosicao(ordemDasPilhas)
    historico.append(list(ordemDasPilhas))


def IteratedLocalSearch(ordemDasPilhas, Method):
    resultadoBom        = np.max( hc.PilhasAbertas(ordemDasPilhas) )
    ordemDasPilhasFinal = ordemDasPilhas
    historico           = [list(ordemDasPilhas)]
    i = 0
    while True:
        perturbacoes(historico, ordemDasPilhas)

        if(Method == 'FIM'):
            ordemDasPilhas = hr.FirstImprovementMethod(ordemDasPilhas)
        elif(Method == 'RUM'):
            ordemDasPilhas = hr.RandonUpHillMethod(ordemDasPilhas, 100)

        resultadoMelhor = np.max(hc.PilhasAbertas(ordemDasPilhas))

        if resultadoBom > resultadoMelhor:
            resultadoBom = resultadoMelhor
            ordemDasPilhasFinal = list(ordemDasPilhas)

        i = i+1
        if i >= 50:
            break

    return ordemDasPilhasFinal