# -*- coding: cp1252 -*-

''' DISCIPLINA: COM936 - METAHEURÍSTICAS PARA PROBLEMAS DE OTIMIZAÇÃO
    PROFESSOR:  RAFAEL DE MAGALHAES DIAS FRINHANI
    ALUNOS:     JEAN CARLOS DE OLIVEIRA     35138
                ROBERT NÍCOLAS MENDES       2018012810
                VICTOR PEREIRA MOREIRA      2016012632
    TEMA:       CUTTING STOCK (PROBLEMA DE CORTE DE ESTOQUE)'''

import sys

from timeCounter import timeCounter
from Datasource import dataFile as dt
from HeuristicaConstrutiva import heuristicaConstrutiva as hc

runType = 0
tc = timeCounter()

print("\n#### CUTTING STOCK (PROBLEMA DE CORTE DE ESTOQUE) ####\n")

#VERIFICA SE HÁ ARGUMENTOS EXTERNOS
if __name__ == "__main__":
    if len(sys.argv) == 1:
        runType = 1

# MODO ARGUMENTO
if runType == 0:
    filename    = sys.argv[1]

# MODO MANUAL
elif runType == 1:
    #'filename = input("Qual nome do dataset: ")
    filename = "scoop-A_AP-9.d_3"

nrows, ncols, data = dt.dataRead(filename)
dt.matPaPe = data

try:
    if len(data) >= 0:
        tc.start()                                  #INICIA O CONTADOR
        LP = hc.embaralhar(data)                    #RANDOMIZA O VETOR
        VP = hc.PilhasAbertas(LP)                   #REALIZA A CONTAGEM DAS PILHAS
        tc.stop()                                   #ENCERRA O CONTADOR
        print(VP)
        print(f'\n[INFO]: O tempo total de execução foi: {tc.total:.5f}')

except ValueError as err:
    print("\n[ERROR]: Opção inválida. Dados ainda não carregados ..." + err)

print("[INFO]: Encerrando.. .")