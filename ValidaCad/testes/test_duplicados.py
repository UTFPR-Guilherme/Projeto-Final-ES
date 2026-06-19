"""Testes automatizados da identificação de registros duplicados."""
from __future__ import annotations

import unittest

from codigo.dominio.registro import Registro
from codigo.dominio.resultado import ResultadoValidacao
from codigo.validacao.duplicados import ValidadorDuplicados


class TestValidadorDuplicados(unittest.TestCase):
    """Cobre sucesso, falha e borda da detecção de duplicidades."""

    def executar(self, registros: list[Registro]) -> ResultadoValidacao:
        resultado = ResultadoValidacao(total_registros=len(registros))
        ValidadorDuplicados().validar(registros, resultado)
        return resultado

    def test_sem_duplicidade_nao_gera_erro(self) -> None:
        """Sucesso: CPFs e e-mails diferentes não geram inconsistência."""
        registros = [
            Registro(2, {"cpf": "529.982.247-25", "email": "joao@email.com"}),
            Registro(3, {"cpf": "168.995.350-09", "email": "ana@email.com"}),
        ]
        resultado = self.executar(registros)
        self.assertEqual(resultado.total_inconsistencias, 0)

    def test_email_duplicado_gera_erro_na_segunda_ocorrencia(self) -> None:
        """Falha: repetição de e-mail deve marcar a segunda ocorrência."""
        registros = [
            Registro(2, {"cpf": "529.982.247-25", "email": "JOAO@EMAIL.COM"}),
            Registro(3, {"cpf": "168.995.350-09", "email": " joao@email.com "}),
        ]
        resultado = self.executar(registros)
        self.assertEqual(resultado.total_inconsistencias, 1)
        erro = resultado.erros[0]
        self.assertEqual(erro.linha, 3)
        self.assertEqual(erro.tipo, "E-mail duplicado")

    def test_cpf_com_e_sem_pontuacao_eh_duplicado(self) -> None:
        """Borda: mesmo CPF com formatos diferentes deve ser considerado duplicado."""
        registros = [
            Registro(2, {"cpf": "529.982.247-25", "email": "a@email.com"}),
            Registro(3, {"cpf": "52998224725", "email": "b@email.com"}),
        ]
        resultado = self.executar(registros)
        self.assertEqual(resultado.total_inconsistencias, 1)
        self.assertEqual(resultado.erros[0].tipo, "CPF duplicado")


if __name__ == "__main__":
    unittest.main()
