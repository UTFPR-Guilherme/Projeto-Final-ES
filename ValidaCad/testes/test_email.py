"""Testes automatizados do validador de e-mail."""
from __future__ import annotations

import unittest

from codigo.dominio.registro import Registro
from codigo.dominio.resultado import ResultadoValidacao
from codigo.validacao.email import ValidadorEmail


class TestValidadorEmail(unittest.TestCase):
    """Cobre sucesso, falha e borda da validação de e-mail."""

    def validar_email(self, email: str | None) -> ResultadoValidacao:
        registro = Registro(linha=2, campos={"email": email})
        resultado = ResultadoValidacao(total_registros=1)
        ValidadorEmail().validar([registro], resultado)
        return resultado

    def test_email_valido_nao_gera_erro(self) -> None:
        """Sucesso: e-mail em formato básico válido não gera inconsistência."""
        resultado = self.validar_email("ana@email.com")
        self.assertEqual(resultado.total_inconsistencias, 0)

    def test_email_sem_arroba_gera_erro(self) -> None:
        """Falha: e-mail sem arroba deve gerar erro de formato."""
        resultado = self.validar_email("mariaemail.com")
        self.assertEqual(resultado.total_inconsistencias, 1)
        erro = resultado.erros[0]
        self.assertEqual(erro.campo, "email")
        self.assertEqual(erro.tipo, "E-mail em formato inválido")

    def test_email_vazio_eh_ignorado_por_este_validador(self) -> None:
        """Borda: campo vazio é responsabilidade do validador de obrigatórios."""
        resultado = self.validar_email("   ")
        self.assertEqual(resultado.total_inconsistencias, 0)


if __name__ == "__main__":
    unittest.main()
