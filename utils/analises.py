import numpy as np

def calcular_transicoes(s):
    return np.sum(np.diff(s) != 0)

def calcular_dc(s):
    return np.mean(s)

def estimar_banda(transicoes, Rb):
    if transicoes / Rb < 0.5:
        return "baixa"
    elif transicoes / Rb < 1.5:
        return "média"
    else:
        return "alta"