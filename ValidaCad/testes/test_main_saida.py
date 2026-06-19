"""Teste da escrita do relatório em arquivo de saída."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from codigo.main import executar


class TestSaidaRelatorio(unittest.TestCase):
    """Cobre a refatoração que cria automaticamente a pasta de saída."""

    def test_executar_cria_pasta_de_saida_quando_nao_existe(self) -> None:
        with tempfile.TemporaryDirectory() as pasta_temporaria:
            base = Path(pasta_temporaria)
            entrada = base / "entrada.csv"
            saida = base / "relatorios" / "relatorio.txt"

            entrada.write_text(
                "id,nome,cpf,email\n"
                "1,Ana,168.995.350-09,ana@email.com\n",
                encoding="utf-8",
            )

            relatorio = executar(str(entrada), str(saida))

            self.assertTrue(saida.exists())
            self.assertIn("Total de registros analisados: 1", relatorio)
            self.assertIn("Total de registros analisados: 1", saida.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
