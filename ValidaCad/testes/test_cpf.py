"""Testes automatizados do validador de CPF."""
from __future__ import annotations

import unittest

from codigo.validacao.cpf import ValidadorCPF


class TestValidadorCPF(unittest.TestCase):
    """Cobre sucesso, falha e borda do método cpf_valido."""

    def test_cpf_valido_com_formatacao(self) -> None:
        """Sucesso: CPF real válido com pontos e traço deve ser aceito."""
        self.assertTrue(ValidadorCPF.cpf_valido("529.982.247-25"))

    def test_cpf_invalido_com_digitos_repetidos(self) -> None:
        """Falha: CPF com todos os dígitos iguais deve ser rejeitado."""
        self.assertFalse(ValidadorCPF.cpf_valido("111.111.111-11"))

    def test_cpf_borda_vazio_ou_incompleto(self) -> None:
        """Borda: valor vazio ou com menos de 11 dígitos deve ser rejeitado."""
        self.assertFalse(ValidadorCPF.cpf_valido(""))
        self.assertFalse(ValidadorCPF.cpf_valido("123.456"))


if __name__ == "__main__":
    unittest.main()
