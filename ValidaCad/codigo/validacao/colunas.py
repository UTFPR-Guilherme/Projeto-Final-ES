"""Validação da presença das colunas obrigatórias (RF02)."""
from __future__ import annotations

from codigo.dominio.erro_validacao import ErroValidacao, Severidade
from codigo.dominio.registro import Registro
from codigo.dominio.resultado import ResultadoValidacao
from codigo.validacao.validador import Validador


class ValidadorColunas(Validador):
    """Verifica se o arquivo possui todas as colunas obrigatórias (RF02).

    A ausência de uma coluna inteira é um problema de nível de arquivo
    (cabeçalho), e não de um registro específico; por isso o erro usa a
    linha 0. As demais regras só checam o conteúdo das colunas que existem,
    evitando que uma coluna ausente vire um erro repetido em cada linha.
    """

    COLUNAS_OBRIGATORIAS = ("id", "nome", "cpf", "email")
    LINHA_CABECALHO = 0

    def __init__(self, colunas_presentes: list[str] | None = None) -> None:
        super().__init__()
        self._colunas = (tuple(colunas_presentes)
                         if colunas_presentes is not None else None)

    def _aplicar(self, registros: list[Registro],
                 resultado: ResultadoValidacao) -> None:
        if self._colunas is None:
            return  # sem informação do cabeçalho: nada a verificar
        for coluna in self.COLUNAS_OBRIGATORIAS:
            if coluna not in self._colunas:
                resultado.adicionar_erro(ErroValidacao(
                    linha=self.LINHA_CABECALHO,
                    campo=coluna,
                    tipo="Coluna obrigatória ausente",
                    valor="(coluna não existe no arquivo)",
                    severidade=Severidade.CRITICA,
                ))
