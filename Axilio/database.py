import sqlite3

# Função para conectar ao banco de dados
def conectar():
    conexao = sqlite3.connect('escola_danca.db')
    return conexao

# Função para inicializar o banco com todas as tabelas
def iniciar_banco():
    conexao = conectar()
    cursor = conexao.cursor()
    
    # Tabela de Alunos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            estilo TEXT NOT NULL
        )
    ''')
    
    # Tabela de Professores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            especialidade TEXT NOT NULL
        )
    ''')
    
    # Tabela de Matrículas (vínculo entre alunos, professores e estilo)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matriculas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_aluno INTEGER NOT NULL,
            id_professor INTEGER NOT NULL,
            estilo_escolhido TEXT NOT NULL,
            data_matricula TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_aluno) REFERENCES alunos(id),
            FOREIGN KEY (id_professor) REFERENCES professores(id)
        )
    ''')
    
    conexao.commit()
    conexao.close()

# ============= FUNÇÕES DE ALUNOS =============

def cadastrar_aluno(nome, estilo):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO alunos (nome, estilo) VALUES (?, ?)', (nome, estilo))
        conexao.commit()
        conexao.close()
        return {"sucesso": True, "mensagem": f"✅ {nome} adicionado com sucesso!"}
    except sqlite3.IntegrityError:
        return {"sucesso": False, "mensagem": f"⚠️ Erro: O aluno '{nome}' já está cadastrado no sistema."}

def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM alunos')
    rows = cursor.fetchall()
    conexao.close()
    return rows

def atualizar_estilo_aluno(id_aluno, novo_estilo):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('UPDATE alunos SET estilo = ? WHERE id = ?', (novo_estilo, id_aluno))
    sucesso = cursor.rowcount > 0
    conexao.commit()
    conexao.close()
    return sucesso

def remover_aluno(id_aluno):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM alunos WHERE id = ?', (id_aluno,))
    sucesso = cursor.rowcount > 0
    conexao.commit()
    conexao.close()
    return sucesso

# ============= FUNÇÕES DE PROFESSORES =============

def cadastrar_professor(nome, especialidade):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO professores (nome, especialidade) VALUES (?, ?)', (nome, especialidade))
        conexao.commit()
        conexao.close()
        return {"sucesso": True, "mensagem": f"✅ {nome} adicionado como professor com sucesso!"}
    except sqlite3.IntegrityError:
        return {"sucesso": False, "mensagem": f"⚠️ Erro: O professor '{nome}' já está cadastrado no sistema."}

def listar_professores():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM professores')
    rows = cursor.fetchall()
    conexao.close()
    return rows

def remover_professor(id_professor):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM professores WHERE id = ?', (id_professor,))
    sucesso = cursor.rowcount > 0
    conexao.commit()
    conexao.close()
    return sucesso

# ============= FUNÇÕES DE MATRÍCULAS =============

def realizar_matricula(aluno_id, prof_id, estilo):
    """
    Realiza uma matrícula vinculando um aluno a um professor e um estilo de dança.
    Retorna um dicionário com sucesso e mensagem.
    """
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        
        # Verifica se o aluno existe
        cursor.execute('SELECT id FROM alunos WHERE id = ?', (aluno_id,))
        if cursor.fetchone() is None:
            return {"sucesso": False, "mensagem": f"⚠️ Erro: Aluno com ID {aluno_id} não existe."}
        
        # Verifica se o professor existe
        cursor.execute('SELECT id FROM professores WHERE id = ?', (prof_id,))
        if cursor.fetchone() is None:
            return {"sucesso": False, "mensagem": f"⚠️ Erro: Professor com ID {prof_id} não existe."}
        
        # Realiza a matrícula
        cursor.execute('''
            INSERT INTO matriculas (id_aluno, id_professor, estilo_escolhido)
            VALUES (?, ?, ?)
        ''', (aluno_id, prof_id, estilo))
        
        conexao.commit()
        conexao.close()
        
        return {"sucesso": True, "mensagem": f"✅ Matrícula realizada com sucesso! Aluno ID {aluno_id} vinculado ao Professor ID {prof_id} - Estilo: {estilo}"}
    
    except Exception as e:
        return {"sucesso": False, "mensagem": f"❌ Erro ao realizar matrícula: {str(e)}"}

def listar_diario():
    """
    Realiza uma consulta com JOIN triplo para exibir o diário de classe.
    Retorna: Nome do Aluno | Nome do Professor | Estilo Matriculado
    """
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        
        cursor.execute('''
            SELECT alunos.nome, professores.nome, matriculas.estilo_escolhido
            FROM matriculas
            JOIN alunos ON matriculas.id_aluno = alunos.id
            JOIN professores ON matriculas.id_professor = professores.id
        ''')
        
        rows = cursor.fetchall()
        conexao.close()
        
        return rows
    
    except Exception as e:
        print(f"❌ Erro ao listar diário: {str(e)}")
        return []

def remover_matricula(matricula_id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM matriculas WHERE id = ?', (matricula_id,))
    sucesso = cursor.rowcount > 0
    conexao.commit()
    conexao.close()
    return sucesso
