import time
import random
from ordenacao import Ordenacao
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from counting_sort import counting_sort

def gerar_valores(quantidade, tipo):
    if tipo == "aleatorio":
        return [random.randint(1, 10000) for _ in range(quantidade)]
    elif tipo == "ordenado":
        return list(range(quantidade, 0, -1))

def main():
    print("Escolha a quantidade de valores:")
    print("1. 10\n2. 100\n3. 1.000\n4. 10.000")
    escolha_quantidade = int(input("Opção: "))
    
    quantidades = {1: 10, 2: 100, 3: 1000, 4: 10000}
    quantidade = quantidades.get(escolha_quantidade, 10)

    print("Escolha a disposição dos valores:")
    print("1. Aleatório\n2. Ordenado Descendente")
    escolha_disposicao = int(input("Opção: "))

    disposicao = {1: "aleatorio", 2: "ordenado"}
    tipo = disposicao.get(escolha_disposicao, "aleatorio")

    valores = gerar_valores(quantidade, tipo)
    
    print("Valores de entrada: ", valores)
    
    print("Escolha o algoritmo de ordenação:")
    print("1. Bubble Sort\n2. Merge Sort\n3. Counting Sort")
    escolha_algoritmo = int(input("Opção: "))

    ordenacao = Ordenacao(valores)
    
    inicio = time.time()
    
    if escolha_algoritmo == 1:
        bubble_sort(ordenacao)
    elif escolha_algoritmo == 2:
        merge_sort(ordenacao)
    elif escolha_algoritmo == 3:
        counting_sort(ordenacao)
    
    fim = time.time()
    
    tempo_execucao = fim - inicio
    
    print("\nValores ordenados: ", ordenacao.valores)
    print("Tempo de execução: {:.6f} segundos".format(tempo_execucao))
    print("Número de comparações: ", ordenacao.comparacoes)
    print("Número de trocas: ", ordenacao.trocas)

if __name__ == "__main__":
    main()
