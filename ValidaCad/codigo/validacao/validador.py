"""Elo base da Chain of Responsibility de validação."""
from __future__ import annotations

from abc import ABC, abstractmethod

from codigo.dominio.registro import Registro
from codigo.dominio.resultado import ResultadoValidacao


class Validador(ABC):
    """Elo abstrato da cadeia de validação (Chain of Responsibility).

    Cada validador concreto aplica UMA regra sobre todos os registros e,
    em seguida, delega ao próximo elo da cadeia. Assim, novas regras podem
    ser adicionadas sem alterar as já existentes (princípio Aberto/Fechado).
    """

    def __init__(self) -> None:
        self._proximo: Validador | None = None

    def definir_proximo(self, proximo: Validador) -> Validador:
        """Define o próximo elo e o devolve, permitindo encadear em sequência."""
        self._proximo = proximo
        return proximo

    def validar(self, registros: list[Registro],
                resultado: ResultadoValidacao) -> None:
        """Aplica a regra deste elo e repassa a requisição ao próximo."""
        self._aplicar(registros, resultado)
        if self._proximo is not None:
            self._proximo.validar(registros, resultado)

    @abstractmethod
    def _aplicar(self, registros: list[Registro],
                 resultado: ResultadoValidacao) -> None:
        """Regra específica de cada validador concreto."""
