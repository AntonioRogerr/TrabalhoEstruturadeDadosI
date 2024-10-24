def merge_sort(ordenacao, valores=None):
    if valores is None:
        valores = ordenacao.valores

    if len(valores) > 1:
        mid = len(valores) // 2
        L = valores[:mid]
        R = valores[mid:]

        merge_sort(ordenacao, L)
        merge_sort(ordenacao, R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            ordenacao.comparacoes += 1
            if L[i] < R[j]:
                valores[k] = L[i]
                i += 1
            else:
                valores[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            valores[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            valores[k] = R[j]
            j += 1
            k += 1
