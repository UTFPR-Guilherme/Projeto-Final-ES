# Requisitos

> **Sprint 1: Engenharia de Requisitos.**

## 1. Pitch do Problema

Pequenas empresas, escolas, cursos e setores administrativos mantêm cadastros de clientes, alunos e participantes em planilhas, muitas vezes preenchidas à mão ou importadas de fontes diferentes. Essas bases acumulam CPFs inválidos, e-mails incorretos, campos obrigatórios vazios e registros duplicados, e a conferência costuma ser feita manualmente, linha a linha.

O problema é real e relevante:

- A Experian, em sua pesquisa de gestão de dados, aponta que as organizações consideram cerca de **um terço dos seus dados cadastrais imprecisos** (32% em 2015).
- O estudo da Harvard Business Review (Nagle, Redman e Sammon, 2017) constatou que **apenas 3% das bases atendem a padrões básicos de qualidade** e que **47% dos registros recém-criados têm ao menos um erro crítico**.
- A Gartner estima que a má qualidade de dados custa, em média, **US$ 12,9 milhões por ano** por organização.

Para o público-alvo do ValidaCad, esse esforço manual é lento e sujeito a falhas. O sistema automatiza a verificação das inconsistências mais comuns (campos obrigatórios, CPF, e-mail e duplicidade) e entrega um relatório claro e rastreável, permitindo corrigir a base antes de usá-la ou importá-la para outro sistema.

## 2. Fontes

