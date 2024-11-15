
#   Ordenador BubbleSort, possui notação big O de n^2,
#   utiliza o método por comparação simples

class BubbleSort:
    def OrdenarColunas(self, vetor):
        tmp = 0  # Valor temporário para troca de posição
        for i in range(len(vetor) - 1):
            uvFoiTrocado = False  # Reinicia a variável de controle a cada iteração externa
            for ii in range(len(vetor) - 1 - i):
                if vetor[ii][0] > vetor[ii + 1][0]:  
                    # Troca de posição
                    tmp = vetor[ii]
                    vetor[ii] = vetor[ii + 1]
                    vetor[ii + 1] = tmp
                    uvFoiTrocado = True
            if not uvFoiTrocado:
                break  # Para se nenhuma troca foi feita
        return vetor  # Retorna o vetor ordenado
    
    def OrdenarLinhas(self, vetor):
        tmp = 0  # Valor temporário para troca de posição
        for i in range(len(vetor) - 1):
            uvFoiTrocado = False  # Reinicia a variável de controle a cada iteração externa
            for ii in range(len(vetor) - 1 - i):
                if vetor[ii][1] > vetor[ii + 1][1]:
                    # Troca de posição
                    tmp = vetor[ii]
                    vetor[ii] = vetor[ii + 1]
                    vetor[ii + 1] = tmp
                    uvFoiTrocado = True
            if not uvFoiTrocado:
                break  # Para se nenhuma troca foi feita
        return vetor  # Retorna o vetor ordenado


#   Ordenador InsertionSort, com notação big O de n^2,
#   Utiliza do método por inserção

class InsertionSort:
    def Ordenar(self, array):

        VC = 0 # VC signfica Valor Comparado, referente ao
        # valor que está sendo comparado com a lista ordenada

        # Esta variável vai atuar como ponteiro, indicando o
        # valor que será inserido na parte ordenada do vetor
        # ptr, abreviação para POINTER

        for ptr in range(1, len(array)):

            temp = array[ptr]
            indAnterior = (ptr - 1)
            
            while indAnterior >= 0 and array[indAnterior] > temp:
                array[indAnterior + 1] = array[indAnterior]
                indAnterior -= 1
            array[indAnterior + 1] = temp

        return array

#   Ordenador QuickSort, com notação big O de n^2, utiliza
#   o método de divisão combinado ao modelo de pivô

class QuickSort():

    def Ordenar(self, Array):
        if len(Array) <= 1:
            return Array
        else:
            pivot = Array[len(Array) // 2]      # O Pivô é o elemento central do vetor
            left = [x for x in Array if x < pivot]      # Vetor left (esquerdo), com valores menores que o Pivô
            middle = [x for x in Array if x == pivot]   # Vetor middle (central), com valores iguais que o Pivô
            right = [x for x in Array if x > pivot]     # Vetor right (direito), com valores maiores que o Pivô
            return self.Ordenar(left) + middle + self.Ordenar(right)
            # Utilizando a função de forma recursiva para obter vetores de valor unitário, e aplicando
            # uma comparação por inserção a partir das listas geradas utilizando o pivô

#   Ordenador MergeSort, com notação big O de (nlog(n))
#   o método utiliza modelo de divisão, conquista e combinação

class  MergeSort:

    @staticmethod # Método estático para validar e dividir um array
    def MetadeArray(array):

        # Método que valida o valor obtido da metade do vetor,
        # útil quando o vetor possuir valor ímpar e obter um valor de
        # índice decimal, o que não é aceito, por isso é obtido o módulo
        # do tamanho do array, caso 0, é par e segue normalmente,
        # caso seja ímpar, o valor da metade é subtraído 1, e a divisão
        # do array fica com um a menos na esquerda, o valor é destinado
        # à segunda parte do array (do meio para a direita)

        if (len(array) % 2) == 0:
            return (len(array) / 2)
        else:
            return ((len(array) - 1) / 2)

    def Ordenar(self, array):
        if len(array) > 1:
            meioArray = int(self.MetadeArray(array))

            # Os dois pontos dentro dos colchetes
            # indicam um método chamado slicing em python,
            # ele utiliza o valor que está ao lado para determinar
            # até qual número será dividido, no caso do :meioArray
            # o método seleciona os valores do índice 0 até
            # o índice anterior ao da variável meioArray (início até o meio)
            # no caso do meioArray: ele inicia do valor meioArray
            # e vai até o final do vetor

            subArrEsq = array[:meioArray]      
            subArrDir = array[meioArray:]      

            self.Ordenar(subArrEsq)    # Recursão da função para subdividir os vetores até
            self.Ordenar(subArrDir)    # obter vetores com um valor unitário
            
            i = ii = iii = 0    # Inicializando os índices para percorrer os subvetores

            # Combinação de subvetores para a ordenação
            # é feita em três instâncias de while,
            # cada um com os índices i, ii, e iii

            # O índice i referencia o vetor da esquerda
            # O índice ii referencia o vetor da direita
            # O vetor iii referencia o vetor principal,
            # onde estão sendo inseridos os valores combinados

            # Neste primeiro WHILE, o elemento da esquerda
            # é comparado

            while i < len(subArrEsq) and ii < len(subArrDir):   
                if subArrEsq[i] < subArrDir[ii]:
                    array[iii] = subArrEsq[i]
                    i += 1
                else:
                    array[iii] = subArrDir[ii]
                    ii += 1
                iii += 1

            while i < len(subArrEsq):
                array[iii] = subArrEsq[i]
                i += 1
                iii += 1

            while ii < len(subArrDir):
                array[iii] = subArrDir[ii]
                ii += 1
                iii += 1
        return array
    

class  MergeSort:

    @staticmethod # Método estático para validar e dividir um array
    def MetadeArray(array):

        if (len(array) % 2) == 0:
            return (len(array) / 2)
        else:
            return ((len(array) - 1) / 2)

    def Ordenar(self, array):
        if len(array) > 1:
            meioArray = int(self.MetadeArray(array))

            subArrEsq = array[:meioArray]      
            subArrDir = array[meioArray:]      

            self.Ordenar(subArrEsq)    # Recursão da função para subdividir os vetores até
            self.Ordenar(subArrDir)    # obter vetores com um valor unitário
            
            i = ii = iii = 0    # Inicializando os índices para percorrer os subvetores

            while i < len(subArrEsq) and ii < len(subArrDir):   
                if subArrEsq[i] < subArrDir[ii]:
                    array[iii] = subArrEsq[i]
                    i += 1
                else:
                    array[iii] = subArrDir[ii]
                    ii += 1
                iii += 1

            while i < len(subArrEsq):
                array[iii] = subArrEsq[i]
                i += 1
                iii += 1

            while ii < len(subArrDir):
                array[iii] = subArrDir[ii]
                ii += 1
                iii += 1
        return array
    

