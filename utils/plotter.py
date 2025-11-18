import matplotlib.pyplot as plt
import numpy as np

def plot_signal(t, s, bits, title):
    plt.figure(figsize=(12, 3))
    plt.step(t, s, where='post')
    plt.title(title)
    plt.xlabel("Tempo (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)

    
    for k in range(len(bits) + 1):
        plt.axvline(k, color='gray', linestyle='--', linewidth=0.5)

    plt.tight_layout()
    plt.show()