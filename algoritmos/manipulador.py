import sqlite3
import numpy as np
import random
import timeit
from algoritmos.Ordenadores import *

# Conexão com o DB
class Manipulador():

    # Esta função lê todos os itens de uma COLUNA de uma matriz
    # Os parâmetros são:

    # Matriz -> tabela observada para a requisição de dados
    # Array -> Vetor no qual os valores serão armazenados
    # numCol -> número do índice da coluna que será percorrida da matriz

    def PercorreCoordenada(self, Matriz, Array, numCol):
        for cord in range(len(Matriz)):
            Array = np.append(Array,Matriz[cord][numCol])
        return Array

    # Aqui podemos desorganizar um vetor, ele retorna o
    # próprio vetor, mas com posições aleatórias

    def embaralhar(self, vetor):
        random.shuffle(vetor)
        return vetor

    # Esta função exibe de forma precisa o tempo utilizado
    # para realizar a ordenação por completo, para
    # utilizá-la basta informar a operação que será
    # realizada (função) e o parâmetro dela (neste caso
    # em específico, serão utilizadas as funções de
    # ordenação e como parâmetro para elas o vetor
    # que deseja ser ordenado

    def exibeTempoExecucao(self, funcao, *args):
        tempoExecucao1 = timeit.timeit(lambda: funcao(args[0]), number=1000)
        tempoExecucao2 = timeit.timeit(lambda: funcao(args[1]), number=1000)
        tempoExecucaoTotal = tempoExecucao1 + tempoExecucao2
        print(f'Tempo de execução total: {tempoExecucaoTotal:.20f} segundos')
