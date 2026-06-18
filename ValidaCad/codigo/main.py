"""Ponto de entrada do ValidaCad: orquestra o pipeline de validação.

Uso:
    python -m codigo.main <arquivo.csv> [saida.txt] [--formato completo|resumido]
"""
from __future__ import annotations

import sys
from pathlib import Path

from codigo.dominio.resultado import ResultadoValidacao
from codigo.infra.leitor_csv import ErroLeitura, LeitorCSV
from codigo.relatorio.fabrica import FabricaRelatorio
from codigo.validacao.fabrica import FabricaValidadores


def executar(caminho_entrada: str, caminho_saida: str | None = None,
             formato: str = "completo") -> str:
    """Executa o pipeline completo e devolve o texto do relatório."""
    # 1. Carregamento e conversão para objetos de domínio
    leitor = LeitorCSV(caminho_entrada)
    registros = leitor.carregar()

    # 2. Execução da cadeia de validadores (Chain of Responsibility).
    #    O cabeçalho lido permite verificar as colunas obrigatórias (RF02).
    resultado = ResultadoValidacao(total_registros=len(registros))
    cadeia = FabricaValidadores.criar_cadeia(leitor.colunas)
    cadeia.validar(registros, resultado)

    # 3. Geração do relatório (Factory Method)
    relatorio = FabricaRelatorio.criar(formato).gerar(resultado)

    if caminho_saida:
        caminho = Path(caminho_saida)
        if caminho.parent != Path("."):
            caminho.parent.mkdir(parents=True, exist_ok=True)
        caminho.write_text(relatorio + "\n", encoding="utf-8")

    return relatorio


def main(argumentos: list[str]) -> int:
    if not argumentos:
        print("Uso: python -m codigo.main <arquivo.csv> "
              "[saida.txt] [--formato completo|resumido]")
        return 1

    formato = "completo"
    posicionais: list[str] = []
    indice = 0
    while indice < len(argumentos):
        arg = argumentos[indice]
        if arg == "--formato":
            if indice + 1 >= len(argumentos):
                print("Erro: --formato requer um valor (completo ou resumido).")
                return 1
            formato = argumentos[indice + 1]
            indice += 2
        else:
            posicionais.append(arg)
            indice += 1

    caminho_entrada = posicionais[0]
    caminho_saida = posicionais[1] if len(posicionais) > 1 else None

    try:
        relatorio = executar(caminho_entrada, caminho_saida, formato)
    except ErroLeitura as exc:
        print(f"Erro ao ler o arquivo: {exc}")
        return 1
    except ValueError as exc:
        print(f"Erro: {exc}")
        return 1

    print(relatorio)
    if caminho_saida:
        print(f"\nRelatório salvo em: {caminho_saida}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
