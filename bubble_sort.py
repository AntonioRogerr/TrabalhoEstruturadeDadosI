# Função que implementa o algoritmo Bubble Sort
def bubble_sort(ordenacao):
    n = len(ordenacao.valores) # Tamanho da lista de valores
    # Loop para iterar sobre todos os elementos
    for i in range(n):
        # Loop interno para comparar os elementos adjacentes
        for j in range(0, n-i-1):
            ordenacao.comparacoes += 1 # Incrementa o contador de comparações
            # Se o elemento atual é maior que o próximo, realiza a troca
            if ordenacao.valores[j] > ordenacao.valores[j+1]:
                ordenacao.valores[j], ordenacao.valores[j+1] = ordenacao.valores[j+1], ordenacao.valores[j]
                ordenacao.trocas += 1 # Incrementa o contador de trocas
