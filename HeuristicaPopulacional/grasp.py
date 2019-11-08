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
    #matrixOrdenada = matrixOrdenada[::,0]
    # GERA A NOVA MATRIX ORDENADA
    return matrixOrdenada


def construtivaGrasp(matrixOrdenada):
    ALPHA = random.uniform(0.0, 1.0)
    # GERA OS VALORES DE CORTE SUPERIOR E INFERIOR
    cMin = np.min(matrixOrdenada[::1], axis=0)[1]
    cMax = np.max(matrixOrdenada[::1], axis=0)[1]
    ce = math.floor(cMin + ( ALPHA * (cMax - cMin)))
    # REMOVE O VETOR DE PESOS E DEIXA APENAS O DE INDICES. ENCONTRA A ULTIMA POSICAO DO ELEMENTO CE NO VETOR PARA CORTAR
    tempMat = matrixOrdenada[::, 1]
    limiteSuperior = list(tempMat)[::1].index(ce)
    # VETOR DE INDICE DOS ELEMENTOS PARTICIONADOS
    indicesDasAmostras = matrixOrdenada[limiteSuperior:][::1]
    # REMOVE RCL DA MATRIZ ORIGINAL
    matrixOrdenada = matrixOrdenada[:limiteSuperior]
    # EMBARALHA OS ELEMENTOS SELECIONADOS DA MATRIZ
    indicesDasAmostras = random.sample(list(indicesDasAmostras), len(indicesDasAmostras))
    # REMOVE OS PESOS DOS INDECES
    indicesDasAmostras = np.array(indicesDasAmostras)[::, 0]
    matrixOrdenada = matrixOrdenada[::, 0]
    # EMBARALHA OS RESTANTES DA RCL
    np.random.shuffle(matrixOrdenada)
    # CONCATENA O RCL COM O RESTANTE INICAL E REMOVE A COLUNA DOS PESOS
    # FICANDO APENAS OS INDICES DA MATRIX ORIGINAL
    ordemPecaPadrao = np.concatenate((
        indicesDasAmostras,
        matrixOrdenada
    ))
    return ordemPecaPadrao

# HEURISTICA POPULACIONAL GRASP - FIRST IMPROVEMEMENT
def graspFim(ordemDasPilhas):
    resultadoBom = np.max(hc.PilhasAbertas(ordemDasPilhas))
    # ORDENA A MATRIZ DE FORMA CRESCENTE
    matOrd = gerarMatrizOrdenada()
    i = 0
    while i < 150:
        ordemDasPilhasAtual = construtivaGrasp(matOrd)
        ordemDasPilhasAtual = hr.FirstImprovementMethod(ordemDasPilhasAtual)

        resultadoMelhor       = np.max(hc.PilhasAbertas(ordemDasPilhasAtual))
        if  resultadoMelhor < resultadoBom :
            ordemDasPilhas  = ordemDasPilhasAtual
            resultadoBom    = resultadoMelhor
            i = -1

        i = i+1
        print(i)

    return ordemDasPilhas

# HEURISTICA POPULACIONAL GRASP - RAMDON UPHILL
def graspRum(ordemDasPilhas):
    resultadoBom = np.max(hc.PilhasAbertas(ordemDasPilhas))
    # ORDENA A MATRIZ DE FORMA CRESCENTE
    matOrd = gerarMatrizOrdenada()
    for counter in range(100):
        ordemDasPilhasAtual = construtivaGrasp(matOrd)
        ordemDasPilhasAtual = hr.RandonUpHillMethod(list(ordemDasPilhasAtual), 100)

        resultadoMelhor       = np.max(hc.PilhasAbertas(ordemDasPilhasAtual))
        if  resultadoMelhor < resultadoBom :
            ordemDasPilhas  = ordemDasPilhasAtual
            resultadoBom    = resultadoMelhor

    return ordemDasPilhas
