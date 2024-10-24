def bubble_sort(ordenacao):
    n = len(ordenacao.valores)
    for i in range(n):
        for j in range(0, n-i-1):
            ordenacao.comparacoes += 1
            if ordenacao.valores[j] > ordenacao.valores[j+1]:
                ordenacao.valores[j], ordenacao.valores[j+1] = ordenacao.valores[j+1], ordenacao.valores[j]
                ordenacao.trocas += 1
