import random
import numpy as np
import globals as g
import math
from HeuristicaRefinamento import heuristicaRefinamento as hr
from HeuristicaConstrutiva import heuristicaConstrutiva as hc
from HeuristicaPopulacional import grasp

# HEURISTICA POPULACIONAL GRASP PATH RELINK BACKWARD - FIRST IMPROVEMEMENT
def graspPathRelinkMixedFim(ordemDasPilhas):
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
            ordemDasPilhasAtual = forwardPathRelink(list(ordemDasPilhasAtual), list(orderPilhasCandidata))

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

def forwardPathRelink(OPA, OPC):
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

    # VAI REALIZAR A TROCA ENTRE MOVER PARA DIREITA, OU PARA A ESQUERDA
    switch = True
    custoAtual = 0
    while (list(piorSolucao) != list(melhorSolucao)):
        # MENOR PARA O MAIOR
        if(switch):
            # CRIA-SE UM VETOR COM INDICE DOS ELEMENTOS DIFERENTES
            vetNaoSimetricos = [i for i in range(len(piorSolucao)) if piorSolucao[i] != melhorSolucao[i]]
            # REALIZA A TROCAs
            for i in range(len(vetNaoSimetricos) - 1):
                piorSolucao[vetNaoSimetricos[i]], piorSolucao[vetNaoSimetricos[i + 1]] = piorSolucao[ vetNaoSimetricos[i + 1]], piorSolucao[vetNaoSimetricos[i]]

            custoAtual = np.max(hc.PilhasAbertas(piorSolucao))

            switch = False

        # MAIOR PARA O MENOR
        else:
            # CRIA-SE UM VETOR COM INDICE DOS ELEMENTOS DIFERENTES
            vetNaoSimetricos = [i for i in range(len(melhorSolucao)) if melhorSolucao[i] != piorSolucao[i]]
            # REALIZA A TROCA
            for i in reversed(range(len(vetNaoSimetricos) - 1)):
                melhorSolucao[vetNaoSimetricos[i]], melhorSolucao[vetNaoSimetricos[i + 1]] = melhorSolucao[vetNaoSimetricos[i + 1]], melhorSolucao[vetNaoSimetricos[i]]

            custoAtual = np.max(hc.PilhasAbertas(melhorSolucao))

            switch = True

        if  custoAtual <= melhorCusto:
            solucaoSaida    = piorSolucao
            melhorCusto     = custoAtual

    return solucaoSaida