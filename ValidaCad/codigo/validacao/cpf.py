"""Validação de CPF (RF04)."""
from __future__ import annotations

from codigo.dominio.erro_validacao import ErroValidacao, Severidade
from codigo.dominio.registro import Registro
from codigo.dominio.resultado import ResultadoValidacao
from codigo.validacao.validador import Validador


class ValidadorCPF(Validador):
    """Sinaliza CPFs com formato ou dígitos verificadores inválidos."""

    def _aplicar(self, registros: list[Registro],
                 resultado: ResultadoValidacao) -> None:
        for registro in registros:
            valor = registro.valor("cpf")
            if valor is None or valor.strip() == "":
                continue  # a ausência é tratada por ValidadorCamposObrigatorios
            if not self.cpf_valido(valor):
                resultado.adicionar_erro(ErroValidacao(
                    linha=registro.linha,
                    campo="cpf",
                    tipo="CPF inválido",
                    valor=valor,
                    severidade=Severidade.CRITICA,
                ))

    @staticmethod
    def cpf_valido(cpf: str) -> bool:
        """Valida um CPF pelos dígitos verificadores (algoritmo oficial)."""
        digitos = [c for c in cpf if c.isdigit()]
        if len(digitos) != 11:
            return False
        if len(set(digitos)) == 1:  # todos iguais, ex.: 111.111.111-11
            return False
        numeros = [int(d) for d in digitos]
        for posicao in (9, 10):
            soma = sum(numeros[i] * (posicao + 1 - i) for i in range(posicao))
            verificador = (soma * 10) % 11
            verificador = 0 if verificador == 10 else verificador
            if verificador != numeros[posicao]:
                return False
        return True
