"""Identificação de registros duplicados (RF06)."""
from __future__ import annotations

from codigo.dominio.erro_validacao import ErroValidacao, Severidade
from codigo.dominio.registro import Registro
from codigo.dominio.resultado import ResultadoValidacao
from codigo.validacao.validador import Validador


class ValidadorDuplicados(Validador):
    """Sinaliza registros duplicados com base em CPF e e-mail.

    A primeira ocorrência é mantida como referência; as repetições
    seguintes são marcadas como duplicadas.
    """

    def _aplicar(self, registros: list[Registro],
                 resultado: ResultadoValidacao) -> None:
        self._marcar_duplicados(registros, resultado,
                                campo="cpf", tipo="CPF duplicado")
        self._marcar_duplicados(registros, resultado,
                                campo="email", tipo="E-mail duplicado")

    @staticmethod
    def _marcar_duplicados(registros: list[Registro],
                           resultado: ResultadoValidacao,
                           campo: str, tipo: str) -> None:
        vistos: set[str] = set()
        for registro in registros:
            valor = registro.valor(campo)
            if valor is None or valor.strip() == "":
                continue
            chave = "".join(valor.split()).lower()  # normaliza p/ comparação
            if chave in vistos:
                resultado.adicionar_erro(ErroValidacao(
                    linha=registro.linha,
                    campo=campo,
                    tipo=tipo,
                    valor=valor,
                    severidade=Severidade.CRITICA,
                ))
            else:
                vistos.add(chave)
