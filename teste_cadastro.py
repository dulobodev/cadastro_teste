import csv
import pytest
import os

CSV_FILE = "C:\cadastro_teste\clientes.csv"


def test_csv_existe():
    assert os.path.exists(CSV_FILE), "O arquivo clientes.csv não foi encontrado."


def test_csv_cabecalho():
    with open(CSV_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        cabecalho = next(reader) 
        esperado = ["Nome", "Email", "Cpf", "Salário", "Setor", "Senha", "Cargo"]
        cabecalho_limpo = [col.strip(" /") for col in cabecalho]
        assert cabecalho_limpo == esperado, "Os cabeçalhos estão incorretos."

def test_segunda_linha_csv():
    dados_esperados = ["João Silva", "joao@email.com", "12345678900", "2500", "TI", "senha123", "Analista"]

    with open(CSV_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Pular o cabeçalho
        segunda_linha = next(reader, None)

        assert segunda_linha is not None, "A segunda linha não foi encontrada no arquivo."

        # Limpar espaços extras e aspas
        segunda_linha_limpa = [col.strip().strip('"') for col in segunda_linha]

        assert segunda_linha_limpa == dados_esperados, f"A segunda linha está incorreta: {segunda_linha_limpa}"




def test_exibir_csv():
    with open(CSV_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row) 
