"""Fábrica que cria e encadeia os validadores (Factory Method)."""
from __future__ import annotations

from codigo.validacao.campos_obrigatorios import ValidadorCamposObrigatorios
from codigo.validacao.colunas import ValidadorColunas
from codigo.validacao.cpf import ValidadorCPF
from codigo.validacao.duplicados import ValidadorDuplicados
from codigo.validacao.email import ValidadorEmail
from codigo.validacao.validador import Validador


class FabricaValidadores:
    """Centraliza a criação e o encadeamento dos validadores.

    O restante do sistema não precisa conhecer quais validadores existem
    nem a ordem em que são aplicados: basta pedir a cadeia pronta à fábrica.
    Para adicionar uma nova regra, altera-se apenas este método.
    """

    @staticmethod
    def criar_cadeia(colunas: list[str] | None = None) -> Validador:
        """Cria os validadores, encadeia-os e devolve o primeiro elo.

        ``colunas`` é o cabeçalho lido do CSV. Ele permite verificar a
        presença das colunas obrigatórias (RF02) e evitar erro duplicado
        nos campos obrigatórios.
        """
        colunas_presentes = list(colunas) if colunas is not None else None

        colunas_v = ValidadorColunas(colunas_presentes)
        obrigatorios = ValidadorCamposObrigatorios(colunas_presentes)
        cpf = ValidadorCPF()
        email = ValidadorEmail()
        duplicados = ValidadorDuplicados()

        # colunas -> obrigatorios -> cpf -> email -> duplicados
        colunas_v.definir_proximo(obrigatorios)
        obrigatorios.definir_proximo(cpf)
        cpf.definir_proximo(email)
        email.definir_proximo(duplicados)

        return colunas_v
