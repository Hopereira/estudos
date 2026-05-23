# 📊 Sistema de Relatórios Gerenciais - SistemaDança BI

## 📋 Descrição

Sistema de inteligência de negócios (BI) implementado para o **SistemaDança**, que permite ao gestor visualizar análises estratégicas sobre:
- Volume de alunos por modalidade de dança
- Distribuição de professores por matéria
- Matrículas e relacionamento aluno-professor
- Resumo executivo com métricas-chave

---

## ✅ Funcionalidades Implementadas

### 1️⃣ **Função: `resumo_por_estilo()`**
- **Localização**: `database.py`
- **SQL**: `GROUP BY estilo`
- **Retorno**: Lista de tuplas `(estilo, total_alunos)`
- **Descrição**: Agrupa alunos por estilo de dança e conta o total

```python
dados = database.resumo_por_estilo()
# Retorno: [('Forró', 5), ('Samba', 3), ('Pagode', 2)]
```

---

### 2️⃣ **Função: `alunos_por_professor()`**
- **Localização**: `database.py`
- **SQL**: `LEFT JOIN matriculas` + `GROUP BY professores.id`
- **Retorno**: Lista de tuplas `(id_professor, nome_professor, total_alunos)`
- **Descrição**: Relaciona cada professor com a quantidade de alunos vinculados

```python
dados = database.alunos_por_professor()
# Retorno: [(1, 'Maria Silva', 8), (2, 'João Santos', 5), (3, 'Ana Costa', 0)]
```

---

### 3️⃣ **Função: `relatorio_professores_por_materia()`**
- **Localização**: `database.py`
- **SQL**: `GROUP BY materia`
- **Retorno**: Lista de tuplas `(materia, total_professores)`
- **Descrição**: Agrupa professores por matéria de ensino

```python
dados = database.relatorio_professores_por_materia()
# Retorno: [('Dança Contemporânea', 2), ('Balé', 3), ('Ritmos Brasileiros', 1)]
```

---

### 4️⃣ **Função: `relatorio_alunos_por_professor()`**
- **Localização**: `database.py`
- **SQL**: `JOIN profesores` + `JOIN alunos`
- **Retorno**: Lista de tuplas `(professor, aluno, estilo_escolhido)`
- **Descrição**: Relatório detalhado com nome do aluno, professor e estilo

```python
dados = database.relatorio_alunos_por_professor()
# Retorno: [('Maria Silva', 'João Pedro', 'Samba'), ...]
```

---

## 🎯 Menu de Relatórios Gerenciais

Acessível via **opção 3** do menu principal:

```
=== RELATÓRIOS GERENCIAIS ===
1.  Total de Alunos por Estilo
2.  Total de Professores por Matéria
3.  Alunos por Professor
4.  Resumo Executivo
0.  Voltar
```

### Relatório 1: Alunos por Estilo
Mostra o volume de alunos distribuído por cada modalidade de dança.

### Relatório 2: Professores por Matéria
Exibe quantidade de instrutores para cada disciplina.

### Relatório 3: Alunos por Professor
Lista detalhada de todos os alunos vinculados a cada professor com estilo escolhido.

### Relatório 4: Resumo Executivo
Dashboard com métricas consolidadas:
- Total de alunos no sistema
- Total de professores
- Quantidade de estilos cadastrados
- Estilo mais popular
- Professor com mais alunos

---

## 📊 Exemplos de Saída

### Exemplo 1: Total de Alunos por Estilo
```
---  TOTAL DE ALUNOS POR ESTILO ---
  SAMBA: 5 alunos
  FORRÓ: 3 alunos
  PAGODE: 2 alunos
  ✅ Total de Alunos: 10
```

### Exemplo 2: Alunos por Professor
```
--- ALUNOS POR PROFESSOR ---
  📌 Professor: Maria Silva
     1. João Pedro (Samba)
     2. Ana Santos (Pagode)
     3. Carlos Oliveira (Samba)
  
  📌 Professor: João Santos
     1. Fernanda Costa (Forró)
```

### Exemplo 3: Resumo Executivo
```
--- RESUMO EXECUTIVO ---
    MÉTRICAS GERAIS:
     • Total de Alunos: 12
     • Total de Professores: 4
     • Estilos Cadastrados: 3
     • Estilo Mais Popular: Samba (5 alunos)
     • Professor com Mais Alunos: Maria Silva (5 alunos)
```

---

## 🔧 Estrutura de Dados

### Tabelas Utilizadas

**`alunos`**
```sql
id (PK) | nome | estilo
```

**`professores`**
```sql
id (PK) | nome | materia | estilo_principal
```

**`matriculas`**
```sql
id (PK) | id_aluno (FK) | id_professor (FK) | estilo_escolhido | data_matricula
```

---

## 🧪 Teste das Funcionalidades

Execute o script de teste para validar todas as funções:

```bash
python teste_relatorios.py
```


