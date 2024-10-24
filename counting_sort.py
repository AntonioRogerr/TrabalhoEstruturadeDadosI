def counting_sort(ordenacao):
    max_val = max(ordenacao.valores)
    min_val = min(ordenacao.valores)
    range_of_elements = max_val - min_val + 1
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(ordenacao.valores)

    for i in range(len(ordenacao.valores)):
        count_arr[ordenacao.valores[i] - min_val] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(ordenacao.valores) - 1, -1, -1):
        output_arr[count_arr[ordenacao.valores[i] - min_val] - 1] = ordenacao.valores[i]
        count_arr[ordenacao.valores[i] - min_val] -= 1

    for i in range(len(ordenacao.valores)):
        ordenacao.valores[i] = output_arr[i]
