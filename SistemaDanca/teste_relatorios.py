#!/usr/bin/env python3
"""Script de teste para as funções de relatório"""

import database

# Inicializar banco
database.iniciar_banco()

print("\n=== TESTE DAS FUNÇÕES DE RELATÓRIO ===\n")

# Teste 1: Resumo por Estilo
print("1️⃣  Testando resumo_por_estilo():")
estilo_data = database.resumo_por_estilo()
print(f"   Retornou {len(estilo_data)} registros")
if estilo_data:
    for estilo, total in estilo_data:
        print(f"   ✓ {estilo}: {total} alunos")
else:
    print("   ℹ️  Sem dados - adicione alunos primeiro")

# Teste 2: Alunos por Professor
print("\n2️⃣  Testando alunos_por_professor():")
prof_data = database.alunos_por_professor()
print(f"   Retornou {len(prof_data)} professores")
if prof_data:
    for id_prof, nome, total in prof_data:
        print(f"   ✓ {nome}: {total} alunos")
else:
    print("   ℹ️  Sem dados - matricule alunos primeiro")

# Teste 3: Professores por Matéria
print("\n3️⃣  Testando relatorio_professores_por_materia():")
materia_data = database.relatorio_professores_por_materia()
print(f"   Retornou {len(materia_data)} registros")
if materia_data:
    for materia, total in materia_data:
        print(f"   ✓ {materia}: {total} professores")
else:
    print("   ℹ️  Sem dados - adicione professores primeiro")

# Teste 4: Alunos por Professor (detalhado)
print("\n4️⃣  Testando relatorio_alunos_por_professor():")
aluno_prof_data = database.relatorio_alunos_por_professor()
print(f"   Retornou {len(aluno_prof_data)} registros")
if aluno_prof_data:
    for prof, aluno, estilo in aluno_prof_data:
        print(f"   ✓ {prof} -> {aluno} ({estilo})")
else:
    print("   ℹ️  Sem matrículas - realize matrículas primeiro")

print("\n✅ Testes concluídos!")
