"""Fábrica que cria e encadeia os validadores (Factory Method)."""
from __future__ import annotations

from codigo.validacao.campos_obrigatorios import ValidadorCamposObrigatorios
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
    def criar_cadeia() -> Validador:
        """Cria os validadores, encadeia-os e devolve o primeiro elo."""
        obrigatorios = ValidadorCamposObrigatorios()
        cpf = ValidadorCPF()
        email = ValidadorEmail()
        duplicados = ValidadorDuplicados()

        # obrigatorios -> cpf -> email -> duplicados
        obrigatorios.definir_proximo(cpf)
        cpf.definir_proximo(email)
        email.definir_proximo(duplicados)

        return obrigatorios
