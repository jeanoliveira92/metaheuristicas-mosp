# -*- coding: cp1252 -*-
import time
from Datasource             import dataFile              as df
from HeuristicaConstrutiva  import heuristicaConstrutiva as hc
from HeuristicaRefinamento  import heuristicaRefinamento as hr
from HeuristicaPopulacional import grasp                 as grasp
from ILS                    import ils                   as ils
import globals              as g


def main(FILENAME, SELECT):
    print("\nMOSP - MINIMIZATION OF OPEN STACKS PROBLEM (PROBLEMA DE MINIMIZAÇÃO DE PILHAS ABERTAS)")
    try:
        # CARREGA OS DADOS DO ARQUIVO
        df.dataRead(FILENAME)
        # ------------------------- MÉTODO CONSTRUTIVO ---------------------------------------#
        #---------------------------- RandonShuffle ------------------------------------------#
        print("\nRandonShuffle - Método Construtivo")
        ordemDasPilhas   = list(range(0, g.nrows))           # CRIA A LISTA INICIAL
        timeCounter      = time.time()                       # INICIA O CONTADOR
        ordemDasPilhas   = hc.RandonShuffle(ordemDasPilhas)  # METODO CONSTRUTOR
        timeCounter      = time.time() - timeCounter         # ENCERRA O CONTADOR
        qtdPilhasAbertas = hc.PilhasAbertas(ordemDasPilhas)  # REALIZA A CONTAGEM DAS PILHAS
        MatrizDePilhas   = g.matPaPe[ordemDasPilhas, :]      # GERA A MATRIZ A PARTIR DOS INDICES
        nomeMetodo       = 'RandonShuffle'

        g.printInformacoes(ordemDasPilhas, qtdPilhasAbertas, timeCounter)                 # IMPRIME AS INFORMAÇÕES
        df.dataWrite(FILENAME, nomeMetodo, timeCounter, MatrizDePilhas, qtdPilhasAbertas) # GRAVA NO DISCO AS INFORMAÇÕES

        # ---------------------------- FirstImprovementMethod --------------------------------------#
        if(SELECT == 1):
            print("\nFirstImprovementMethod - Método de Refinamento\n")
            # METODO REFINAMENTO
            timeCounter      = time.time()
            ordemDasPilhas   = hr.FirstImprovementMethod(ordemDasPilhas)
            timeCounter      = time.time() - timeCounter
            nomeMetodo       = 'FirstImprovementMethod'

        # ---------------------------- RandonUpHillMethod --------------------------------------#
        elif(SELECT == 2):
            print("\nRandonUpHillMethod - Método de Refinamento\n")

            timeCounter      = time.time()
            ordemDasPilhas   = hr.RandonUpHillMethod(ordemDasPilhas, 100)
            timeCounter      = time.time() - timeCounter
            nomeMetodo       = 'RandonUpHillMethod'

        # ---------------------------- IteratedLocalSearch FirstImprovementMethod --------------------------------------#
        elif(SELECT == 3):
            print("[INFO] Iterated Local Search - First Improvement Method")
            timeCounter     = time.time()
            ordemDasPilhas  = ils.IteratedLocalSearch(ordemDasPilhas, 'FIM')
            timeCounter     = time.time() - timeCounter
            nomeMetodo      = 'IteratedLocalSearchFirstImprovement'

        # ---------------------------- IteratedLocalSearch RandonUpHillMethod  --------------------------------------#
        elif (SELECT == 4):
            print("[INFO] Iterated Local Search - Randon Uphill Method")
            timeCounter     = time.time()
            ordemDasPilhas  = ils.IteratedLocalSearch(ordemDasPilhas, 'RUM')
            timeCounter     = time.time() - timeCounter
            nomeMetodo      = 'IteratedLocalSearchRandonUphill'

        elif(SELECT == 5):
            print("[INFO] GRASP - First Improvement Method")
            timeCounter     = time.time()
            ordemDasPilhas  = grasp.graspFim(ordemDasPilhas)
            timeCounter     = time.time() - timeCounter
            nomeMetodo      = 'GraspFirstImprovement'

        elif (SELECT == 6):
            print("[INFO] GRASP - Randon Uphill Method")
            timeCounter = time.time()
            ordemDasPilhas = grasp.graspRum(ordemDasPilhas)
            timeCounter = time.time() - timeCounter
            nomeMetodo = 'GraspRandonUphill'

        elif (SELECT == 7):
            print("[INFO] GRASP PathRelink Forward - First Improvement Method")
            timeCounter = time.time()
            ordemDasPilhas = grasp.graspPathRelinkForwardFim(ordemDasPilhas)
            timeCounter = time.time() - timeCounter
            nomeMetodo = 'GraspFirstImprovementPathRelinkForward'
        # --------------------------------------- FIM DOS METODOS ---------------------------------------------------#
        # IMPRESSÃO E GRAVAÇÃO NO DISCO
        qtdPilhasAbertas = hc.PilhasAbertas(ordemDasPilhas)  # REALIZA A CONTAGEM DAS PILHAS
        MatrizDePilhas   = g.matPaPe[ordemDasPilhas, :]      # GERA A MATRIZ A PARTIR DOS INDICES

        g.printInformacoes(ordemDasPilhas, qtdPilhasAbertas, timeCounter)

        df.dataWrite(FILENAME, nomeMetodo, timeCounter, MatrizDePilhas, qtdPilhasAbertas)

    except ValueError as err:
        raise(err)