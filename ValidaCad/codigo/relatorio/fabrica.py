"""Fábrica de geradores de relatório (Factory Method)."""
from __future__ import annotations

from codigo.relatorio.relatorio import (
    GeradorRelatorio,
    RelatorioCompleto,
    RelatorioResumido,
)


class FabricaRelatorio:
    """Cria o gerador de relatório adequado ao formato solicitado.

    Permite adicionar novos formatos (ex.: JSON) sem alterar o código
    cliente, que continua pedindo o relatório apenas pelo nome do formato.
    """

    _FORMATOS = {
        "completo": RelatorioCompleto,
        "resumido": RelatorioResumido,
    }

    @classmethod
    def criar(cls, formato: str = "completo") -> GeradorRelatorio:
        try:
            return cls._FORMATOS[formato]()
        except KeyError:
            disponiveis = ", ".join(sorted(cls._FORMATOS))
            raise ValueError(
                f"Formato de relatório desconhecido: {formato!r}. "
                f"Disponíveis: {disponiveis}."
            ) from None
