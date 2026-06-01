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

A equipe atua de forma **conjunta em todas as etapas** do projeto (requisitos, implementação, testes e documentação). As responsabilidades abaixo são principais, mas não exclusivas.

- **Guilherme Pontremolez:** leitura e carregamento dos arquivos `.csv`, validação de CPF e de campos obrigatórios; co-condução dos requisitos; testes e documentação.
- **Guilherme Ramalho:** validação de e-mail e de registros duplicados, geração do relatório final; pesquisa e validação do problema com fontes reais; testes e documentação.
- **Ruan Mateus Trizotti:** arquitetura da aplicação, padrões de projeto (Chain of Responsibility e Factory Method) e integração dos módulos; diagramas; testes e documentação.

## Estrutura do Repositório

```
README.md                  # visão geral, problema, público-alvo e equipe
docs/
  requisitos.md            # requisitos, histórias de usuário, elicitação e validação (Sprint 1)
  arquitetura.md           # arquitetura, padrões de projeto e diagramas (Sprint 2)
  padroes_codificacao.md   # padrões de codificação e de gestão/qualidade (Sprint 2)
codigo/
  dominio/                 # entidades (Registro, ErroValidacao, ResultadoValidacao)
  infra/                   # leitura do CSV (LeitorCSV)
  validacao/               # cadeia de validadores (Chain of Responsibility)
  relatorio/               # geradores de relatório (Factory Method)
  main.py                  # ponto de entrada e orquestração do pipeline
dados/                     # CSV de exemplo
```

## Sprints do Projeto

Status das sprints concluídas até a entrega de 02/06:

### Sprint 1: Engenharia de Requisitos
**Status: concluída.** Pitch do problema com fontes reais, requisitos funcionais (RF01 a RF08) e não funcionais (RNF01 a RNF06), histórias de usuário com critérios de aceitação e priorização, síntese da elicitação e registro de validação. Tudo em [`docs/requisitos.md`](docs/requisitos.md).

### Sprint 2: Projeto da Aplicação (Review 02/06)
**Status: concluída.** Itens entregues:

- [x] Documentação dos padrões de codificação e de gestão/qualidade, em [`docs/padroes_codificacao.md`](docs/padroes_codificacao.md);
- [x] Diagrama de arquitetura com componentes, responsabilidades e trade-offs justificados, em [`docs/arquitetura.md`](docs/arquitetura.md);
- [x] Diagramas dos dois padrões de projeto (Chain of Responsibility e Factory Method) com classes reais do código;
- [x] Demonstração funcional inicial no terminal, com o código em [`codigo/`](codigo/) rodando sobre um CSV de exemplo.
