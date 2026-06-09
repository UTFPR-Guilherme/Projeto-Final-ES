"""Agrega os erros encontrados e calcula o resumo quantitativo."""
from __future__ import annotations

from codigo.dominio.erro_validacao import ErroValidacao


class ResultadoValidacao:
    """Acumula os erros de validação e fornece o resumo da análise.

    É o objeto que atravessa toda a cadeia de validadores: cada validador
    adiciona aqui os problemas que encontrar, e ao final o gerador de
    relatório lê estes dados.
    """

    def __init__(self, total_registros: int) -> None:
        self.total_registros = total_registros
        self._erros: list[ErroValidacao] = []

    def adicionar_erro(self, erro: ErroValidacao) -> None:
        self._erros.append(erro)

    @property
    def erros(self) -> list[ErroValidacao]:
        """Erros ordenados por linha e campo, para um relatório estável."""
        return sorted(self._erros, key=lambda e: (e.linha, e.campo))

    @property
    def linhas_com_erro(self) -> set[int]:
        """Linhas de dados com erro (exclui erros de arquivo/cabeçalho, linha 0)."""
        return {erro.linha for erro in self._erros if erro.linha > 0}

    @property
    def total_inconsistencias(self) -> int:
        return len(self._erros)

    @property
    def registros_com_erro(self) -> int:
        return len(self.linhas_com_erro)

    @property
    def registros_validos(self) -> int:
        return self.total_registros - self.registros_com_erro
