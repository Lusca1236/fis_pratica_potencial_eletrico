import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from enum import Enum

class ValCarga(Enum):
    X = 0
    Y = 1
    Q = 2

K = 8.99e9 #DEFINIDA AQUI COMO VARIAVEL CONSTANTE E GLOBAL PARA TODO O CÓDIGO

cargas = []

def calcula_potencial(x,y, cargas):
    potencial = 0
    
    #Este for calcula o potencial 
    for carga in cargas:
        disX = x - carga[ValCarga.X]
        disY = y - cargas[ValCarga.Y]
        raio = np.sqrt(disX**2 + disY**2)
        potencial = K* carga[ValCarga.Q] / raio
    
    return potencial