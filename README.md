📘 Projeto: Simulador de Codificação de Linha

Este projeto implementa um simulador completo de esquemas de codificação de linha, desenvolvido como parte da disciplina Comunicação de Dados.

O programa recebe uma sequência de bits, gera o sinal correspondente em diferentes esquemas de codificação, exibe os gráficos e calcula métricas importantes do sinal.

⸻

🎯 Objetivo do Projeto

Implementar em Python um sistema capaz de:
	•	Codificar uma sequência de bits em 7 esquemas de codificação:
	1.	NRZ-L
	2.	NRZ-I
	3.	RZ
	4.	Manchester
	5.	Manchester Diferencial
	6.	AMI
	7.	Pseudoternário
	•	Gerar gráficos dos sinais usando matplotlib
	•	Exibir no terminal análises como:
	•	Número de transições
	•	Componente DC
	•	Estimativa da largura de banda

⸻

⚙️ Tecnologias Utilizadas
	•	Python 3
	•	NumPy
	•	Matplotlib

⸻

🚀 Como Rodar o Projeto

✔ Passo 1 — Abra o terminal na pasta do projeto

Exemplo:

cd projeto_codificacao_de_linha

⸻

✔ Passo 2 — Execute o script de instalação

O projeto possui um script automático para criar e configurar o ambiente virtual:

./setup.sh

Esse script:
	•	Cria o ambiente virtual venv/
	•	Ativa o ambiente virtual
	•	Instala todas as dependências necessárias

⸻

✔ Passo 3 — Ativar o ambiente virtual (caso ainda não esteja ativo)

Sempre que quiser rodar o projeto novamente:

source venv/bin/activate

⸻

✔ Passo 4 — Executar o programa

python main.py

O programa pedirá:

Digite uma sequência de bits ou caminho para .txt:

Exemplo de entrada:

1011001110

Ou:

bits.txt

(Arquivo contendo uma linha com 0 e 1)

⸻

📊 O que o programa exibe

Para cada codificação:
	•	Abre um gráfico step mostrando o sinal
	•	Delimita visualmente os intervalos de bits
	•	Exibe no terminal:

--- Manchester ---
DC = 0.0000, Transições = 10, Banda = alta
⸻

🧪 Testes Recomendados
	•	Entrada simples: 1010
	•	Apenas zeros: 00000
	•	Apenas uns: 11111
	•	Arquivo .txt com: 1100110011
