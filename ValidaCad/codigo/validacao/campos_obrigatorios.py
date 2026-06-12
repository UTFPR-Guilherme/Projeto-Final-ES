"""Validação de campos obrigatórios (RF03)."""
from __future__ import annotations

from codigo.dominio.erro_validacao import ErroValidacao, Severidade
from codigo.dominio.registro import Registro
from codigo.dominio.resultado import ResultadoValidacao
from codigo.validacao.validador import Validador


class ValidadorCamposObrigatorios(Validador):
    """Sinaliza registros com campos obrigatórios ausentes ou vazios (RF03).

    Só verifica as colunas que de fato existem no arquivo. A ausência de uma
    coluna inteira é tratada por ValidadorColunas (RF02), evitando que o
    mesmo problema seja reportado uma vez por linha.
    """

    CAMPOS_OBRIGATORIOS = ("id", "nome", "cpf", "email")

    def __init__(self, colunas_presentes: list[str] | None = None) -> None:
        super().__init__()
        self._colunas = (tuple(colunas_presentes)
                         if colunas_presentes is not None else None)

    def _aplicar(self, registros: list[Registro],
                 resultado: ResultadoValidacao) -> None:
        for registro in registros:
            for campo in self.CAMPOS_OBRIGATORIOS:
                if self._colunas is not None and campo not in self._colunas:
                    continue  # coluna ausente: tratada por ValidadorColunas
                valor = registro.valor(campo)
                if valor is None or valor.strip() == "":
                    resultado.adicionar_erro(ErroValidacao(
                        linha=registro.linha,
                        campo=campo,
                        tipo="Campo obrigatório vazio",
                        valor="vazio",
                        severidade=Severidade.CRITICA,
                    ))
