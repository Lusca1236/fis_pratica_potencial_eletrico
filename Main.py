import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Carga import Carga
from Grafico import Grafico


class Main:

    def __init__(self):
        self.grafico = Grafico()
        self.main() # Chama a função main

    # Função que captura cliques
    def on_click(self, event):
        x, y = event.xdata, event.ydata

        print(type(event))
        if x is not None and y is not None:
            # Atualiza gráfico se o valor de x e y não for nulo
            self.grafico.atualiza_grafico(x, y)

    def main(self):

        # Faz os cálculos enquanto a janela estiver aberta
        while True:
            num_cargas = int(input("Digite a quantidade de cargas elétricas: "))

            for i in range(num_cargas):
                x = float(input(f"Digite a posição x da carga {i + 1}: "))
                y = float(input(f"Digite a posição y da carga {i + 1}: "))
                q = float(input(f"Digite o valor da carga {i + 1} (em Coulombs): "))
                self.grafico.cargas.append(
                    Carga(x, y, q)) 

            break

        plt.figure()
        self.grafico.atualiza_grafico(0, 0)
        
        # Chama a função do clique caso encontre o evento de clique
        plt.gcf().canvas.mpl_connect('button_press_event', self.on_click)
        plt.show()

main = Main()
