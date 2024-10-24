# Importa módulos necessários para o programa
import time
import random
from ordenacao import Ordenacao # Classe para armazenar os valores e contadores
from bubble_sort import bubble_sort # Função de ordenação por Bubble Sort
from merge_sort import merge_sort # Função de ordenação por Merge Sort
from counting_sort import counting_sort # Função de ordenação por Counting Sort

# Função para gerar valores aleatórios ou ordenados de forma decrescente
def gerar_valores(quantidade, tipo):
    if tipo == "aleatorio":
        return [random.randint(1, 10000) for _ in range(quantidade)] # Gera valores aleatórios
    elif tipo == "ordenado":
        return list(range(quantidade, 0, -1)) # Gera valores decrescentes

# Função principal que gerencia a execução do programa
def main():
    # Opções para selecionar a quantidade de valores
    print("Escolha a quantidade de valores:")
    print("1. 10\n2. 100\n3. 1.000\n4. 10.000")
    escolha_quantidade = int(input("Opção: "))
    
    # Dicionário para mapear a escolha do usuário com a quantidade de valores
    quantidades = {1: 10, 2: 100, 3: 1000, 4: 10000}
    quantidade = quantidades.get(escolha_quantidade, 10) # Padrão é 10 se escolha for inválida

    # Opções para selecionar a disposição inicial dos valores
    print("Escolha a disposição dos valores:")
    print("1. Aleatório\n2. Ordenado Descendente")
    escolha_disposicao = int(input("Opção: "))

    # Dicionário para mapear o tipo de disposição
    disposicao = {1: "aleatorio", 2: "ordenado"}
    tipo = disposicao.get(escolha_disposicao, "aleatorio") # Padrão é aleatório se escolha for inválida

    # Gera os valores de acordo com as opções selecionadas
    valores = gerar_valores(quantidade, tipo)
    
    # Exibe os valores de entrada
    print("Valores de entrada: ", valores)
    
    # Opções para selecionar o algoritmo de ordenação
    print("Escolha o algoritmo de ordenação:")
    print("1. Bubble Sort\n2. Merge Sort\n3. Counting Sort")
    escolha_algoritmo = int(input("Opção: "))

    # Cria uma instância da classe Ordenacao para armazenar os valores e contadores
    ordenacao = Ordenacao(valores)
    
    # Marca o início do cronômetro
    inicio = time.time()
    
    # Escolha do algoritmo de ordenação baseado na opção do usuário
    if escolha_algoritmo == 1:
        bubble_sort(ordenacao)
    elif escolha_algoritmo == 2:
        merge_sort(ordenacao)
    elif escolha_algoritmo == 3:
        counting_sort(ordenacao)
    
    # Marca o fim do cronômetro
    fim = time.time()
    
    # Calcula o tempo total de execução
    tempo_execucao = fim - inicio
    
    # Exibe o vetor ordenado, o tempo de execução e os contadores de comparações e trocas
    print("\nValores ordenados: ", ordenacao.valores)
    print("Tempo de execução: {:.6f} segundos".format(tempo_execucao))
    print("Número de comparações: ", ordenacao.comparacoes)
    print("Número de trocas: ", ordenacao.trocas)

# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    main()
