"""Leitura do arquivo CSV e conversão para objetos de domínio."""
from __future__ import annotations

import csv

from codigo.dominio.registro import Registro


class ErroLeitura(Exception):
    """Lançada quando o arquivo de entrada não pode ser lido ou interpretado."""


class LeitorCSV:
    """Carrega um arquivo ``.csv`` e o converte em uma lista de Registros."""

    def __init__(self, caminho: str) -> None:
        self.caminho = caminho
        self.colunas: list[str] = []

    def carregar(self) -> list[Registro]:
        """Lê o arquivo e devolve um Registro por linha de dados.

        A linha 1 do arquivo é o cabeçalho; por isso a numeração dos
        registros começa em 2, refletindo a posição real no arquivo.
        """
        try:
            with open(self.caminho, newline="", encoding="utf-8") as arquivo:
                leitor = csv.DictReader(arquivo)
                if leitor.fieldnames is None:
                    raise ErroLeitura("Arquivo CSV vazio ou sem cabeçalho.")
                self.colunas = list(leitor.fieldnames)
                return [
                    Registro(linha=numero, campos=dict(linha))
                    for numero, linha in enumerate(leitor, start=2)
                ]
        except FileNotFoundError as exc:
            raise ErroLeitura(f"Arquivo não encontrado: {self.caminho}") from exc
