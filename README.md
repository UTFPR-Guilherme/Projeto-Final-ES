# ValidaCad: Validador Automatizado de Cadastros

## Visão Geral

O **ValidaCad** é um sistema em Python, executado via terminal (sem interface gráfica), que automatiza a validação de cadastros armazenados em arquivos `.csv`. O sistema recebe uma planilha de cadastros, executa uma cadeia de validações sobre cada registro e gera um relatório estruturado com as inconsistências encontradas.

O foco do projeto é aplicar **qualidade de engenharia de software** a um problema real: requisitos bem definidos, escopo delimitado, arquitetura justificada, padrões de projeto aplicados intencionalmente e documentação das decisões.

## Problema que o Sistema Resolve

Empresas, escolas, cursos e equipes administrativas mantêm cadastros de clientes, alunos ou participantes em planilhas, muitas vezes preenchidas manualmente ou importadas de fontes diferentes. Isso gera inconsistências como CPFs inválidos, e-mails incorretos, campos obrigatórios vazios e registros duplicados.

A conferência manual, linha por linha, é demorada e sujeita a falhas humanas. O ValidaCad automatiza essa verificação e produz um relatório claro e rastreável dos problemas encontrados.

## Público-Alvo

- Pequenas empresas que mantêm cadastros de clientes em arquivos `.csv`;
- Setores administrativos de escolas, cursos, associações e organizações;
- Equipes que precisam validar dados antes de importá-los para outro sistema.

## Justificativa do Escopo

O escopo foi definido para ser pequeno, objetivo e completo: o sistema resolve um problema real de conferência de dados cadastrais, evitando funcionalidades excessivas que comprometeriam a entrega. A escolha por arquivos `.csv` mantém o sistema simples de executar e testar, compatível com a realidade de quem já trabalha com planilhas. O projeto prioriza **qualidade de engenharia** em vez de quantidade de funcionalidades.

## Membros da Equipe

| Nome | Matrícula |
| --- | --- |
| Guilherme Pontremolez | 2478412 |
| Guilherme Ramalho | 2320649 |
| Ruan Mateus Trizotti | 2152177 |

## Divisão Inicial de Responsabilidades

A equipe atua de forma **conjunta em todas as etapas** do projeto (requisitos, implementação, testes e documentação). As responsabilidades abaixo são as principais, mas não exclusivas.

- **Guilherme Pontremolez:** leitura e carregamento dos arquivos `.csv`, validação de CPF e de campos obrigatórios; co-condução dos requisitos; testes e documentação.
- **Guilherme Ramalho:** validação de e-mail e de registros duplicados, geração do relatório final; pesquisa e validação do problema com fontes reais; testes e documentação.
- **Ruan Mateus Trizotti:** arquitetura da aplicação, padrões de projeto (Chain of Responsibility e Factory Method) e integração dos módulos; diagramas; testes e documentação.

## Estrutura do Repositório

```
README.md                    # visão geral, problema, público-alvo e equipe (este arquivo)
ValidaCad/                   # código, documentação e dados do projeto
  docs/
    requisitos.md            # requisitos, histórias de usuário, elicitação e validação (Sprint 1)
    arquitetura.md           # arquitetura, padrões de projeto e diagramas (Sprint 2 e 3)
    padroes_codificacao.md   # padrões de codificação e de gestão/qualidade (Sprint 2)
  codigo/
    dominio/                 # entidades (Registro, ErroValidacao, ResultadoValidacao)
    infra/                   # leitura do CSV (LeitorCSV)
    validacao/               # cadeia de validadores (Chain of Responsibility)
    relatorio/               # geradores de relatório (Factory Method)
    main.py                  # ponto de entrada e orquestração do pipeline
  testes/                    # testes automatizados da Sprint 4
  dados/                     # CSVs de exemplo
```

## Sprints do Projeto

Status das sprints concluídas:

