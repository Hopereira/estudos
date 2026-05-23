from database import (
    iniciar_banco, cadastrar_aluno, listar_alunos, atualizar_estilo_aluno, remover_aluno,
    cadastrar_professor, listar_professores, remover_professor,
    realizar_matricula, listar_diario, remover_matricula
)

def menu_principal():
    """Menu principal do sistema"""
    while True:
        print("\n" + "="*50)
        print("  SISTEMA DE GESTÃO - ESCOLA DE DANÇA")
        print("="*50)
        print("📚 GERENCIAMENTO DE ALUNOS")
        print("  1. Cadastrar Novo Aluno")
        print("  2. Listar Todos os Alunos")
        print("  3. Atualizar Estilo de Aluno")
        print("  4. Remover Aluno")
        print("\n👨‍🏫 GERENCIAMENTO DE PROFESSORES")
        print("  5. Cadastrar Novo Professor")
        print("  6. Listar Todos os Professores")
        print("  7. Remover Professor")
        print("\n📝 GERENCIAMENTO DE MATRÍCULAS")
        print("  8. Realizar Matrícula (vincular aluno + professor + estilo)")
        print("  9. Listar Diário de Classe (Aluno | Professor | Estilo)")
        print("  10. Remover Matrícula")
        print("\n0. Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            menu_cadastrar_aluno()
        elif opcao == "2":
            menu_listar_alunos()
        elif opcao == "3":
            menu_atualizar_aluno()
        elif opcao == "4":
            menu_remover_aluno()
        elif opcao == "5":
            menu_cadastrar_professor()
        elif opcao == "6":
            menu_listar_professores()
        elif opcao == "7":
            menu_remover_professor()
        elif opcao == "8":
            menu_realizar_matricula()
        elif opcao == "9":
            menu_listar_diario()
        elif opcao == "10":
            menu_remover_matricula()
        elif opcao == "0":
            print("\n👋 Saindo do sistema... Até logo!")
            break
        else:
            print("\n⚠️ Opção inválida! Tente novamente.")

# ============= MENUS DE ALUNOS =============

def menu_cadastrar_aluno():
    print("\n" + "-"*50)
    print("CADASTRAR NOVO ALUNO")
    print("-"*50)
    nome = input("Nome do Aluno: ").strip()
    estilo = input("Estilo de Dança (ex: Samba, Forró, Balet, etc): ").strip()
    
    resultado = cadastrar_aluno(nome, estilo)
    print(resultado["mensagem"])

def menu_listar_alunos():
    print("\n" + "-"*50)
    print("LISTA DE ALUNOS")
    print("-"*50)
    alunos = listar_alunos()
    
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print(f"\n{'ID':<5} {'Nome':<25} {'Estilo':<20}")
        print("-"*50)
        for aluno in alunos:
            print(f"{aluno[0]:<5} {aluno[1]:<25} {aluno[2]:<20}")

def menu_atualizar_aluno():
    print("\n" + "-"*50)
    print("ATUALIZAR ESTILO DE ALUNO")
    print("-"*50)
    menu_listar_alunos()
    
    try:
        id_aluno = int(input("\nDigite o ID do aluno para atualizar: "))
        novo_estilo = input("Novo Estilo de Dança: ").strip()
        
        if atualizar_estilo_aluno(id_aluno, novo_estilo):
            print(f"🔄 Estilo do aluno ID {id_aluno} atualizado para {novo_estilo}!")
        else:
            print(f"⚠️ ID {id_aluno} não encontrado.")
    except ValueError:
        print("⚠️ ID deve ser um número!")

def menu_remover_aluno():
    print("\n" + "-"*50)
    print("REMOVER ALUNO")
    print("-"*50)
    menu_listar_alunos()
    
    try:
        id_aluno = int(input("\nDigite o ID do aluno para remover: "))
        if remover_aluno(id_aluno):
            print(f"❌ Aluno ID {id_aluno} removido com sucesso.")
        else:
            print(f"⚠️ ID {id_aluno} não encontrado.")
    except ValueError:
        print("⚠️ ID deve ser um número!")

# ============= MENUS DE PROFESSORES =============

def menu_cadastrar_professor():
    print("\n" + "-"*50)
    print("CADASTRAR NOVO PROFESSOR")
    print("-"*50)
    nome = input("Nome do Professor: ").strip()
    especialidade = input("Especialidade (ex: Samba, Forró, Balet, etc): ").strip()
    
    resultado = cadastrar_professor(nome, especialidade)
    print(resultado["mensagem"])

def menu_listar_professores():
    print("\n" + "-"*50)
    print("LISTA DE PROFESSORES")
    print("-"*50)
    professores = listar_professores()
    
    if not professores:
        print("Nenhum professor cadastrado.")
    else:
        print(f"\n{'ID':<5} {'Nome':<25} {'Especialidade':<20}")
        print("-"*50)
        for professor in professores:
            print(f"{professor[0]:<5} {professor[1]:<25} {professor[2]:<20}")

def menu_remover_professor():
    print("\n" + "-"*50)
    print("REMOVER PROFESSOR")
    print("-"*50)
    menu_listar_professores()
    
    try:
        id_professor = int(input("\nDigite o ID do professor para remover: "))
        if remover_professor(id_professor):
            print(f"❌ Professor ID {id_professor} removido com sucesso.")
        else:
            print(f"⚠️ ID {id_professor} não encontrado.")
    except ValueError:
        print("⚠️ ID deve ser um número!")

# ============= MENUS DE MATRÍCULAS =============

def menu_realizar_matricula():
    print("\n" + "-"*50)
    print("REALIZAR MATRÍCULA")
    print("-"*50)
    print("\n📚 ALUNOS DISPONÍVEIS:")
    menu_listar_alunos()
    
    print("\n👨‍🏫 PROFESSORES DISPONÍVEIS:")
    menu_listar_professores()
    
    try:
        id_aluno = int(input("\nDigite o ID do Aluno: "))
        id_professor = int(input("Digite o ID do Professor: "))
        estilo = input("Digite o Estilo de Dança para esta matrícula: ").strip()
        
        resultado = realizar_matricula(id_aluno, id_professor, estilo)
        print(f"\n{resultado['mensagem']}")
    except ValueError:
        print("⚠️ IDs devem ser números!")

def menu_listar_diario():
    print("\n" + "-"*50)
    print("DIÁRIO DE CLASSE - RELATÓRIO COMPLETO")
    print("-"*50)
    
    diario = listar_diario()
    
    if not diario:
        print("Nenhuma matrícula registrada ainda.")
    else:
        print(f"\n{'Nome do Aluno':<25} {'Nome do Professor':<25} {'Estilo':<20}")
        print("-"*70)
        for linha in diario:
            print(f"{linha[0]:<25} {linha[1]:<25} {linha[2]:<20}")

def menu_remover_matricula():
    print("\n" + "-"*50)
    print("REMOVER MATRÍCULA")
    print("-"*50)
    
    menu_listar_diario()
    
    try:
        matricula_id = int(input("\nDigite o ID da matrícula para remover (visualize em Listar Diário): "))
        if remover_matricula(matricula_id):
            print(f"❌ Matrícula ID {matricula_id} removida com sucesso.")
        else:
            print(f"⚠️ ID {matricula_id} não encontrado.")
    except ValueError:
        print("⚠️ ID deve ser um número!")

if __name__ == "__main__":
    iniciar_banco()
    menu_principal()
