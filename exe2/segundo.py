import sqlite3

def iniciar_banco():
    conexao = sqlite3.connect('escola_danca.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            materia TEXT NOT NULL,
            estilo_principal TEXT NOT NULL
        )
    ''')
    conexao.commit()
    return conexao

def menu():
    while True:
        print("\n" + "="*30)
        print("  SISTEMA DE GESTÃO DE PROFESSORES")
        print("="*30)
        print("1. Cadastrar Novo Professor")
        print("2. Listar Todos os Professores")
        print("3. Atualizar Estilo Principal de Professor")
        print("4. Remover Professor")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        conn = iniciar_banco()
        cursor = conn.cursor()

        if opcao == "1":
            materia = input("Matéria do Professor: ")
            estilo_principal = input("Estilo Principal de Dança: ")
            cursor.execute('INSERT INTO professores (materia, estilo_principal) VALUES (?, ?)', (materia, estilo_principal))
            conn.commit()
            print(f"✅ Professor de {materia} adicionado!")

        elif opcao == "2":
            cursor.execute('SELECT * FROM professores')
            rows = cursor.fetchall()
            print("\n--- LISTA DE PROFESSORES ---")
            for r in rows:
                print(f"ID: {r[0]} | Matéria: {r[1]} | Estilo Principal: {r[2]}")

        elif opcao == "3":
            id_professor = input("Digite o ID do professor para atualizar: ")
            novo_estilo_principal = input("Novo Estilo Principal: ")
            cursor.execute('UPDATE professores SET estilo_principal = ? WHERE id = ?', (novo_estilo_principal, id_professor))
            conn.commit()
            print("🔄 Dados atualizados!")

        elif opcao == "4":
            id_professor = input("Digite o ID do professor para remover: ")
            cursor.execute('DELETE FROM professores WHERE id = ?', (id_professor,))
            conn.commit()
            print("❌ Professor removido com sucesso.")

        elif opcao == "0":
            print("Saindo do sistema... Até logo!")
            conn.close()
            break
        
        if __name__ == "__main__":
            menu()