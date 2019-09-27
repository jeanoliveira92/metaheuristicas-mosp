import numpy as np
from HeuristicaRefinamento from HeuristicaRefinamento as hf

def ils(QPA, ):

    #S0 -> solucção inicial (JA TEMOS A SOLUCAO INICIAL)

    #s->buscalocal -> usar a first

    enquanto ( os criterios de parada nao estiverem satisfeito) faça
        s' -> perturbacao(historico,s)
        s' -> buscaLocal(s')
        s  -> criterioAceitacao(s, s'', historico)
    fim enquanto

    print (QPA)