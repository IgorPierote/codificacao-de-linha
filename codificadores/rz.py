import numpy as np

def encode_rz(bits, Rb, sps):
    Tb = 1 / Rb
    N = len(bits)

    t = np.linspace(0, N * Tb, N * sps, endpoint=False)
    s = np.zeros_like(t)

    half = sps // 2

    for i, bit in enumerate(bits):
        if bit == 1:
            s[i*sps:i*sps + half] = 1
            s[i*sps + half:(i+1)*sps] = 0
        else:
            s[i*sps:(i+1)*sps] = 0

    return t, s