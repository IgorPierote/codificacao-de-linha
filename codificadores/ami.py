import numpy as np

def encode_ami(bits, Rb, sps):
    Tb = 1 / Rb
    N = len(bits)
    t = np.linspace(0, N * Tb, N * sps, endpoint=False)
    s = np.zeros_like(t)

    nivel = 1

    for i, bit in enumerate(bits):
        if bit == 1:
            s[i*sps:(i+1)*sps] = nivel
            nivel *= -1
        else:
            s[i*sps:(i+1)*sps] = 0

    return t, s