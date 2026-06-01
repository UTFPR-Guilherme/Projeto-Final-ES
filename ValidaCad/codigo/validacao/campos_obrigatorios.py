"""Validação de campos obrigatórios (RF03)."""
from __future__ import annotations

from codigo.dominio.erro_validacao import ErroValidacao, Severidade
from codigo.dominio.registro import Registro
from codigo.dominio.resultado import ResultadoValidacao
from codigo.validacao.validador import Validador


class ValidadorCamposObrigatorios(Validador):
    """Sinaliza registros com campos obrigatórios ausentes ou vazios."""

    CAMPOS_OBRIGATORIOS = ("id", "nome", "cpf", "email")

    def _aplicar(self, registros: list[Registro],
                 resultado: ResultadoValidacao) -> None:
        for registro in registros:
            for campo in self.CAMPOS_OBRIGATORIOS:
                valor = registro.valor(campo)
                if valor is None or valor.strip() == "":
                    resultado.adicionar_erro(ErroValidacao(
                        linha=registro.linha,
                        campo=campo,
                        tipo="Campo obrigatório vazio",
                        valor="vazio",
                        severidade=Severidade.CRITICA,
                    ))
