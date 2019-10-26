import random
import numpy as np
import globals as g
import math
from HeuristicaRefinamento import heuristicaRefinamento as hr
from HeuristicaConstrutiva import heuristicaConstrutiva as hc


# CONSTRUTIVA GRASP
def gerarMatrizOrdenada():
    # COPIA DA MATRIZ ORIGINAL
    matrixOriginal = g.matPaPe
    # SOMA O PESO TOTAL DE CADA LINHA
    somaLinhas  = np.sum(matrixOriginal, axis=1)
    # CRIA UM VETOR DE INDICES
    indices = list(range(0, g.nrows))
    # ADICIONA O VETOR DE INDICE AO VETOR DE PESOS/LINHA
    matrixOrdenada =  np.c_[indices, somaLinhas]
    # REALIZA A ORDENAÇÃO DECRESCENTE DOS VALORES
    matrixOrdenada = matrixOrdenada[matrixOrdenada[:,1].argsort()[::-1]]
    # REMOVE O VETOR DE PESOS E DEIXA APENAS O DE INDICES
    matrixOrdenada = matrixOrdenada[::,0]
    # GERA A NOVA MATRIX ORDENADA
    return matrixOrdenada


def construtivaGrasp(mOrd):
    # GERA OS VALORES DE CORTE SUPERIOR E INFERIOR
    limiteInferior =  random.randint( math.floor(g.nrows/6), round( 3 * (g.nrows/6))-1)
    limiteSuperior =  random.randint( math.floor(3 * g.nrows/6)+1, round( 5 * (g.nrows/6)))
    # VETOR DE INDICE DOS ELEMENTOS PARTICIONADOS
    indicesDasAmostras  = mOrd[limiteInferior:limiteSuperior]
    print(limiteInferior)
    print(limiteSuperior)
    # EMBARALHA OS ELEMENTOS SELECIONADOS DA MATRIZ
    indicesDasAmostras = random.sample(list(indicesDasAmostras), len(indicesDasAmostras))
    print(indicesDasAmostras)
    # CONCATENA O INDECE DAS AMOSTRA COM O RESTANTE INICAL E FINAL DOS VALORES
    ordemPecaPadrao = np.concatenate((
         mOrd[0:limiteInferior],
         indicesDasAmostras,
         mOrd[limiteSuperior:] ), axis=0)

    print("MATRIZ ORIGINAL: ")
    print(g.matPaPe[mOrd, :])
    print("MATRIZ ORDENADA: ")
    print(g.matPaPe[ordemPecaPadrao, :])
    #return ordemPecaPadrao
    return ordemPecaPadrao

# HEURISTICA POPULACIONAL GRASP
def grasp(ordemDasPilhas):
    resultadoBom = np.max(hc.PilhasAbertas(ordemDasPilhas))
    ordemDasPilhasAtual = ordemDasPilhas

    matOrd = gerarMatrizOrdenada()

    construtivaGrasp(matOrd)

    '''for counter in range(1):
        ordemDasPilhasAtual = construtivaGrasp(ordemDasPilhasAtual)
        #ordemDasPilhasAtual = hr.FirstImprovementMethod(ordemDasPilhasAtual)

        resultadoMelhor       = np.max(hc.PilhasAbertas(ordemDasPilhasAtual))
        if  resultadoMelhor < resultadoBom :
            ordemDasPilhas  = ordemDasPilhasAtual
            resultadoBom    = resultadoMelhor'''

    return ordemDasPilhas
