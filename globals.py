global matPaPe
global nrows
global ncols

def printInformacoes(ordemDasPilhas, qtdPilhasAbertas, timeCounter):
    print("\n[INFO]: Ordem das pilhas: ", end="")
    print(ordemDasPilhas)
    print("\n[INFO]: Quantidade de pilhas abertas: ", end="")
    print(qtdPilhasAbertas)
    print('\n[INFO]: O tempo total de execução foi: ', end="")
    print(timeCounter)