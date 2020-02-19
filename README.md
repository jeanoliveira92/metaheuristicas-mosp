## Aplicação de Heurísticas e Metaheurísticas para Resolução de Problemas de Minimização de Pilhas Abertas (MOSP)
Trabalho desenvolvido para a disciplina de Metaheuristicas pra Problemas de Otimização

Problema: Minimização de Pilhas
* Quando a primeira peca de um determinado tipo for produzida, a respectiva pilha é
considerada aberta e permanece neste estado até que a última péca do mesmo tipo seja
produzida, quando então a pilha é considerada fechada, podendo ser removida para outro
local para dar continuidade ao processo de produção.

* Uma vez que uma pilha é aberta, são podería ser fechada e movimentada quando toda a
demanda de pécas do mesmo tipo tiver sido atendida

## Tecnologias
* Python
* Biblioteca Numpy

## Autores

Jean Carlos de Oliveira [(jeanoliveira92)](https://github.com/jeanoliveira92)

Robert Nicolas Mendes [(robertnicolas88)](https://github.com/robertnicolas88)

## Implementação
Heuristicas Construtiva
- Randon Shuffle

Heuristicas Populacionais
- Grasp Path Relink Backward
- Grasp Path Relink Forward
- Grasp Path Relink Mixed

HeuristicaRefinamento
- First Improvement Method
- Randon UpHill Method
- Pesquisa Local
- Iterated Local Search

## Licença
Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE.md] (LICENSE.md) para obter detalhes
