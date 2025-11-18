from utils.input_loader import load_bits_from_input
from utils.plotter import plot_signal
from utils.analises import calcular_transicoes, calcular_dc, estimar_banda

from codificadores.nrzl import encode_nrzl
from codificadores.nrzi import encode_nrzi
from codificadores.rz import encode_rz
from codificadores.manchester import encode_manchester
from codificadores.manchester_diferencial import encode_manchester_diferencial
from codificadores.ami import encode_ami
from codificadores.pseudoternario import encode_pseudoternario

def main():
    bits = load_bits_from_input()

    Rb = 1
    sps = 100

    codificadores = [
        ("NRZ-L", encode_nrzl),
        ("NRZ-I", encode_nrzi),
        ("RZ", encode_rz),
        ("Manchester", encode_manchester),
        ("Manchester Diferencial", encode_manchester_diferencial),
        ("AMI", encode_ami),
        ("Pseudoternário", encode_pseudoternario)
    ]

    for nome, func in codificadores:
        t, s = func(bits, Rb, sps)

        print(f"\n--- {nome} ---")
        trans = calcular_transicoes(s)
        dc = calcular_dc(s)
        banda = estimar_banda(trans, Rb)

        print(f"DC = {dc:.4f}, Transições = {trans}, Banda = {banda}")

        plot_signal(t, s, bits, nome)

if __name__ == "__main__":
    main()