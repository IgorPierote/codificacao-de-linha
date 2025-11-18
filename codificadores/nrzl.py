import numpy as np

def encode_nrzl(bits, Rb, sps):
    Tb = 1 / Rb
    N = len(bits)

    t = np.linspace(0, N * Tb, N * sps, endpoint=False)

    s = np.zeros_like(t)

    for i, bit in enumerate(bits):
        nivel = 1 if bit == 1 else -1
        s[i*sps:(i+1)*sps] = nivel

    return t, s