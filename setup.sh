#!/bin/bash

echo "========================================"
echo "  Projeto Codificação de Linha - Setup"
echo "========================================"

# Verifica se python3 existe
if ! command -v python3 &> /dev/null
then
    echo "ERRO: python3 não encontrado. Instale o Python 3 antes de continuar."
    exit 1
fi

echo "Criando ambiente virtual (venv)..."
python3 -m venv venv

echo "Ativando ambiente virtual..."
source venv/bin/activate

echo "Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

echo "========================================"
echo "Setup concluído com sucesso! 🎉"
echo ""
echo "Para rodar o projeto:"
echo "    source venv/bin/activate"
echo "    python main.py"
echo ""
echo "Para sair do ambiente virtual:"
echo "    deactivate"
echo "========================================"