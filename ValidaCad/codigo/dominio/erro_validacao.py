"""Erro de validação e níveis de severidade."""
from __future__ import annotations

from enum import Enum


class Severidade(Enum):
    """Gravidade de uma inconsistência encontrada em um registro."""

    CRITICA = "crítica"
    MEDIA = "média"
    BAIXA = "baixa"


class ErroValidacao:
    """Representa uma inconsistência encontrada em um campo de um registro."""

    def __init__(self, linha: int, campo: str, tipo: str,
                 valor: str, severidade: Severidade) -> None:
        self.linha = linha
        self.campo = campo
        self.tipo = tipo
        self.valor = valor
        self.severidade = severidade

    def __repr__(self) -> str:
        return (f"ErroValidacao(linha={self.linha}, campo={self.campo!r}, "
                f"tipo={self.tipo!r}, severidade={self.severidade.value})")