### Sprint 1: Engenharia de Requisitos
**Status: concluída.** Pitch do problema com fontes reais, requisitos funcionais (RF01 a RF08) e não funcionais (RNF01 a RNF06), histórias de usuário com critérios de aceitação e priorização, síntese da elicitação e registro de validação. Tudo em [`ValidaCad/docs/requisitos.md`](ValidaCad/docs/requisitos.md).

### Sprint 2: Projeto da Aplicação (Review 02/06)
**Status: concluída.** Itens entregues:

- [x] Documentação dos padrões de codificação e de gestão/qualidade, em [`ValidaCad/docs/padroes_codificacao.md`](ValidaCad/docs/padroes_codificacao.md);
- [x] Diagrama de arquitetura com componentes, responsabilidades e trade-offs justificados, em [`ValidaCad/docs/arquitetura.md`](ValidaCad/docs/arquitetura.md);
- [x] Diagramas dos dois padrões de projeto (Chain of Responsibility e Factory Method) com classes reais do código;
- [x] Demonstração funcional inicial no terminal, com o código em [`ValidaCad/codigo/`](ValidaCad/codigo/) rodando sobre um CSV de exemplo.

### Sprint 3: Desenvolvimento (Review 12/06)
**Status: concluída.** Implementadas as funcionalidades restantes das histórias de usuário:

- [x] Validação das colunas obrigatórias (RF02): a coluna ausente é reportada uma vez, no nível do arquivo, em vez de linha por linha;
- [x] Robustez na leitura do CSV para casos de borda (codificação não UTF-8, arquivo apenas com cabeçalho, arquivo inexistente);
- [x] Demonstração no terminal cobrindo as histórias, incluindo o exemplo [`ValidaCad/dados/cadastros_sem_coluna.csv`](ValidaCad/dados/cadastros_sem_coluna.csv) com uma coluna faltando.

A validação nova entrou como um `ValidadorColunas` na cadeia (Chain of Responsibility), sem alterar os validadores existentes. Detalhes em [`ValidaCad/docs/arquitetura.md`](ValidaCad/docs/arquitetura.md).

### Sprint 4: Testes e Refatoração (Review 19/06)
**Status: concluída.** Foram adicionados testes automatizados com `unittest`, cobrindo métodos relevantes com casos de sucesso, falha e borda.

- [x] Testes de `ValidadorCPF.cpf_valido`;
- [x] Testes de `ValidadorEmail.validar`;
- [x] Testes de `ValidadorDuplicados.validar`;
- [x] Teste da função `executar` com gravação do relatório em pasta inexistente;
- [x] Refatoração da saída para criar automaticamente a pasta do relatório;
- [x] Refatoração da duplicidade de CPF para comparar apenas os dígitos;
- [x] Documentação da estratégia de testes em [`ValidaCad/docs/estrategia_testes.md`](ValidaCad/docs/estrategia_testes.md).

## Como Executar

Pré-requisito: Python 3.10 ou superior. O código fica dentro da pasta `ValidaCad/`, então rode a partir dela.

```bash
cd ValidaCad

# Relatório completo (resumo e detalhamento dos erros)
python3 -m codigo.main dados/cadastros_exemplo.csv

# Apenas o resumo quantitativo
python3 -m codigo.main dados/cadastros_exemplo.csv --formato resumido

# Exemplo com uma coluna obrigatória faltando (demonstra o RF02)
python3 -m codigo.main dados/cadastros_sem_coluna.csv

# Salvando o relatório em um arquivo .txt
python3 -m codigo.main dados/cadastros_exemplo.csv relatorios/relatorio.txt
```

## Como Executar os Testes

A partir da pasta `ValidaCad/`, execute:

```bash
python3 -m unittest discover -s testes -v
```

No Windows:

```powershell
py -m unittest discover -s testes -v
```

Resultado esperado:

```text
Ran 10 tests
OK
```
