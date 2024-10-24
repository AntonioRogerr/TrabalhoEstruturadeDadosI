# Função que implementa o algoritmo Counting Sort
def counting_sort(ordenacao):
    max_val = max(ordenacao.valores) # Valor máximo no vetor
    min_val = min(ordenacao.valores) # Valor mínimo no vetor
    range_of_elements = max_val - min_val + 1 # Intervalo de valores possíveis
    count_arr = [0] * range_of_elements # Array de contagem
    output_arr = [0] * len(ordenacao.valores) # Array de saída ordenada

    # Conta a frequência de cada elemento
    for i in range(len(ordenacao.valores)):
        count_arr[ordenacao.valores[i] - min_val] += 1

    # Atualiza o array de contagem para refletir as posições
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # Constrói o array de saída
    for i in range(len(ordenacao.valores) - 1, -1, -1):
        output_arr[count_arr[ordenacao.valores[i] - min_val] - 1] = ordenacao.valores[i]
        count_arr[ordenacao.valores[i] - min_val] -= 1

    # Copia os valores ordenados de volta para o vetor original
    for i in range(len(ordenacao.valores)):
        ordenacao.valores[i] = output_arr[i]
