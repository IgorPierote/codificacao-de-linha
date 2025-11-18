import numpy as np

def encode_manchester_diferencial(bits, Rb, sps):
    Tb = 1 / Rb
    N = len(bits)
    t = np.linspace(0, N * Tb, N * sps, endpoint=False)
    s = np.zeros_like(t)

    half = sps // 2
    nivel = 1

    for i, bit in enumerate(bits):
        if bit == 0:
            nivel *= -1  

        s[i*sps:i*sps+half] = nivel
        s[i*sps+half:(i+1)*sps] = -nivel

    return t, s