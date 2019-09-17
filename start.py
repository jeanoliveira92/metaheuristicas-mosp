# -*- coding: cp1252 -*-

import sys
import main


#PARAMETROS DE ARGUMENTO
#RECE O NOME DO ARQUIVO A SER ABERTO, SENAO, SOLICITA UM
if __name__ == "__main__":
    if len(sys.argv) > 1:
        FILENAME = sys.argv[1]

    # MODO MANUAL
    else:
        FILENAME = input("[INFO]: Qual nome do dataset: ")
        #filename = "scoop-A_AP-9.d_3"
try:
    main.main(str(FILENAME))

except ValueError as err:
    print("\n[ERROR]: Opção inválida. Dados ainda não carregados ..." + err)

print("[INFO]: Encerrando.. .")