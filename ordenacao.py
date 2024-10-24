# Classe Ordenacao para armazenar os valores, número de comparações e trocas
class Ordenacao:
    def __init__(self, valores):
        self.valores = valores # Lista de valores a serem ordenados
        self.comparacoes = 0 # Contador de comparações
        self.trocas = 0 # Contador de trocas
