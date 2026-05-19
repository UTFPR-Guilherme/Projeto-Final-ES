# ValidaCad — Validador Automatizado de Cadastros

## Visão Geral

O **ValidaCad** é um sistema desenvolvido em Python para automatizar a validação de cadastros armazenados em bases de dados estruturadas, inicialmente em arquivos `.csv`.

O sistema recebe uma planilha de cadastros como entrada, executa uma cadeia de validações sobre cada registro e gera um relatório estruturado com os problemas encontrados. Entre as validações previstas estão: CPF inválido, e-mail em formato incorreto, campos obrigatórios vazios e registros duplicados.

O foco do projeto não é apenas validar dados, mas aplicar conceitos de Engenharia de Software em um problema real: definição de requisitos, delimitação de escopo, arquitetura justificada, padrões de projeto, testes automatizados e documentação das decisões tomadas.

---

## Problema que o Sistema Resolve

Empresas, escolas, cursos, pequenos negócios e equipes administrativas frequentemente mantêm cadastros de clientes, alunos, usuários ou participantes em planilhas. Esses cadastros podem ser preenchidos manualmente, copiados de formulários diferentes ou importados de outras fontes.

Esse processo pode gerar inconsistências como:

- CPFs inválidos;
- e-mails digitados incorretamente;
- campos obrigatórios não preenchidos;
- registros duplicados;
- dificuldade para localizar erros manualmente;
- perda de confiabilidade na base de dados.

A conferência manual linha por linha é demorada, sujeita a falhas humanas e pouco padronizada. O ValidaCad busca reduzir esse esforço por meio de uma validação automatizada, organizada e rastreável.

---

## Público-Alvo

O sistema é destinado a usuários que manipulam bases cadastrais em formato de planilha, especialmente:

- Pequenas empresas que mantêm cadastros de clientes em arquivos `.csv`;
- Setores administrativos de escolas, cursos, igrejas, associações ou organizações;
- Equipes que precisam validar dados antes de importar cadastros para outro sistema;
- Usuários responsáveis por revisar planilhas sem depender de conferência manual linha por linha.

---

## Objetivo do Projeto

Desenvolver um sistema simples, funcional e bem estruturado para apoiar a qualidade de dados cadastrais.

O objetivo principal é permitir que o usuário forneça uma base de cadastros em `.csv` e receba como saída um relatório indicando quais registros possuem problemas, quais campos foram afetados e qual tipo de erro foi identificado.

O projeto foi delimitado para ser executado inteiramente em Python, sem interface gráfica, com entrada estruturada, processamento automatizado e geração de saída estruturada.

---


## Membros da Equipe

- Guilherme Pontremolez — 2478412
- Guilherme Ramalho — 2320649

---

## Divisão Inicial de Responsabilidades

A equipe atuará de forma conjunta em todas as etapas do projeto, incluindo requisitos, implementação, testes e documentação. A divisão abaixo representa responsabilidades principais, mas não exclusivas.

### Guilherme Pontremolez

- Definição inicial dos requisitos do sistema;
- Organização das histórias de usuário e critérios de aceitação;
- Implementação da leitura dos arquivos de entrada;
- Desenvolvimento das validações de CPF e campos obrigatórios;
- Participação na implementação dos testes automatizados;
- Participação na documentação técnica do projeto.

### Guilherme Ramalho

- Pesquisa e validação do problema com fontes reais;
- Apoio na definição e refinamento do escopo;
- Implementação das validações de e-mail e registros duplicados;
- Organização da geração do relatório final;
- Participação na implementação dos testes automatizados;
- Participação na documentação técnica do projeto.

---

## Sprints do Projeto

### Sprint 1 — Engenharia de Requisitos

- Refinamento da proposta;
- Levantamento e validação dos requisitos;
- Definição das histórias de usuário;
- Escrita dos critérios de aceitação;
- Registro de ambiguidades, conflitos e questões em aberto.

### Sprint 2 — Projeto da Aplicação

- Definição da arquitetura;
- Escolha dos padrões de projeto;
- Criação dos diagramas;
- Definição dos módulos principais;
- Início da codificação.

