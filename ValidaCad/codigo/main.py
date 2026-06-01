"""Ponto de entrada do ValidaCad: orquestra o pipeline de validação.

Uso:
    python -m codigo.main <arquivo.csv> [saida.txt] [--formato completo|resumido]
"""
from __future__ import annotations

import sys

from codigo.dominio.resultado import ResultadoValidacao
from codigo.infra.leitor_csv import ErroLeitura, LeitorCSV
from codigo.relatorio.fabrica import FabricaRelatorio
from codigo.validacao.fabrica import FabricaValidadores


def executar(caminho_entrada: str, caminho_saida: str | None = None,
             formato: str = "completo") -> str:
    """Executa o pipeline completo e devolve o texto do relatório."""
    # 1. Carregamento e conversão para objetos de domínio
    registros = LeitorCSV(caminho_entrada).carregar()

    # 2. Execução da cadeia de validadores (Chain of Responsibility)
    resultado = ResultadoValidacao(total_registros=len(registros))
    cadeia = FabricaValidadores.criar_cadeia()
    cadeia.validar(registros, resultado)

    # 3. Geração do relatório (Factory Method)
    relatorio = FabricaRelatorio.criar(formato).gerar(resultado)

    if caminho_saida:
        with open(caminho_saida, "w", encoding="utf-8") as arquivo:
            arquivo.write(relatorio + "\n")

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
