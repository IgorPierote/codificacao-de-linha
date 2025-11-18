import numpy as np

def encode_nrzi(bits, Rb, sps):
    Tb = 1 / Rb
    N = len(bits)

    t = np.linspace(0, N * Tb, N * sps, endpoint=False)

    s = np.zeros_like(t)
    nivel = 1  

    for i, bit in enumerate(bits):
        if bit == 1:
            nivel *= -1
        s[i*sps:(i+1)*sps] = nivel

    return t, s