import database

def menu_alunos():
    while True:
        print("\n--- GESTÃO DE ALUNOS ---")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Remover Aluno")
        print("4. Atualizar Estilo")
        print("5. Pesquisar Alunos")
        print("0. Voltar")
        
        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            try:
                if not nome.replace(" ", "").isalpha():
                    raise ValueError("O nome do aluno deve conter apenas letras e espaços.")
            except ValueError as e:
                print(f"❌ Erro: {e}")
                continue
            
            estilo = input("Estilo: ")
            try:
                database.salvar_aluno(nome, estilo)
                print("✅ Aluno cadastrado!")
            except database.AlunoDuplicadoError as e:
                print(f"⚠️ {e}")
        
        elif op == "2":
            alunos = database.listar_alunos()
            for a in alunos:
                print(f"ID: {a[0]} | Nome: {a[1]} | Estilo: {a[2]}")
        
        elif op == "3":
            id_remover = input("ID do aluno para remover: ")
            try:
                if not id_remover.isdigit():
                    raise ValueError("O ID deve ser um número inteiro.")
            except ValueError as e:
                print(f"❌ Erro: {e}")
                continue
            database.remover_aluno(id_remover)
            print("Removido!")

        elif op == "4":  # Atualizar estilo do aluno
            id_aluno = input("Digite o ID do aluno: ")
            try:
                if not id_aluno.isdigit():
                    raise ValueError("O ID deve ser um número inteiro.")
            except ValueError as e:
                print(f"Erro: {e}")
                continue

            novo_estilo = input("Digite o novo estilo: ")
            try:
                if not novo_estilo.replace(" ", "").isalpha():
                    raise ValueError("O estilo de dança deve conter apenas letras e espaços.")
            except ValueError as e:
                print(f"Erro: {e}")
                continue
            database.atualizar_estilo_aluno(id_aluno, novo_estilo)
            print("Estilo atualizado!")

        elif op == "5":
            termo_pesquisa = input("Digite o termo para pesquisa: ")
            try:
                if not termo_pesquisa.replace(" ", "").isalpha():
                    raise ValueError("O termo de pesquisa deve conter apenas letras e espaços.")
            except ValueError as e:
                print(f"Erro: {e}")
                continue
            resultados = database.pesquisar_alunos(termo_pesquisa)
            if resultados:
                print("\n--- RESULTADOS DA PESQUISA ---")
                for r in resultados:
                    print(f"ID: {r[0]} | Nome: {r[1]} | Estilo: {r[2]}")
            else:
                print("Nenhum aluno encontrado.")

        elif op == "0":
            break

def menu_professores():
    while True:
        print("\n--- GESTÃO DE PROFESSORES ---")
        print("1. Cadastrar Professor")
        print("2. Listar Professores")
        print("3. Remover Professor")
        print("4. Atualizar Estilo do Aluno")
        print("5. Pesquisar Professores")
        print("0. Voltar")
        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            try:
                if not nome.replace(" ", "").isalpha():
                    raise ValueError("O nome do professor deve conter apenas letras e espaços.")
            except ValueError as e:
                print(f" Erro: {e}")
                continue
            materia = input("Matéria: ")
            try:
                if not materia.replace(" ", "").isalpha():
                    raise ValueError("A matéria deve conter apenas letras e espaços.")
            except ValueError as e:
                print(f" Erro: {e}")
                continue
            
            estilo = input("Estilo Principal: ")
            try:
                if not estilo.replace(" ", "").isalpha():
                    raise ValueError("O estilo de dança deve conter apenas letras e espaços.")
            except ValueError as e:
                print(f" Erro: {e}")
                continue
            database.salvar_professor(nome, materia, estilo)
            print("✅ Professor cadastrado!")

        elif op == "2":
            profs = database.listar_professores()
            print("\n--- LISTA DE PROFESSORES ---")
            for p in profs:
                print(f"ID: {p[0]} | Nome: {p[1]} | Matéria: {p[2]}")

        elif op == "3":
            id_remover = input("Digite o ID do professor para remover: ")
            try:
                if not id_remover.isdigit():
                    raise ValueError("O ID deve ser um número inteiro.")
            except ValueError as e:
                print(f" Erro: {e}")
                continue
            database.remover_professor(id_remover)
            print("❌ Professor removido!")
            
        elif op == "4": # Opção para atualizar
            id_aluno = input("Digite o ID do aluno para atualizar: ")
            novo_estilo = input("Digite o novo estilo de dança: ")
            try:
                if not novo_estilo.replace(" ", "").isalpha():
                    raise ValueError("O estilo de dança deve conter apenas letras e espaços.")
            except ValueError as e:
                print(f" Erro: {e}")
                continue
            database.atualizar_estilo_aluno(id_aluno, novo_estilo)
            print("🔄 Estilo atualizado com sucesso!")
            
        elif op == "5":
            termo_pesquisa = input("Digite o termo para pesquisa: ")
            try:
                if not termo_pesquisa.replace(" ", "").isalpha():
                    raise ValueError("O termo de pesquisa deve conter apenas letras e espaços.")    
            except ValueError as e:
                print(f" Erro: {e}")
                continue
            resultados = database.pesquisar_professores(termo_pesquisa)
            if resultados:
                print("\n--- RESULTADOS DA PESQUISA ---")
                for r in resultados:
                    print(f"ID: {r[0]} | Nome: {r[1]} | Matéria: {r[2]} | Estilo Principal: {r[3]}")
            else:
                print("Nenhum professor encontrado.")

        elif op == "0":
            break

