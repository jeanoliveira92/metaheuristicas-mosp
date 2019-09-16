# -*- coding: cp1252 -*-

''' DISCIPLINA: COM936 - METAHEURÍSTICAS PARA PROBLEMAS DE OTIMIZAÇÃO
    PROFESSOR:  RAFAEL DE MAGALHAES DIAS FRINHANI
    ALUNOS:     JEAN CARLOS DE OLIVEIRA     35138
                ROBERT NÍCOLAS MENDES       2018012810
                VICTOR PEREIRA MOREIRA      2016012632
    TEMA:       CUTTING STOCK (PROBLEMA DE CORTE DE ESTOQUE)'''

import sys
import time

from Datasource import dataFile as dt
from HeuristicaConstrutiva import heuristicaConstrutiva as hc
from HeuristicaRefinamento import heuristicaRefinamento as hf

runType = 0

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


try:
    dt.dataRead(filename)

    # METODO CONSTRUTIVO
    timeCounter = time.time()                                          #INICIA O CONTADOR
    ordemPilhas = hc.embaralhar()                                      #RANDOMIZA O VETOR
    quantidadePilhas = hc.PilhasAbertas(ordemPilhas)                   #REALIZA A CONTAGEM DAS PILHAS
    timeCounter = time.time() - timeCounter                            #ENCERRA O CONTADOR

    #IMPRESSÃO DO MODO CONSTRUTIVO
    print("\nCONSTRUTIVO\nResultado do método aleatório:\nOrdem das pilhas:\n")
    print(ordemPilhas)
    print("\nQuantidade de pilhas abertas")
    print(quantidadePilhas)
    print(f'\n[INFO]: O tempo total de execução foi: {timeCounter:f}')

    #METODO REFINAMENTO
    timeCounter = time.time()
    ordemPilhasNovo, quantidadePilhasNovo = hf.DescidaRandomica(quantidadePilhas)
    timeCounter = time.time() - timeCounter

    #IMPRESSÃO DO MODO REFINAMENTO
    print("\nREFINAMENTO\nResultado do método de refinamento:\nOrdem das pilhas:\n")
    print(ordemPilhasNovo)
    print("\nQuantidade de pilhas abertas")
    print(quantidadePilhasNovo)
    print(f'\n[INFO]: O tempo total de execução foi: {timeCounter:f}')


except ValueError as err:
    print("\n[ERROR]: Opção inválida. Dados ainda não carregados ..." + err)

print("[INFO]: Encerrando.. .")