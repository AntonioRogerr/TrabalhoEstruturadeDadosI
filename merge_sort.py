# Função que implementa o algoritmo Merge Sort
def merge_sort(ordenacao, valores=None):
    if valores is None:
        valores = ordenacao.valores # Se não for passado um sub-vetor, usa o vetor principal

    # Se o vetor tem mais de um elemento, divide-o em duas partes
    if len(valores) > 1:
        mid = len(valores) // 2 # Divide o vetor ao meio
        L = valores[:mid] # Parte esquerda
        R = valores[mid:] # Parte direita

        merge_sort(ordenacao, L) # Recursão para a parte esquerda
        merge_sort(ordenacao, R) # Recursão para a parte direita

        i = j = k = 0
        # Junta as partes ordenadas de volta
        while i < len(L) and j < len(R):
            ordenacao.comparacoes += 1 # Incrementa comparações
            if L[i] < R[j]:
                valores[k] = L[i]
                i += 1
            else:
                valores[k] = R[j]
                j += 1
            k += 1

        # Copia o restante da parte esquerda, se houver
        while i < len(L):
            valores[k] = L[i]
            i += 1
            k += 1

        # Copia o restante da parte direita, se houver
        while j < len(R):
            valores[k] = R[j]
            j += 1
            k += 1
