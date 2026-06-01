# Padrões de Codificação e de Gestão / Qualidade

> **Sprint 2: Projeto da Aplicação.** Convenções que a equipe segue para manter o código consistente, legível e sustentável.

## 1. Padrões de Codificação

### Linguagem e estilo
- **Python 3** (compatível com 3.9+), seguindo o guia de estilo **PEP 8**.
- Indentação de **4 espaços** (sem tabs); uma instrução por linha.
- Codificação **UTF-8** em todos os arquivos (o domínio usa acentuação em português).

### Nomenclatura

| Elemento | Convenção | Exemplo |
| --- | --- | --- |
| Módulos e pacotes | `snake_case` | `leitor_csv.py`, `validacao/` |
| Classes | `PascalCase` | `ValidadorCPF`, `ResultadoValidacao` |
| Funções e variáveis | `snake_case` | `criar_cadeia`, `caminho_entrada` |
| Constantes | `UPPER_SNAKE_CASE` | `CAMPOS_OBRIGATORIOS`, `PADRAO` |
| Membros internos | prefixo `_` | `_aplicar`, `_resumo`, `_proximo` |

- **Termos de domínio em português** (`Registro`, `Validador`, `Severidade`) para alinhar o código ao vocabulário do problema.

### Documentação e tipos
- **Docstring** em todo módulo, classe e método público, em português.
- **Type hints** nas assinaturas (`def carregar(self) -> list[Registro]:`), com `from __future__ import annotations` para compatibilidade com Python 3.9.
- Comentários explicam o **porquê**, não o óbvio.

### Organização
- **Um pacote por camada** (`dominio`, `infra`, `validacao`, `relatorio`); arquivos curtos e coesos, com uma responsabilidade principal cada.
- **Imports** ordenados: biblioteca padrão, depois terceiros, depois módulos do projeto; imports absolutos a partir de `codigo.`.
- As dependências apontam das camadas externas para o domínio (o domínio não importa validação nem relatório), preservando o baixo acoplamento.

### Tratamento de erros
- Exceções **específicas e nomeadas** (`ErroLeitura`) em vez de capturar `Exception` genérica.
- Mensagens claras e acionáveis no terminal.
- `main()` devolve **código de saída** `0` (sucesso) ou `1` (erro), padrão de ferramentas de linha de comando.

## 2. Padrões de Gestão / Qualidade

### Fluxo de trabalho (Git)
- Branch `main` sempre funcional; trabalho em **branches por funcionalidade** (ex.: `feat/validador-cpf`).
- **Commits pequenos e descritivos**, no imperativo (ex.: "Adiciona validador de CPF").
- Integração via **Pull Request revisado por outro membro** antes do merge.
- Toda a documentação fica **versionada em `docs/`** (regra da disciplina: links externos não são considerados).

### Definição de Pronto (Definition of Done)
Uma tarefa só está concluída quando:
1. O código segue os padrões acima e roda sem erros;
2. Possui docstring e type hints;
3. A documentação afetada foi atualizada.

### Qualidade e revisão
- **Revisão por pares**: conforme exige a disciplina, qualquer membro deve entender e saber explicar qualquer parte do código.
- **Ferramentas recomendadas** (opcionais): `ruff` ou `flake8` para lint e `black` para formatação, garantindo aderência ao PEP 8.

### Rastreabilidade
- Cada validador referencia, na docstring, o requisito que atende (de RF03 a RF06).
- Cada erro do relatório informa **linha, campo, tipo, valor e severidade**, tornando a saída rastreável até o dado de origem.
