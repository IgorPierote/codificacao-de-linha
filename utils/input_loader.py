def load_bits_from_input():
    entrada = input("Digite uma sequência de bits ou caminho para .txt: ")

    if entrada.endswith(".txt"):
        with open(entrada, "r") as f:
            line = f.read().strip()
    else:
        line = entrada.strip()

    if not all(c in "01" for c in line):
        raise ValueError("Entrada inválida: deve conter apenas 0 e 1.")

    return [int(b) for b in line]