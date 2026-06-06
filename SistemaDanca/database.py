import sqlite3

class AlunoDuplicadoError(Exception):
    pass

def iniciar_banco():
    conexao = None
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        
        # Criação das tabelas principais
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
        
        # Chama a criação da tabela de matrículas
        criar_tabelas()
        
        print("Banco iniciado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao configurar o banco: {e}")
    finally:
        if conexao:
            conexao.close()
            

def criar_tabelas():
    conexao = None
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS matriculas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_aluno INTEGER NOT NULL,
                id_professor INTEGER NOT NULL,
                estilo_escolhido TEXT NOT NULL,
                data_matricula TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (id_aluno) REFERENCES alunos(id) ON DELETE CASCADE,
                FOREIGN KEY (id_professor) REFERENCES professores(id) ON DELETE CASCADE
            )
        ''')
        conexao.commit()
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela de matrículas: {e}")
    finally:
        if conexao:
            conexao.close()

# --- FUNÇÕES DE ALUNOS ---

def salvar_aluno(nome, estilo):
    # Corrigido para usar obter_conexao() para manter o padrão e evitar conflitos
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM alunos WHERE LOWER(nome) = LOWER(?)', (nome,))
    if cursor.fetchone() is not None:
        conn.close()
        raise AlunoDuplicadoError(f"Aluno '{nome}' ja esta cadastrado.")
    cursor.execute('INSERT INTO alunos (nome, estilo) VALUES (?, ?)', (nome, estilo))
    conn.commit()
    conn.close()

def listar_alunos():
    conn = None
    dados = []
    try:
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM alunos')
        dados = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erro ao listar: {e}")
    finally:
        if conn:
            conn.close()
    return dados

def pesquisar_alunos(termo):
    conn = None
    dados = []
    try:        
        conn = obter_conexao()
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
    conn = None  
    try:        
        conn = obter_conexao() 
        cursor = conn.cursor()
        cursor.execute('DELETE FROM alunos WHERE id = ?', (id_aluno,))
        conn.commit()
        print("❌ Aluno removido!")
    except sqlite3.Error as e:
        print(f"Erro ao remover aluno: {e}")
    finally:
        if conn:
            conn.close()

def atualizar_estilo_aluno(id_aluno, novo_estilo):
    conn = None
    try:
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute('UPDATE alunos SET estilo = ? WHERE id = ?', (novo_estilo, id_aluno))
        conn.commit()
        print("🔄 Estilo atualizado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao atualizar estilo: {e}")
    finally:
        if conn:
            conn.close()

# --- FUNÇÕES DE PROFESSORES ---

def salvar_professor(nome, materia, estilo):
    conn = None
    try:
        conn = obter_conexao() 
        cursor = conn.cursor()
        cursor.execute('INSERT INTO professores (nome, materia, estilo_principal) VALUES (?, ?, ?)', 
                       (nome, materia, estilo))
        conn.commit()
        print("✅ Professor cadastrado com sucesso!")
    except sqlite3.Error as e:
        print(f"❌ Erro ao salvar professor: {e}")
    finally:
        if conn:
            conn.close()

def listar_professores():
    conn = None
    dados = []
    try:
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM professores')
        dados = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erro ao listar professores: {e}")
    finally:
        if conn:
            conn.close()
    return dados

def remover_professor(id_professor):
    conn = None
    try:
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM professores WHERE id = ?', (id_professor,))
        conn.commit()
        print("❌ Professor removido!")
    except sqlite3.Error as e:
        print(f"Erro ao remover professor: {e}")
    finally:
        if conn:
            conn.close()
            
def realizar_matricula(id_aluno, id_professor, estilo_escolhido):
    conn = None
    try:
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO matriculas (id_aluno, id_professor, estilo_escolhido) VALUES (?, ?, ?)', 
                       (id_aluno, id_professor, estilo_escolhido))
        conn.commit()
        print("✅ Matrícula realizada com sucesso!")
    except sqlite3.IntegrityError:
        print("❌ Erro: Aluno ou professor não encontrado. Verifique os IDs e tente novamente.")
    except sqlite3.Error as e:
        print(f"Erro ao realizar matrícula: {e}")
    finally:
        if conn:
            conn.close()
            
def pesquisar_professores(termo):
    conn = None
    dados = []
    try:        
        conn = obter_conexao()
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

# --- FUNÇÕES DE RELATÓRIOS ---

def resumo_por_estilo():
    """
    Objetivo 1: Fornece o estilo e a contagem de alunos vinculados.
    Alimenta o cálculo de 'Estilo Mais Popular' no Resumo Executivo.
    """
    conexao = None
    resultado = []
    try:
        conexao = obter_conexao()  
        cursor = conexao.cursor()
        
        cursor.execute("""
            SELECT estilo_escolhido, COUNT(id) 
            FROM matriculas 
            GROUP BY estilo_escolhido
        """)
        resultado = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"❌ Erro ao gerar resumo por estilo: {e}")
    finally:
        if conexao:
            conexao.close()
    return resultado

def alunos_por_professor():
    """
    Objetivo 2: Retorna o ID, o Nome do professor e o total de alunos associados.
    Garante visibilidade gerencial sobre professores sem turmas usando LEFT JOIN.
    """
    conexao = None
    resultado = []
    try:
        conexao = obter_conexao()  
        cursor = conexao.cursor()
        
        cursor.execute("""
            SELECT professores.id, professores.nome, COUNT(matriculas.id)
            FROM professores
            LEFT JOIN matriculas ON matriculas.id_professor = professores.id
            GROUP BY professores.id
        """)
        resultado = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"❌ Erro ao gerar alunos por professor: {e}")
    finally:
        if conexao:
            conexao.close()
    return resultado

def relatorio_alunos_por_estilo():
    """Relatório de total de alunos por estilo"""
    return resumo_por_estilo()

def relatorio_professores_por_materia():
    """Retorna quantidade de professores por matéria"""
    conn = None
    dados = []
    try:
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT materia, COUNT(*) as total_professores
            FROM professores
            GROUP BY materia
            ORDER BY total_professores DESC
        """)
        dados = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"❌ Erro ao gerar relatório de professores por matéria: {e}")
    finally:
        if conn:
            conn.close()
    return dados

def relatorio_alunos_por_professor():
    """Relatório detalhado de alunos vinculados a cada professor"""
    conn = None
    dados = []
    try:
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                p.nome as professor,
                a.nome as aluno,
                m.estilo_escolhido
            FROM matriculas m
            JOIN professores p ON m.id_professor = p.id
            JOIN alunos a ON m.id_aluno = a.id
            ORDER BY p.nome, a.nome
        """)
        dados = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"❌ Erro ao gerar relatório detalhado: {e}")
    finally:
        if conn:
            conn.close()
    return dados