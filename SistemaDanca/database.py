import sqlite3

def iniciar_banco():
    conexao = None
    try:
        conexao = sqlite3.connect('escola_danca.db')
        cursor = conexao.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                estilo TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS professores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                materia TEXT NOT NULL,
                estilo_principal TEXT NOT NULL
            )
        ''')
        conexao.commit()
        print("Banco iniciado com sucesso!")

    except sqlite3.Error as e:
        # SEM ESSA PARTE, o programa trava se o arquivo do banco sumir
        print(f"Erro ao configurar o banco: {e}")
    finally:
        if conexao:
            conexao.close()
            print("Conexão encerrada.")

def salvar_aluno(nome, estilo):
    conn = None
    try:
        conn = sqlite3.connect('escola_danca.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO alunos (nome, estilo) VALUES (?, ?)', (nome, estilo))
        conn.commit()
        print("Aluno cadastrado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao salvar aluno: {e}")
    finally:
        if conn:
            conn.close()

def salvar_professor(nome, materia, estilo):
    conn = None
    try:
        conn = obter_conexao() 
        cursor = conn.cursor()
        cursor.execute('INSERT INTO professores (nome, materia, estilo_principal) VALUES (?, ?, ?)', 
                       (nome, materia, estilo))
        conn.commit()
        print("Professor cadastrado com sucesso!")
    except sqlite3.Error as e:
        print(f"❌ Erro ao salvar professor: {e}")
    finally:
        if conn:
            conn.close()

def listar_alunos():
    conn = None
    dados = [] # Garantimos que ela exista para o return no final do try, mesmo que dê erro.
    try:
        conn = sqlite3.connect('escola_danca.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM alunos')
        dados = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erro ao listar: {e}")
    finally:
        if conn:
            conn.close()
    return dados # Retorna os alunos ou a lista vazia se der erro

def listar_professores():
    conn = None
    dados = [] # Garantimos que ela exista para o return no final do try, mesmo que dê erro.
    try:
        conn = sqlite3.connect('escola_danca.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM professores')
        dados = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erro ao listar professores: {e}")
    finally:
        if conn:
            conn.close()
    return dados

def pesquisar_professores(termo):
    conn = None
    dados = []
    try:        
        conn = sqlite3.connect('escola_danca.db')
        cursor = conn.cursor()
        filtro = f"%{termo}%"
        cursor.execute("SELECT * FROM professores WHERE nome LIKE ? OR materia LIKE ? OR estilo_principal LIKE ?", 
                       (filtro, filtro, filtro))
        dados = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erro ao pesquisar professores: {e}")
    finally:
        if conn:
            conn.close()
    return dados

def pesquisar_alunos(termo):
    conn = None
    dados = []
    try:        
        conn = sqlite3.connect('escola_danca.db')
        cursor = conn.cursor()
        filtro = f"%{termo}%"
        cursor.execute("SELECT * FROM alunos WHERE nome LIKE ? OR estilo LIKE ?", (filtro, filtro))
        dados = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erro ao pesquisar alunos: {e}")
    finally:
        if conn:
            conn.close()
    return dados
    

def remover_aluno(id_aluno):
    conn
    try:        
        conn = sqlite3.connect('escola_danca.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM alunos WHERE id = ?', (id_aluno,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao remover aluno: {e}")
    finally:
        if conn:
            conn.close()

def remover_professor(id_professor):
    conn = None
    try:
        conn = sqlite3.connect('escola_danca.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM professores WHERE id = ?', (id_professor,))
        conn.commit()   
    except sqlite3.Error as e:
        print(f"Erro ao remover professor: {e}")
    finally:
        if conn:
            conn.close()

def atualizar_estilo_aluno(id_aluno, novo_estilo):
    conn = None
    try:
        conn = sqlite3.connect('escola_danca.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE alunos SET estilo = ? WHERE id = ?
        ''', (novo_estilo, id_aluno))
        conn.commit()
        print("Estilo atualizado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao atualizar estilo: {e}")
    finally:
        if conn:
            conn.close()
            
def obter_conexao():
    return sqlite3.connect('escola_danca.db')
