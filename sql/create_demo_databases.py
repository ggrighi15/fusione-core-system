"""
Script para criar bancos de dados SQLite de demonstração
com dados realistas para o Fusione Core System
"""

import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

def create_demo_databases():
    """Cria bancos de dados SQLite com dados de demonstração"""
    
    # Garantir que o diretório sql existe
    os.makedirs('/home/ubuntu/fusione-core-system/sql', exist_ok=True)
    
    # 1. Banco de Contencioso
    create_contencioso_db()
    
    # 2. Banco Geral
    create_geral_db()
    
    # 3. Banco de Clientes
    create_clientes_db()
    
    print("✅ Bancos de dados de demonstração criados com sucesso!")

def create_contencioso_db():
    """Cria banco de dados de contencioso"""
    
    conn = sqlite3.connect('/home/ubuntu/fusione-core-system/sql/contencioso.sqlite')
    
    # Tabela de processos
    processos_data = []
    categorias = ['Trabalhista', 'Cível', 'Fiscal', 'Tributário']
    situacoes = ['Em Andamento', 'Suspenso', 'Arquivado', 'Finalizado']
    polos = ['Ativo', 'Passivo']
    riscos = ['Alto', 'Médio', 'Baixo']
    
    for i in range(1, 201):  # 200 processos
        data_cadastro = datetime.now() - timedelta(days=random.randint(1, 730))
        
        processo = {
            'id': i,
            'numero_processo': f"{random.randint(1000000, 9999999)}-{random.randint(10, 99)}.{random.randint(2020, 2024)}.{random.randint(1, 9)}.{random.randint(10, 99)}.{random.randint(1000, 9999)}",
            'cliente_id': random.randint(1, 50),
            'categoria': random.choice(categorias),
            'situacao': random.choice(situacoes),
            'polo': random.choice(polos),
            'risco': random.choice(riscos),
            'valor_causa': round(random.uniform(10000, 5000000), 2),
            'valor_atualizado': round(random.uniform(15000, 7500000), 2),
            'coeficiente_trabalhista': round(random.uniform(0.1, 0.4), 3),
            'data_cadastro': data_cadastro.strftime('%Y-%m-%d'),
            'data_atualizacao': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'status': 'Ativo' if random.random() > 0.2 else 'Inativo',
            'observacoes': f'Processo {random.choice(["de alta complexidade", "em fase inicial", "aguardando decisão", "em recurso"])}'
        }
        processos_data.append(processo)
    
    df_processos = pd.DataFrame(processos_data)
    df_processos.to_sql('processos', conn, if_exists='replace', index=False)
    
    # Tabela de movimentações
    movimentacoes_data = []
    tipos_mov = ['Petição', 'Audiência', 'Sentença', 'Recurso', 'Despacho', 'Decisão']
    
    for i in range(1, 501):  # 500 movimentações
        movimentacao = {
            'id': i,
            'processo_id': random.randint(1, 200),
            'tipo': random.choice(tipos_mov),
            'descricao': f'Movimentação {random.choice(["protocolada", "agendada", "realizada", "pendente"])}',
            'data_movimentacao': (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d'),
            'responsavel': f'Advogado {random.randint(1, 10)}',
            'status': random.choice(['Concluída', 'Pendente', 'Cancelada'])
        }
        movimentacoes_data.append(movimentacao)
    
    df_movimentacoes = pd.DataFrame(movimentacoes_data)
    df_movimentacoes.to_sql('movimentacoes', conn, if_exists='replace', index=False)
    
    conn.close()
    print("✅ Banco contencioso.sqlite criado")

def create_geral_db():
    """Cria banco de dados geral"""
    
    conn = sqlite3.connect('/home/ubuntu/fusione-core-system/sql/geral.sqlite')
    
    # Tabela de usuários
    usuarios_data = []
    for i in range(1, 21):  # 20 usuários
        usuario = {
            'id': i,
            'nome': f'Usuário {i}',
            'email': f'usuario{i}@vipal.com.br',
            'perfil': random.choice(['Admin', 'Advogado', 'Assistente', 'Consultor']),
            'ativo': random.choice([True, False]),
            'data_cadastro': (datetime.now() - timedelta(days=random.randint(30, 365))).strftime('%Y-%m-%d'),
            'ultimo_acesso': (datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d %H:%M:%S')
        }
        usuarios_data.append(usuario)
    
    df_usuarios = pd.DataFrame(usuarios_data)
    df_usuarios.to_sql('usuarios', conn, if_exists='replace', index=False)
    
    # Tabela de configurações
    config_data = [
        {'chave': 'sistema_nome', 'valor': 'Fusione Core System', 'descricao': 'Nome do sistema'},
        {'chave': 'versao', 'valor': '2.0.0', 'descricao': 'Versão atual'},
        {'chave': 'empresa', 'valor': 'Vipal', 'descricao': 'Empresa cliente'},
        {'chave': 'backup_automatico', 'valor': 'true', 'descricao': 'Backup automático ativo'},
        {'chave': 'manutencao', 'valor': 'false', 'descricao': 'Modo manutenção'}
    ]
    
    df_config = pd.DataFrame(config_data)
    df_config.to_sql('configuracoes', conn, if_exists='replace', index=False)
    
    conn.close()
    print("✅ Banco geral.sqlite criado")

def create_clientes_db():
    """Cria banco de dados de clientes"""
    
    conn = sqlite3.connect('/home/ubuntu/fusione-core-system/sql/clientes.sqlite')
    
    # Tabela de clientes
    clientes_data = []
    tipos = ['Pessoa Física', 'Pessoa Jurídica']
    segmentos = ['Indústria', 'Comércio', 'Serviços', 'Agronegócio', 'Tecnologia']
    
    for i in range(1, 51):  # 50 clientes
        tipo = random.choice(tipos)
        
        if tipo == 'Pessoa Física':
            nome = f'Cliente PF {i}'
            documento = f'{random.randint(10000000000, 99999999999)}'  # CPF simulado
        else:
            nome = f'Empresa Cliente {i} Ltda'
            documento = f'{random.randint(10000000000000, 99999999999999)}'  # CNPJ simulado
        
        cliente = {
            'id': i,
            'nome': nome,
            'tipo': tipo,
            'documento': documento,
            'email': f'cliente{i}@email.com',
            'telefone': f'({random.randint(11, 99)}) {random.randint(90000, 99999)}-{random.randint(1000, 9999)}',
            'endereco': f'Rua {random.choice(["das Flores", "Principal", "Central", "dos Trabalhadores"])}, {random.randint(1, 999)}',
            'cidade': random.choice(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Curitiba']),
            'estado': random.choice(['SP', 'RJ', 'MG', 'RS', 'PR']),
            'segmento': random.choice(segmentos) if tipo == 'Pessoa Jurídica' else None,
            'ativo': random.choice([True, False]),
            'data_cadastro': (datetime.now() - timedelta(days=random.randint(30, 730))).strftime('%Y-%m-%d'),
            'observacoes': f'Cliente {random.choice(["prioritário", "regular", "especial"])}'
        }
        clientes_data.append(cliente)
    
    df_clientes = pd.DataFrame(clientes_data)
    df_clientes.to_sql('clientes', conn, if_exists='replace', index=False)
    
    # Tabela de contratos
    contratos_data = []
    tipos_contrato = ['Consultoria', 'Assessoria', 'Representação', 'Auditoria']
    
    for i in range(1, 101):  # 100 contratos
        contrato = {
            'id': i,
            'cliente_id': random.randint(1, 50),
            'numero': f'CONT-{i:04d}/2024',
            'tipo': random.choice(tipos_contrato),
            'valor': round(random.uniform(5000, 100000), 2),
            'data_inicio': (datetime.now() - timedelta(days=random.randint(30, 365))).strftime('%Y-%m-%d'),
            'data_fim': (datetime.now() + timedelta(days=random.randint(30, 730))).strftime('%Y-%m-%d'),
            'status': random.choice(['Ativo', 'Suspenso', 'Finalizado']),
            'responsavel': f'Advogado {random.randint(1, 10)}',
            'observacoes': f'Contrato {random.choice(["renovado", "novo", "em revisão"])}'
        }
        contratos_data.append(contrato)
    
    df_contratos = pd.DataFrame(contratos_data)
    df_contratos.to_sql('contratos', conn, if_exists='replace', index=False)
    
    conn.close()
    print("✅ Banco clientes.sqlite criado")

if __name__ == "__main__":
    create_demo_databases()