1. Nagle, T.; Redman, T.; Sammon, D. **"Only 3% of Companies' Data Meets Basic Quality Standards."** Harvard Business Review, set. 2017. Sustenta a prevalência de erros: só 3% das bases atendem a padrões básicos e 47% dos novos registros têm erro crítico. [hbr.org](https://hbr.org/2017/09/only-3-of-companies-data-meets-basic-quality-standards)
2. **Experian, Global Data Management / Data Quality research.** Sustenta que cerca de um terço dos dados cadastrais é considerado impreciso pelas próprias organizações. [experianplc.com](https://www.experianplc.com/newsroom/press-releases/2015/new-experian-data-quality-research-shows-inaccurate-data-preventing-desired-customer-insight)
3. **Gartner, "Data Quality: Why It Matters and How to Achieve It."** Sustenta o custo da má qualidade de dados (média de US$ 12,9 milhões por ano). [gartner.com](https://www.gartner.com/en/data-analytics/topics/data-quality)

> As três fontes são reais e devem ser lidas pela equipe: na review, qualquer membro precisa saber explicar o que cada uma sustenta.

## 3. Elicitação

**Método adotado: análise de similares** (comparação com soluções já existentes), por ser viável no tempo da sprint e adequado a um público amplo.

Soluções analisadas e o que aprendemos:

- **Validadores de CPF online:** validam um documento por vez, sem tratar a base inteira nem outras regras (e-mail, duplicidade).
- **Recurso de "validação de dados" do Excel e do Google Sheets:** exige configuração manual por coluna e não valida CPF nem duplicidade de forma automática.
- **Bibliotecas Python de documentos brasileiros (ex.: validate-docbr):** confirmam o algoritmo de validação de CPF por dígitos verificadores.
- **Ferramentas de deduplicação de CRM:** confirmam que registros duplicados são um problema recorrente nas bases.

**Síntese:** o público administrativo precisa de uma ferramenta automática e simples (terminal, CSV) que cubra, em uma única execução, campos obrigatórios, CPF, e-mail e duplicidade, gerando um relatório rastreável. As soluções avulsas (validar um CPF por vez, conferir a planilha manualmente) não preenchem essa lacuna.

## 4. Histórias de Usuário

Formato: "Como [perfil], quero [ação], para [benefício]", com critérios de aceitação e prioridade (MoSCoW).

**HU01 (Carregar base).** Como usuário administrativo, quero carregar um arquivo CSV de cadastros, para validar a base sem conferência manual.
- Dado um arquivo CSV existente, quando executo o sistema, então os registros são carregados para validação.
- Dado um arquivo inexistente, quando executo o sistema, então recebo uma mensagem de erro clara e o programa encerra sem quebrar.
- Prioridade: Must.

**HU02 (Conferir colunas).** Como usuário, quero que o sistema verifique as colunas esperadas, para saber se o arquivo está no formato certo.
- Dado um CSV com as colunas id, nome, cpf e email, quando carregado, então a validação prossegue normalmente.
- Dado um CSV sem uma coluna obrigatória, quando carregado, então os valores ausentes são tratados como vazios e sinalizados.
- Prioridade: Should.

**HU03 (Campos obrigatórios).** Como usuário, quero identificar registros com campos obrigatórios vazios, para corrigir cadastros incompletos.
- Dado um registro com nome vazio, quando validado, então é gerado um erro "Campo obrigatório vazio" com a linha e o campo.
- Dado um campo preenchido só com espaços, quando validado, então também é considerado vazio.
- Prioridade: Must.

**HU04 (CPF).** Como usuário, quero detectar CPFs inválidos, para garantir documentos válidos na base.
- Dado um CPF com dígito verificador incorreto, quando validado, então é sinalizado como "CPF inválido" (severidade crítica).
- Dado um CPF com todos os dígitos iguais, quando validado, então é sinalizado como inválido.
- Dado um CPF válido (com ou sem pontuação), quando validado, então não gera erro.
- Prioridade: Must.

**HU05 (E-mail).** Como usuário, quero detectar e-mails em formato inválido, para garantir um canal de contato válido.
- Dado um e-mail sem "@" ou sem domínio, quando validado, então é sinalizado como "E-mail em formato inválido" (severidade média).
- Dado um e-mail bem formado, quando validado, então não gera erro.
- Prioridade: Must.

**HU06 (Duplicados).** Como usuário, quero identificar registros duplicados, para evitar cadastros repetidos.
- Dado dois registros com o mesmo CPF, quando validados, então a segunda ocorrência é sinalizada como "CPF duplicado".
- Dado dois registros com o mesmo e-mail, quando validados, então a segunda ocorrência é sinalizada como "E-mail duplicado".
- Prioridade: Should.

**HU07 (Relatório).** Como usuário, quero um relatório com os erros encontrados, para localizar e corrigir rapidamente.
- Dado que existem inconsistências, quando o relatório é gerado, então cada erro lista linha, campo, valor informado, tipo e severidade.
- Dado que não há inconsistências, quando o relatório é gerado, então ele informa que a base está íntegra.
- Prioridade: Must.

**HU08 (Resumo).** Como usuário, quero um resumo quantitativo da base, para ter uma visão geral da qualidade.
- Dado um conjunto de registros, quando o relatório é gerado, então exibe total analisado, válidos, com erro e total de inconsistências.
- Prioridade: Should.

## 5. Priorização (MoSCoW)

| Prioridade | Histórias | Justificativa |
| --- | --- | --- |
| Must (essencial) | HU01, HU03, HU04, HU05, HU07 | Núcleo do produto: carregar, validar as regras principais e relatar |
| Should (importante) | HU02, HU06, HU08 | Agregam valor e robustez, mas o MVP funciona sem elas |
| Could (futuro) | Validar telefone e data de nascimento | Fora do MVP; avaliados em sprints futuras |
| Won't (agora) | Suporte a xlsx, interface gráfica | Fora do escopo definido para a disciplina |

## 6. Requisitos Funcionais

### RF01: Carregar arquivo CSV
O sistema deve permitir a leitura de um arquivo `.csv` contendo registros cadastrais.

### RF02: Validar colunas obrigatórias
O sistema deve identificar se o arquivo de entrada possui as colunas obrigatórias esperadas.

### RF03: Validar campos obrigatórios
O sistema deve identificar registros com campos obrigatórios vazios.

### RF04: Validar CPF
O sistema deve identificar CPFs inválidos, incluindo formato incorreto, dígitos verificadores inválidos e CPFs compostos por números repetidos.

### RF05: Validar e-mail
O sistema deve identificar e-mails em formato inválido.

### RF06: Identificar registros duplicados
O sistema deve identificar duplicidades, inicialmente com base em CPF e e-mail.

### RF07: Gerar relatório de inconsistências
O sistema deve gerar um relatório final contendo os erros encontrados: a linha do registro, o campo afetado, o valor informado e o tipo de erro.

### RF08: Exibir resumo quantitativo
O sistema deve apresentar um resumo com total de registros analisados, registros válidos, registros inválidos e total de inconsistências encontradas.

### Campos inicialmente considerados obrigatórios
`id`, `nome`, `cpf`, `email`.

## 7. Requisitos Não Funcionais

- **RNF01 (Simplicidade de execução):** executado via terminal, sem interface gráfica.
- **RNF02 (Modularidade):** regras de validação separadas em componentes independentes.
- **RNF03 (Testabilidade):** principais regras de validação cobertas por testes automatizados.
- **RNF04 (Manutenibilidade):** código organizado para permitir a adição de novas validações com baixo impacto.
- **RNF05 (Clareza do relatório):** relatório compreensível para usuários administrativos, mesmo sem conhecimento técnico.
- **RNF06 (Baixo acoplamento):** módulos com o mínimo de dependência entre si.

## 8. Registro de Validação

### Ambiguidades encontradas e resolução
- "Campo vazio" inclui campos só com espaços? Resolução: sim, espaços em branco contam como vazio (tratado com `strip()`).
- "CPF" deve ser aceito com pontuação (529.982.247-25) e sem (52998224725)? Resolução: ambos; a validação normaliza para apenas dígitos.
- "Registro duplicado" por qual critério? Resolução: por CPF e por e-mail, separadamente; a primeira ocorrência é mantida e as seguintes são sinalizadas.

### Conflitos identificados e resolução
- As colunas telefone e data_nascimento aparecem no exemplo, mas havia dúvida se seriam validadas. Resolução: ficam fora do escopo inicial; obrigatórios apenas id, nome, cpf e email.
- Severidade do e-mail inválido: crítica ou média? Resolução: média (reduz a qualidade do contato, mas não invalida o cadastro), enquanto CPF inválido e duplicidade são críticos.

### Questões em aberto
- Validar também telefone e data de nascimento (formato e plausibilidade)?
- Detectar duplicidade considerando o nome normalizado, além de CPF e e-mail?
- Suportar outros formatos de entrada (xlsx) e outras codificações além de UTF-8?
- Permitir configurar, por execução, quais colunas são obrigatórias?

## 9. Entrada e Saída Esperadas

### Entrada
Arquivo `.csv` com dados cadastrais. Exemplo:

```csv
id,nome,cpf,email,telefone,data_nascimento
1,João Silva,529.982.247-25,joao@email.com,43999990000,2000-05-12
2,Maria Souza,111.111.111-11,mariaemail.com,43988880000,1999-08-20
3,,123.456.789-00,cliente@email.com,43977770000,2001-01-15
4,João Silva,529.982.247-25,joao@email.com,43999990000,2000-05-12
```

### Saída
Relatório estruturado, exibido no terminal e/ou salvo em `.txt`. Exemplo:

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
```