### Sprint 3 — Desenvolvimento

- Implementação das funcionalidades previstas;
- Demonstração funcional via terminal;
- Ajustes no protótipo;
- Integração entre leitura, validação e relatório.

### Sprint 4 — Testes e Refatoração

- Escrita dos testes automatizados;
- Execução dos testes;
- Refatoração do código;
- Documentação da estratégia de testes;
- Finalização do repositório.

---

## Entrada Esperada

O sistema receberá como entrada um arquivo `.csv` contendo dados cadastrais.

Exemplo de estrutura esperada:

```csv
id,nome,cpf,email,telefone,data_nascimento
1,João Silva,529.982.247-25,joao@email.com,43999990000,2000-05-12
2,Maria Souza,111.111.111-11,mariaemail.com,43988880000,1999-08-20
3,,123.456.789-00,cliente@email.com,43977770000,2001-01-15
4,João Silva,529.982.247-25,joao@email.com,43999990000,2000-05-12
```

---

## Saída Esperada

O sistema produzirá um relatório estruturado contendo os erros encontrados.

A saída poderá ser exibida no terminal e/ou salva em arquivo `.txt`.

Exemplo de saída textual:

```txt
RELATÓRIO DE VALIDAÇÃO DE CADASTROS

Total de registros analisados: 4
Registros válidos: 1
Registros com erro: 3
Total de inconsistências encontradas: 5

ERROS ENCONTRADOS:

Linha 3
- Campo: cpf
- Erro: CPF inválido
- Valor informado: 111.111.111-11
- Severidade: crítica

Linha 3
- Campo: email
- Erro: E-mail em formato inválido
- Valor informado: mariaemail.com
- Severidade: média

Linha 4
- Campo: nome
- Erro: Campo obrigatório vazio
- Valor informado: vazio
- Severidade: crítica

Linha 5
- Campo: cpf
- Erro: CPF duplicado
- Valor informado: 529.982.247-25
- Severidade: crítica
```

---

## Funcionalidades Iniciais Previstas

### Funcionalidades principais

1. Leitura de arquivo `.csv` contendo dados cadastrais;
2. Validação da existência das colunas obrigatórias;
3. Verificação de campos obrigatórios vazios;
4. Validação de CPF;
5. Validação de e-mail;
6. Identificação de registros duplicados;
7. Geração de relatório final com inconsistências encontradas;
8. Exibição de um resumo quantitativo da qualidade da base analisada.

### Campos inicialmente considerados obrigatórios

- `id`
- `nome`
- `cpf`
- `email`

---

## Justificativa do Escopo

O escopo foi definido para ser pequeno, objetivo e completo. O sistema resolve um problema real de conferência de dados cadastrais, mas evita funcionalidades excessivas que poderiam comprometer a entrega.

A escolha por arquivos `.csv` torna o sistema simples de executar, fácil de testar e compatível com a realidade de usuários que já trabalham com planilhas. A geração de relatório estruturado permite que o resultado seja utilizado diretamente para correção da base.

O projeto prioriza qualidade de engenharia em vez de quantidade de funcionalidades. Por isso, as validações foram escolhidas por representarem problemas comuns em bases cadastrais e por permitirem implementação modular, testes automatizados e documentação clara das decisões técnicas.

---

## Arquitetura Prevista

A arquitetura prevista é uma combinação de **arquitetura em camadas** com um **pipeline de validação**.

A ideia é separar o sistema em responsabilidades principais:

```txt
Entrada CSV
    ↓
Carregamento dos dados
    ↓
Conversão para objetos de domínio
    ↓
Execução da cadeia de validadores
    ↓
Agrupamento dos erros encontrados
    ↓
Geração do relatório final
```

## Padrões de Projeto Previstos

### 1. Chain of Responsibility

O padrão **Chain of Responsibility** será usado para organizar as validações cadastrais.

Cada validador será responsável por uma regra específica, como campos obrigatórios, CPF, e-mail ou duplicidade. Assim, novas validações poderão ser adicionadas sem alterar diretamente as validações já existentes.

