import numpy as np

def encode_manchester(bits, Rb, sps):
    Tb = 1 / Rb
    N = len(bits)
    t = np.linspace(0, N * Tb, N * sps, endpoint=False)
    s = np.zeros_like(t)

    half = sps // 2

    for i, bit in enumerate(bits):
        if bit == 0:
            s[i*sps:i*sps+half] = 1
            s[i*sps+half:(i+1)*sps] = -1
        else:
            s[i*sps:i*sps+half] = -1
            s[i*sps+half:(i+1)*sps] = 1

    return t, s