import sqlite3

def iniciar_banco():
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
    conexao.close()

def salvar_aluno(nome, estilo):
    conn = sqlite3.connect('escola_danca.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO alunos (nome, estilo) VALUES (?, ?)', (nome, estilo))
    conn.commit()
    conn.close()

def salvar_professor(nome, materia, estilo):
    conn = sqlite3.connect('escola_danca.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO professores (nome, materia, estilo_principal) VALUES (?, ?, ?)', (nome, materia, estilo))
    conn.commit()
    conn.close()

def listar_alunos():
    conn = sqlite3.connect('escola_danca.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alunos')
    dados = cursor.fetchall()
    conn.close()
    return dados

def listar_professores():
    conn = sqlite3.connect('escola_danca.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM professores')
    dados = cursor.fetchall()
    conn.close()
    return dados

def remover_aluno(id_aluno):
    conn = sqlite3.connect('escola_danca.db')
    cursor = conn.cursor()
    # O comando DELETE remove a linha inteira baseada no ID
    cursor.execute('DELETE FROM alunos WHERE id = ?', (id_aluno,))
    conn.commit()
    conn.close()

def remover_professor(id_professor):
    conn = sqlite3.connect('escola_danca.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM professores WHERE id = ?', (id_professor,))
    conn.commit()
    conn.close()

def atualizar_estilo_aluno(id_aluno, novo_estilo):
    conn = sqlite3.connect('escola_danca.db')
    cursor = conn.cursor()
    # O comando UPDATE altera um valor específico onde o ID for igual ao informado
    cursor.execute('''
        UPDATE alunos 
        SET estilo = ? 
        WHERE id = ?
    ''', (novo_estilo, id_aluno))
    conn.commit()
    conn.close()