Exemplo da cadeia prevista:

```txt
RequiredFieldsValidator
        ↓
CPFValidator
        ↓
EmailValidator
        ↓
DuplicateValidator
```

Esse padrão foi escolhido porque o sistema possui várias regras de validação independentes, que podem crescer futuramente. Separar essas regras reduz acoplamento e facilita manutenção.

### 2. Factory Method

O padrão **Factory Method** será usado para centralizar a criação dos validadores e dos geradores de relatório.

Com isso, o arquivo principal não precisa conhecer todos os detalhes de instanciação dos componentes. Essa decisão facilita manutenção, extensão e substituição de partes do sistema.

Exemplos previstos:

```txt
ValidatorFactory → cria a cadeia/lista de validadores
ReportFactory    → cria o gerador de relatório adequado
```

Esse padrão foi escolhido porque permite modificar a forma como validadores e relatórios são criados sem espalhar essa lógica pelo restante do sistema.

---

## Requisitos Funcionais Iniciais

### RF01 — Carregar arquivo CSV

O sistema deve permitir a leitura de um arquivo `.csv` contendo registros cadastrais.

### RF02 — Validar colunas obrigatórias

O sistema deve identificar se o arquivo de entrada possui as colunas obrigatórias esperadas.

### RF03 — Validar campos obrigatórios

O sistema deve identificar registros com campos obrigatórios vazios.

### RF04 — Validar CPF

O sistema deve identificar CPFs inválidos, incluindo formato incorreto, dígitos verificadores inválidos e CPFs compostos por números repetidos.

### RF05 — Validar e-mail

O sistema deve identificar e-mails em formato inválido.

### RF06 — Identificar registros duplicados

O sistema deve identificar duplicidades, inicialmente com base em CPF e e-mail.

### RF07 — Gerar relatório de inconsistências

O sistema deve gerar um relatório final contendo os erros encontrados, a linha do registro, o campo afetado, o valor informado e o tipo de erro.

### RF08 — Exibir resumo quantitativo

O sistema deve apresentar um resumo com total de registros analisados, registros válidos, registros inválidos e total de inconsistências encontradas.

---

## Requisitos Não Funcionais Iniciais

### RNF01 — Simplicidade de execução

O sistema deve ser executado via terminal, sem necessidade de interface gráfica.

### RNF02 — Modularidade

As regras de validação devem ser separadas em componentes independentes.

### RNF03 — Testabilidade

As principais regras de validação devem possuir testes automatizados.

### RNF04 — Manutenibilidade

O código deve ser organizado para permitir adição futura de novas validações com baixo impacto nos módulos existentes.

### RNF05 — Clareza do relatório

O relatório gerado deve ser compreensível para usuários administrativos, mesmo sem conhecimento técnico.

### RNF06 — Baixo acoplamento

Os módulos do sistema devem depender o mínimo possível uns dos outros, facilitando alterações futuras.

---

## Estratégia de Testes Prevista

Os testes automatizados serão implementados utilizando `unittest`.

Inicialmente, serão testados métodos relevantes dos validadores, como:

- validação de CPF;
- validação de e-mail;
- validação de campos obrigatórios;
- validação de duplicidade.

Para cada função ou método relevante, serão considerados pelo menos três tipos de cenário:

1. Caso de sucesso;
2. Caso de falha ou exceção;
3. Caso de borda.

Exemplo:

```txt
CPFValidator

- Sucesso: CPF válido
- Falha: CPF com dígito verificador incorreto
- Borda: CPF com todos os dígitos iguais
```

---

## Como Executar

A execução prevista será feita pelo terminal.

Exemplo:

```bash
python -m codigo.main dados/cadastros_exemplo.csv
```

Ou, caso seja definido um caminho de saída:

```bash
python -m codigo.main dados/cadastros_exemplo.csv relatorios/relatorio_validacao.txt
```

---

## Como Executar os Testes

Os testes serão executados com `unittest`.

Exemplo:

```bash
python -m unittest discover tests
```

---
