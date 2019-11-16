import random
import numpy as np
import globals as g
import math
from HeuristicaRefinamento import heuristicaRefinamento as hr
from HeuristicaConstrutiva import heuristicaConstrutiva as hc
from HeuristicaPopulacional import grasp

# HEURISTICA POPULACIONAL GRASP PATH RELINK BACKWARD - FIRST IMPROVEMEMENT
def graspPathRelinkBackwardFim(ordemDasPilhas):
    resultadoBom = np.max(hc.PilhasAbertas(ordemDasPilhas))
    # ORDENA A MATRIZ DE FORMA CRESCENTE
    matOrd = grasp.gerarMatrizOrdenada()
    # LISTA D CANDIDATOS
    ls = []
    i = 0
    while i < 150:
        ordemDasPilhasAtual = grasp.construtivaGrasp(matOrd)
        ordemDasPilhasAtual = hr.FirstImprovementMethod(ordemDasPilhasAtual)
        #ADICIONA A LISTA DE CANDIDATOS O RESULTADO ATUAL
        if(len(ls) < 2):
            # VERIFICA REPETICAO
            tem = [np.all(ordemDasPilhasAtual == x) for x in ls]
            # ADICIONA SE NAO TIVER REPETIDO
            if (not np.any(tem)):
                ls.append(list(ordemDasPilhasAtual))
        else:
            # ESCOLHER UM VETOR
            orderPilhasCandidata = random.choice(ls)
            ordemDasPilhasAtual = backwardPathRelink(list(ordemDasPilhasAtual), list(orderPilhasCandidata))

            if(len(ls) < 20):
                # VERIFICA REPETICAO
                tem = [np.all(ordemDasPilhasAtual == x) for x in ls]

                # ADICIONA SE NAO TIVER REPETIDO
                if (not np.any(tem)):
                    ls.append(list(ordemDasPilhasAtual))
            else:
                # indices = list(range(0, len(ordemDasPilhasAtual)))
                # matPilhasAbertas = [ [np.max(hc.PilhasAbertas(i)), i] for i in ls]
                removeIten = 21

                last = np.max(hc.PilhasAbertas(ordemDasPilhasAtual))

                atual = last
                k = 0
                for j in ls:
                    temp = np.max(hc.PilhasAbertas(j))
                    if (temp > last and temp > atual):
                        removeIten = k
                        last = temp
                    k = k + 1

                if (removeIten < 20):
                    ls.pop(removeIten)

                    tem = [np.all(ordemDasPilhasAtual == x) for x in ls]
                    # ADICIONA SE NAO TIVER REPETIDO
                    if (not np.any(tem)):
                        ls.append(list(ordemDasPilhasAtual))

                # matPilhasAbertas = np.array(matPilhasAbertas)
            # print(matPilhasAbertas[matPilhasAbertas[:,0].argsort()])

        resultadoMelhor       = np.max(hc.PilhasAbertas(ordemDasPilhasAtual))
        if  resultadoMelhor < resultadoBom :
            ordemDasPilhas  = ordemDasPilhasAtual
            resultadoBom    = resultadoMelhor
            i = -1

        i = i+1
    return ordemDasPilhas

def backwardPathRelink(OPA, OPC):
    piorSolucao = []
    melhorSolucao = []
    melhorCusto = 0
    solucaoSaida = []
    # VERIFICA QUAL DAS DUAS PILHAS É A MAIOR OU MENOR
    pilhaA = np.max(hc.PilhasAbertas(OPA))
    pilhaC = np.max(hc.PilhasAbertas(OPC))
    if(pilhaA < pilhaC):
        melhorSolucao   = OPA
        piorSolucao     = OPC
        melhorCusto = pilhaA
    else:
        melhorSolucao = OPC
        piorSolucao = OPA
        melhorCusto = pilhaC

    solucaoSaida = melhorSolucao

    while (list(piorSolucao) != list(melhorSolucao)):
        # CRIA-SE UM VETOR COM INDICE DOS ELEMENTOS DIFERENTES
        vetNaoSimetricos = [i for i in range(len(melhorSolucao)) if melhorSolucao[i] != piorSolucao[i]]
        # REALIZA A TROCA
        for i in range(len(vetNaoSimetricos) - 1):
            melhorSolucao[vetNaoSimetricos[i]], melhorSolucao[vetNaoSimetricos[i + 1]] = melhorSolucao[vetNaoSimetricos[i + 1]], melhorSolucao[vetNaoSimetricos[i]]

        custoAtual = np.max(hc.PilhasAbertas(melhorSolucao))

        if  custoAtual <= melhorCusto:
            solucaoSaida    = piorSolucao
            melhorCusto     = custoAtual

    return solucaoSaida