def menu_principal():
    database.iniciar_banco()
    while True:
        print("\n=== SISTEMA ESCOLA DE DANÇA ===")
        print("1. Gerenciar Alunos")
        print("2. Gerenciar Professores")
        print("3. Relatórios Gerenciais")
        print("0. Sair")
        opcao = input("Escolha uma das opções: ")
        try:            
            if opcao not in ["0", "1", "2", "3"]:
                raise ValueError("Opção inválida. Por favor, escolha uma opção válida.")
        except ValueError as e:
            print(f"Erro: {e}")
            continue    
        
        if opcao == "1":
            menu_alunos()
        elif opcao == "2":
            menu_professores()
            
        elif opcao == "3":
            menu_relatorios()
            
        elif opcao == "0":
            print("Saindo...")
            break

def menu_relatorios():
    """Menu de Relatórios Gerenciais - BI do Sistema"""
    while True:
        print("\n=== RELATÓRIOS GERENCIAIS ===")
        print("1. 📊 Total de Alunos por Estilo")
        print("2. 👨‍🏫 Total de Professores por Matéria")
        print("3. 👥 Alunos por Professor")
        print("4. 📈 Resumo Executivo")
        print("0. ⬅️  Voltar")
        
        relatorio_op = input("\nEscolha um relatório: ")

        try:
            if relatorio_op == "1":
                dados = database.relatorio_alunos_por_estilo()
                if dados:
                    print("\n--- 📊 TOTAL DE ALUNOS POR ESTILO ---")
                    total_geral = 0
                    for estilo, total in dados:
                        print(f"  {estilo.upper()}: {total} alunos")
                        total_geral += total
                    print(f"\n  ✅ Total de Alunos: {total_geral}")
                else:
                    print("❌ Nenhum dado disponível.")

            elif relatorio_op == "2":
                dados = database.relatorio_professores_por_materia()
                if dados:
                    print("\n--- 👨‍🏫 TOTAL DE PROFESSORES POR MATÉRIA ---")
                    total_professores = 0
                    for materia, total in dados:
                        print(f"  {materia.upper()}: {total} professor(es)")
                        total_professores += total
                    print(f"\n  ✅ Total de Professores: {total_professores}")
                else:
                    print("❌ Nenhum dado disponível.")

            elif relatorio_op == "3":
                dados = database.relatorio_alunos_por_professor()
                if dados:
                    print("\n--- 👥 ALUNOS POR PROFESSOR ---")
                    professor_atual = None
                    contador = 0
                    for professor, aluno, estilo in dados:
                        if professor_atual != professor:
                            if professor_atual is not None:
                                print()
                            professor_atual = professor
                            contador = 1
                            print(f"\n  📌 Professor: {professor}")
                        print(f"     {contador}. {aluno} ({estilo})")
                        contador += 1
                else:
                    print("❌ Nenhuma matrícula registrada ainda.")

            elif relatorio_op == "4":
                print("\n--- 📈 RESUMO EXECUTIVO ---")
                
                # Total de alunos
                alunos = database.listar_alunos()
                total_alunos = len(alunos)
                
                # Total de professores
                professores = database.listar_professores()
                total_professores = len(professores)
                
                # Distribuição por estilo
                estilo_dados = database.resumo_por_estilo()
                
                # Distribuição por professor
                prof_dados = database.alunos_por_professor()
                
                print(f"\n  📊 MÉTRICAS GERAIS:")
                print(f"     • Total de Alunos: {total_alunos}")
                print(f"     • Total de Professores: {total_professores}")
                print(f"     • Estilos Cadastrados: {len(estilo_dados)}")
                
                if estilo_dados:
                    estilo_top = max(estilo_dados, key=lambda x: x[1])
                    print(f"     • Estilo Mais Popular: {estilo_top[0]} ({estilo_top[1]} alunos)")
                
                if prof_dados:
                    prof_top = max(prof_dados, key=lambda x: x[2])
                    print(f"     • Professor com Mais Alunos: {prof_top[1]} ({prof_top[2]} alunos)")
                
                print()

            elif relatorio_op == "0":
                break
            else:
                print("❌ Opção inválida!")
                
        except Exception as e:
            print(f"❌ Erro ao gerar relatório: {e}")
        
        input("\n(Pressione ENTER para continuar...)")

if __name__ == "__main__":
    menu_principal()