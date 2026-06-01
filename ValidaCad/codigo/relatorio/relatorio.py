"""Geradores de relatório (produtos do Factory Method)."""
from __future__ import annotations

from abc import ABC, abstractmethod

from codigo.dominio.resultado import ResultadoValidacao


class GeradorRelatorio(ABC):
    """Interface comum dos geradores de relatório (produto abstrato)."""

    @abstractmethod
    def gerar(self, resultado: ResultadoValidacao) -> str:
        """Produz o texto do relatório a partir do resultado da validação."""

    @staticmethod
    def _resumo(resultado: ResultadoValidacao) -> str:
        """Bloco de resumo quantitativo, comum a todos os relatórios (RF08)."""
        return (
            "RELATÓRIO DE VALIDAÇÃO DE CADASTROS\n\n"
            f"Total de registros analisados: {resultado.total_registros}\n"
            f"Registros válidos: {resultado.registros_validos}\n"
            f"Registros com erro: {resultado.registros_com_erro}\n"
            f"Total de inconsistências encontradas: {resultado.total_inconsistencias}"
        )


class RelatorioResumido(GeradorRelatorio):
    """Apresenta apenas o resumo quantitativo da análise."""

    def gerar(self, resultado: ResultadoValidacao) -> str:
        return self._resumo(resultado)


class RelatorioCompleto(GeradorRelatorio):
    """Apresenta o resumo seguido do detalhamento de cada inconsistência (RF07)."""

    def gerar(self, resultado: ResultadoValidacao) -> str:
        partes = [self._resumo(resultado)]
        if resultado.total_inconsistencias == 0:
            partes.append("\nNenhuma inconsistência encontrada. Base íntegra.")
            return "\n".join(partes)
        partes.append("\nERROS ENCONTRADOS:\n")
        for erro in resultado.erros:
            partes.append(
                f"Linha {erro.linha}\n"
                f"- Campo: {erro.campo}\n"
                f"- Erro: {erro.tipo}\n"
                f"- Valor informado: {erro.valor}\n"
                f"- Severidade: {erro.severidade.value}\n"
            )
        return "\n".join(partes)
