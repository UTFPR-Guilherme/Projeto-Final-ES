# Estratégia de Testes - Sprint 4

A estratégia de testes adotada foi baseada em **testes automatizados unitários com `unittest`**, utilizando apenas a biblioteca padrão do Python para manter o projeto simples e sem dependências externas. Foram priorizados métodos diretamente ligados às histórias de usuário mais relevantes: `ValidadorCPF.cpf_valido`, `ValidadorEmail.validar`, `ValidadorDuplicados.validar` e `executar`. Para cada comportamento principal, foram criados casos de **sucesso, falha e borda**: CPF válido, CPF inválido e CPF vazio/incompleto; e-mail válido, e-mail sem arroba e e-mail vazio delegado ao validador de obrigatórios; duplicidade inexistente, duplicidade real e CPF repetido com formatos diferentes; além da escrita do relatório em pasta inexistente após refatoração. Essa abordagem é adequada ao escopo do ValidaCad porque as regras de negócio são isoladas em classes pequenas e independentes, o que permite testar cada regra sem depender da execução completa pelo terminal. As principais lacunas não cobertas nesta sprint são testes de desempenho com arquivos muito grandes, testes de codificação inválida em UTF-8, testes de integração para todos os fluxos da CLI e validações futuras como telefone, data de nascimento ou leitura de arquivos `.xlsx`.

## Comando para executar

A partir da pasta `ValidaCad`, execute:

```bash
python -m unittest discover -s testes -v
```

No Windows, também pode ser usado:

```bash
py -m unittest discover -s testes -v
```

## Métodos cobertos

| Arquivo de teste | Método / comportamento testado | Casos cobertos |
| --- | --- | --- |
| `testes/test_cpf.py` | `ValidadorCPF.cpf_valido` | CPF válido, CPF com dígitos repetidos, CPF vazio/incompleto |
| `testes/test_email.py` | `ValidadorEmail.validar` | E-mail válido, e-mail inválido, e-mail vazio delegado ao validador de obrigatórios |
| `testes/test_duplicados.py` | `ValidadorDuplicados.validar` | Sem duplicidade, e-mail duplicado, CPF duplicado com e sem pontuação |
| `testes/test_main_saida.py` | `executar` com caminho de saída | Criação automática da pasta de relatório e gravação do arquivo |

## Resultado esperado

```text
Ran 10 tests
OK
```

## Refatorações realizadas

1. `codigo/main.py`: a gravação do relatório passou a criar automaticamente a pasta de saída quando ela não existe, evitando erro ao usar `relatorios/relatorio.txt`.
2. `codigo/validacao/duplicados.py`: a comparação de CPF duplicado passou a remover caracteres não numéricos, permitindo identificar como duplicados CPFs iguais digitados com e sem pontuação.
