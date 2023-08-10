import matplotlib.pyplot as plt
import numpy as np

from Carga import Carga
from Constantes import Constantes


class Grafico:
    def __init__(self):
        self.cargas = [] # Lista de cargas
        
        self.grid = np.linspace(-40, 40, Constantes.pontos())

        '''
        Cria uma grade que vai de -30 até 30 que
        pode ser alterada a depdender da posição
        das cargas ou da posição do clique.
        
        Estes valores serão utilizados para calcular
        o potencial em cada ponto do gráfico.
        '''
        self.X, self.Y = np.meshgrid(self.grid, self.grid)
        '''
        Recebe o mesmo valor de X e Y, mas substitui por zeros.
        
        O valor de cada posição deste array será utilizado
        para desenhar a equipotencial.
        '''
        self.VALORES_Q = np.zeros_like(self.X)

    def desenha_grafico(self, x, y):
        potencial = Carga.calcula_potencial(x, y, self.cargas)
        plt.title(f"Potencial elétrico: {potencial:.2f} Volts")
        plt.scatter(x, y, s=200, marker='o', c='purple')
        plt.text(x, y, f"({x:.2f}, {y:.2f})", ha='center', va='bottom')
    def desenha_linha_equipotencial(self, x, y):

        # Calcula o potencial do lugar clicado
        potencial_alvo = Carga.calcula_potencial(x, y, self.cargas)

        # Configura a linha de contorno
        self.VALORES_Q = Carga.calcula_potencial(self.X, self.Y, self.cargas)
        
        # Faz a linha equipotencial com base nos valores iguais ao potencial do ponto clicado
        plt.contour(self.X, self.Y, self.VALORES_Q, levels=[potencial_alvo], colors='grey')

    def atualiza_grafico(self, x, y):
        plt.clf()

        for carga in self.cargas:
            plt.scatter(carga.x, carga.y, s=200, marker='o', c='pink')
            plt.text(carga.x, carga.y, f"{carga.q} C", ha='center', va='center')

        self.desenha_linha_equipotencial(x, y)

        self.desenha_grafico(x, y)

        plt.xlabel("Coordenada x (m)")
        plt.ylabel("Coordenada y (m)")
        plt.grid()
        plt.draw()