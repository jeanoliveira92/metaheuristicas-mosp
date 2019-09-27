# -*- coding: cp1252 -*-

import sys
import main
import globals as g

#PARAMETROS DE ARGUMENTO
#RECEBE O NOME DO ARQUIVO A SER ABERTO, SENAO, SOLICITA UM
if __name__ == "__main__":
    if len(sys.argv) > 1:
        FILENAME = sys.argv[0]
        QTD = sys.argv[1]
        g.seedInitialize(sys.argv[2]) #INICIALIZA O SEED

    # MODO MANUAL
    else:
        FILENAME = input("[INFO]: Qual nome do dataset: ")
        QTD      = input("[INFO]: Quantas vezes ir� rodar: ")
        g.seedInitialize(int(input("[INFO]: Qual � o valor da seed: "))) #INICIALIZA O SEED

try:
    counter = 0
    while(counter <= int(QTD)):
        main.main(FILENAME)
        counter += 1

except ValueError as err:
    print("\n[ERROR]: Op��o inv�lida. Dados ainda n�o carregados ..." + err)

print("[INFO]: Encerrando.. .")