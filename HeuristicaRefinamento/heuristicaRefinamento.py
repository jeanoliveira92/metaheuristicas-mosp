import numpy as np
import globals as g
import random
from HeuristicaConstrutiva import heuristicaConstrutiva as hc


#---------------------------- RandonUpHillMethod --------------------------------------#

# QPA  = Quantidade de pilhas abertas do primeiro resultado
# imax = número máximo de iterações
def RandonUpHillMethod(QPA, iMax, i = 0):
    #INICIALIZANDO AS VARIAVEIS
    resultadoMelhor  = np.sum(QPA, 0)
    ordemMelhor      = []
    QtdPilhasAbertas = []
    PilhasAbertas    = []
    #FINALIZA QUANDO I FOR MAIOR QUE IMAX
    while(i < iMax):
        i += 1
        ordem                = hc.embaralhar()
        pilhas, QtdPilhas    = hc.PilhasAbertas(ordem)
        resultado            = np.max(QtdPilhas)

        # SE ENCONTRADO UM VALOR OBJETIVO MELHOR, ARMAZENA O RESULTADO E ZERA O CONTADOR
        if resultado < resultadoMelhor:
            ordemMelhor      = ordem
            QtdPilhasAbertas = QtdPilhas
            PilhasAbertas    = pilhas
            resultadoMelhor  = resultado
            i = 0

    return ordemMelhor, PilhasAbertas, QtdPilhasAbertas

#---------------------------- FirstImprovementMethod --------------------------------------#

# QPA = Quantidade de pilhas abertas do primeiro resultado
# OP  = é a ordem de pilhas inicialmente
def FirstImprovementMethod(QPA, OP):
    resultadoBom = np.max(QPA, 0)
    resultadoMelhor = resultadoBom + 1
    ordemMelhor = OP
    QtdPilhasAbertas = []
    PilhasAbertas = hc.PilhasAbertas(ordemMelhor)

    while (resultadoBom < resultadoMelhor):
        ordemMelhor = hc.trocarPosicao(ordemMelhor)
        PilhasAbertas, QtdPilhasAbertas = hc.PilhasAbertas(ordemMelhor)
        resultadoMelhor = np.max(QtdPilhasAbertas)

    return ordemMelhor, PilhasAbertas, QtdPilhasAbertas