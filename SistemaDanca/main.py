import database

def menu_alunos():
    while True:
        print("\n--- GESTÃO DE ALUNOS ---")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Remover Aluno")
        print("4. Atualizar Estilo")  # <--- Nova opção!
        print("0. Voltar")
        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            estilo = input("Estilo: ")
            try    :
                database.salvar_aluno(nome, estilo)
                print("✅ Aluno cadastrado!")
            except database as e:
                print(f"❌ Erro ao cadastrar aluno: {e}")
        
        elif op == "2":
            alunos = database.listar_alunos()
            for a in alunos:
                print(f"ID: {a[0]} | Nome: {a[1]} | Estilo: {a[2]}")
        
        elif op == "3":
            id_remover = input("ID do aluno para remover: ")
            database.remover_aluno(id_remover)
            print("❌ Removido!")

        elif op == "4":  # <--- A lógica para chamar o seu update
            id_aluno = input("Digite o ID do aluno: ")
            novo_estilo = input("Digite o novo estilo: ")
            database.atualizar_estilo_aluno(id_aluno, novo_estilo)
            print("🔄 Estilo atualizado!")
            
        elif op == "0":
            break

def menu_professores():
    while True:
        print("\n--- GESTÃO DE PROFESSORES ---")
        print("1. Cadastrar Professor")
        print("2. Listar Professores")
        print("3. Remover Professor")
        print("0. Voltar")
        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            materia = input("Matéria: ")
            estilo = input("Estilo Principal: ")
            database.salvar_professor(nome, materia, estilo)
            print("✅ Professor cadastrado!")

        elif op == "2":
            profs = database.listar_professores()
            print("\n--- LISTA DE PROFESSORES ---")
            for p in profs:
                print(f"ID: {p[0]} | Nome: {p[1]} | Matéria: {p[2]}")

        elif op == "3":
            id_remover = input("Digite o ID do professor para remover: ")
            database.remover_professor(id_remover)
            print("❌ Professor removido!")
            
        elif op == "4": # Opção para atualizar
            id_aluno = input("Digite o ID do aluno para atualizar: ")
            novo_estilo = input("Digite o novo estilo de dança: ")
            database.atualizar_estilo_aluno(id_aluno, novo_estilo)
            print("🔄 Estilo atualizado com sucesso!")

        elif op == "0":
            break

def menu_principal():
    database.iniciar_banco()
    while True:
        print("\n=== SISTEMA ESCOLA DE DANÇA ===")
        print("1. Gerenciar Alunos")
        print("2. Gerenciar Professores")
        print("0. Sair")
        opcao = input("Escolha: ")
        
        if opcao == "1":
            menu_alunos()
        elif opcao == "2":
            menu_professores()
        elif opcao == "0":
            print("Saindo...")
            break

if __name__ == "__main__":
    menu_principal()
    
try:
    id_aluno = int(input("Digite o ID do aluno: "))
    id_prof = int(input("Digite o ID do professor: "))
    
    # Chama a função que está no outro arquivo
    vincular_aluno(id_aluno, id_prof) 

except ValueError:
    print("Erro: Você precisa digitar um NÚMERO inteiro para o ID.")