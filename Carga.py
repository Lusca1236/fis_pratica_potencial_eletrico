import numpy as np
from Constantes import Constantes as consts
class Carga:
    def __init__(self, x, y, q):
        self.x = x
        self.y = y
        self.q = q
    
    @staticmethod
    def calcula_potencial(x, y, cargas):
        potencial = 0

        for carga in cargas:
            disX = x - carga.x
            disY = y - carga.y
            raio = np.sqrt(disX**2 + disY**2)
            potencial += consts.constanteEletrostatica() * carga.q / raio
    
        return potencial
