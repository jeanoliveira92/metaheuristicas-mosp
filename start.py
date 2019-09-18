# -*- coding: cp1252 -*-

import sys
import main
global FILENAME

#PARAMETROS DE ARGUMENTO
#RECE O NOME DO ARQUIVO A SER ABERTO, SENAO, SOLICITA UM
if __name__ == "__main__":
    if len(sys.argv) > 1:
        FILENAME = sys.argv[0]
    # MODO MANUAL
    else:
        FILENAME = input("[INFO]: Qual nome do dataset: ")
        QTD      = input("[INFO]: Quantas vezes irá rodar: ")
        #filename = "scoop-A_AP-9.d_3"
try:
    counter = 0
    while(counter <= int(QTD)):
        main.main(FILENAME)
        counter += 1

except ValueError as err:
    print("\n[ERROR]: Opção inválida. Dados ainda não carregados ..." + err)

print("[INFO]: Encerrando.. .")