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

# HEURISTICA POPULACIONAL GRASP - FIRST IMPROVEMEMENT
def graspPathRelinkForwardFim(ordemDasPilhas):
    resultadoBom = np.max(hc.PilhasAbertas(ordemDasPilhas))
    # ORDENA A MATRIZ DE FORMA CRESCENTE
    matOrd = gerarMatrizOrdenada()
    # LISTA D CANDIDATOS
    ls = []

    i = 0
    while i < 150:
        ordemDasPilhasAtual = construtivaGrasp(matOrd)
        ordemDasPilhasAtual = hr.FirstImprovementMethod(ordemDasPilhasAtual)
        #ADICIONA A LISTA DE CANDIDATOS O RESULTADO ATUAL

        if(len(ls) < 2  ):
            ls.append(ordemDasPilhasAtual)
        else:
            # escolher um do vetor
            orderPilhasCandidata = random.choice(ls)
            ordemDasPilhasAtual = forwardPathRelink(ordemDasPilhasAtual, orderPilhasCandidata)
            if( len(ls) < 20):
                ls.append(ordemDasPilhasAtual)

        resultadoMelhor       = np.max(hc.PilhasAbertas(ordemDasPilhasAtual))
        if  resultadoMelhor < resultadoBom :
            ordemDasPilhas  = ordemDasPilhasAtual
            resultadoBom    = resultadoMelhor
            i = -1

        i = i+1
        print(i)

    print("LISTA")
    print(ls)
    return ordemDasPilhas

def forwardPathRelink(OPA, OPC):
    print("forwardPathRelink")
    piorSolucao = []
    melhorSolucao = []
    melhorCusto = 0
    solucaoSaida = []
    print(OPA)
    print(OPC)
    # VERIFICA QUAL DAS DUAS PILHAS É A MAIOR OU MENOR
    pilhaA = np.max(hc.PilhasAbertas(OPA))
    pilhaC = np.max(hc.PilhasAbertas(OPC))
    print(pilhaA)
    print(pilhaC)
    if(pilhaA < pilhaC):
        melhorSolucao   = OPA
        piorSolucao     = OPC
        melhorCusto = pilhaA
    else:
        melhorSolucao = OPC
        piorSolucao = OPA
        melhorCusto = pilhaC

    print(melhorSolucao)
    print(piorSolucao)

    solucaoSaida = melhorSolucao

    while (list(piorSolucao) != list(melhorSolucao)):
        # CRIA-SE UM VETOR COM INDICE DOS ELEMENTOS DIFERENTES
        vetNaoSimetricos = [i for i in range(len(piorSolucao)) if piorSolucao[i] != melhorSolucao[i]]
        print(vetNaoSimetricos)
        # REALIZA A TROCA
        for i in range(len(vetNaoSimetricos) - 1):
            piorSolucao[vetNaoSimetricos[i]], piorSolucao[vetNaoSimetricos[i + 1]] = piorSolucao[vetNaoSimetricos[i + 1]], piorSolucao[vetNaoSimetricos[i]]
        print(piorSolucao)
        custoAtual = np.max(hc.PilhasAbertas(piorSolucao))
        print(melhorCusto)
        print(custoAtual)
        if  custoAtual < melhorCusto:
            print("TROCOU")
            solucaoSaida   = piorSolucao
            melhorCusto     = custoAtual

    return solucaoSaida