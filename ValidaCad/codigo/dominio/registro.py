"""Objeto de domínio que representa um registro (linha) do cadastro."""
from __future__ import annotations


class Registro:
    """Representa uma linha do arquivo de cadastros.

    Mantém o número da linha original (para rastreabilidade no relatório)
    e os campos lidos do CSV em um dicionário ``campo -> valor``.
    """

    def __init__(self, linha: int, campos: dict[str, str]) -> None:
        self.linha = linha
        self._campos = campos

    def valor(self, campo: str) -> str | None:
        """Retorna o valor de um campo, ou ``None`` se ele não existir."""
        return self._campos.get(campo)

    def __repr__(self) -> str:  # facilita a depuração no terminal
        return f"Registro(linha={self.linha}, campos={self._campos})"
