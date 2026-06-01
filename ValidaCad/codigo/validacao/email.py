"""Validação de e-mail (RF05)."""
from __future__ import annotations

import re

from codigo.dominio.erro_validacao import ErroValidacao, Severidade
from codigo.dominio.registro import Registro
from codigo.dominio.resultado import ResultadoValidacao
from codigo.validacao.validador import Validador


class ValidadorEmail(Validador):
    """Sinaliza e-mails em formato inválido."""

    # Formato básico: <parte_local>@<domínio>.<extensão>, sem espaços.
    PADRAO = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def _aplicar(self, registros: list[Registro],
                 resultado: ResultadoValidacao) -> None:
        for registro in registros:
            valor = registro.valor("email")
            if valor is None or valor.strip() == "":
                continue  # a ausência é tratada por ValidadorCamposObrigatorios
            if not self.PADRAO.match(valor.strip()):
                resultado.adicionar_erro(ErroValidacao(
                    linha=registro.linha,
                    campo="email",
                    tipo="E-mail em formato inválido",
                    valor=valor,
                    severidade=Severidade.MEDIA,
                ))
