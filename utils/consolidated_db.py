"""
Gerenciador de Banco de Dados Consolidado para o Fusione Core System
Suporte para SQLite, MariaDB e PostgreSQL com fallback automático
"""

import os
import sqlite3
import pandas as pd
from typing import Optional, List, Dict, Any
import logging
from pathlib import Path

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ConsolidatedDB:
    """Gerenciador de conexões de banco consolidado"""
    
    # Caminhos padrão dos bancos SQLite
    DEFAULT_SQLITE_PATHS = [
        # Caminhos locais (sandbox)
        "/home/ubuntu/fusione-core-system/sql/contencioso.sqlite",
        "/home/ubuntu/fusione-core-system/sql/geral.sqlite",
        "/home/ubuntu/fusione-core-system/sql/clientes.sqlite",
        # Caminhos Windows (produção)
        r"C:\Users\Gustavo_ri\fusione-core-system\sql\contencioso.sqlite",
        r"C:\Users\Gustavo_ri\fusione-core-system\sql\geral.sqlite", 
        r"C:\Users\Gustavo_ri\fusione-core-system\sql\clientes.sqlite",
        r"C:\Users\Gustavo_ri\fusione-core-system\sql\contratos.sqlite",
        r"C:\Users\Gustavo_ri\fusione-core-system\sql\procuracoes.sqlite",
        # Caminhos relativos
        "./sql/contencioso.sqlite",
        "./sql/geral.sqlite",
        "./sql/clientes.sqlite",
        "./sql/contratos.sqlite",
        "./sql/procuracoes.sqlite",
    ]
    
    def __init__(self):
        self.connections = {}
        self.available_dbs = []
        self._check_available_databases()
    
    def _check_available_databases(self):
        """Verifica quais bancos estão disponíveis"""
        for path in self.DEFAULT_SQLITE_PATHS:
            if os.path.exists(path):
                self.available_dbs.append(path)
                logger.info(f"Banco disponível: {path}")
        
        if not self.available_dbs:
            logger.warning("Nenhum banco SQLite encontrado. Usando dados demo.")
    
    def _try_connect(self, db_path: str) -> Optional[sqlite3.Connection]:
        """Tenta conectar a um banco SQLite"""
        try:
            if os.path.exists(db_path):
                return sqlite3.connect(db_path)
        except Exception as e:
            logger.error(f"Erro ao conectar em {db_path}: {e}")
        return None
    
    def query_df(self, sql: str, db_paths: List[str] = None) -> pd.DataFrame:
        """
        Executa uma consulta SQL e retorna um DataFrame
        Com fallback automático para dados demo
        """
        paths = db_paths or self.available_dbs or self.DEFAULT_SQLITE_PATHS
        
        for path in paths:
            conn = self._try_connect(path)
            if conn is None:
                continue
            
            try:
                df = pd.read_sql_query(sql, conn)
                conn.close()
                logger.info(f"Consulta executada com sucesso em: {path}")
                return df
            except Exception as e:
                logger.error(f"Erro na consulta em {path}: {e}")
                conn.close()
                continue
        
        # Fallback para dados demo
        logger.info("Usando dados demo (fallback)")
        return self._generate_demo_data(sql)
    
    def _generate_demo_data(self, sql: str) -> pd.DataFrame:
        """Gera dados demo realistas para o dashboard"""
        import numpy as np
        import datetime as dt
        
        # Gerar dados para os últimos 12 meses
        end_date = dt.date.today()
        start_date = end_date.replace(day=1) - pd.DateOffset(months=11)
        date_range = pd.date_range(start_date, periods=12, freq='MS')
        
        # Dados base do dashboard
        demo_data = pd.DataFrame({
            'mes': date_range.strftime('%Y-%m'),
            'data': date_range,
            'processos_ativos': np.random.randint(80, 140, 12),
            'valor_total': np.random.uniform(5e6, 12e6, 12).round(2),
            'valor_atualizado': np.random.uniform(6e6, 15e6, 12).round(2),
            'contratos_vigentes': np.random.randint(40, 85, 12),
            'requisicoes_abertas': np.random.randint(5, 30, 12),
            'coeficiente_trabalhista': np.random.uniform(0.15, 0.35, 12).round(3),
            'num_clientes': np.random.randint(25, 45, 12),
            'polo_ativo': np.random.randint(45, 75, 12),
            'polo_passivo': np.random.randint(25, 55, 12),
            'risco_alto': np.random.randint(5, 15, 12),
            'risco_medio': np.random.randint(15, 35, 12),
            'risco_baixo': np.random.randint(40, 70, 12),
        })
        
        # Adicionar categorias
        categorias = ['Trabalhista', 'Cível', 'Fiscal', 'Tributário']
        for categoria in categorias:
            demo_data[f'processos_{categoria.lower()}'] = np.random.randint(10, 40, 12)
        
        # Adicionar situações
        situacoes = ['Em Andamento', 'Suspenso', 'Arquivado', 'Finalizado']
        for situacao in situacoes:
            demo_data[f'situacao_{situacao.lower().replace(" ", "_")}'] = np.random.randint(5, 25, 12)
        
        return demo_data
    
    def get_kpi_data(self) -> Dict[str, Any]:
        """Retorna dados dos KPIs principais"""
        try:
            # Tentar consultas reais nos bancos SQLite
            
            # KPIs principais de processos
            df_processos = self.query_df("""
                SELECT 
                    COUNT(*) as processos_ativos,
                    SUM(valor_causa) as valor_total,
                    SUM(valor_atualizado) as valor_atualizado,
                    AVG(coeficiente_trabalhista) as coef_trabalhista,
                    COUNT(DISTINCT cliente_id) as num_clientes
                FROM processos 
                WHERE status = 'Ativo'
            """)
            
            # Distribuição por polo
            df_polo = self.query_df("""
                SELECT 
                    polo,
                    COUNT(*) as quantidade
                FROM processos 
                WHERE status = 'Ativo'
                GROUP BY polo
            """)
            
            # Distribuição por risco
            df_risco = self.query_df("""
                SELECT 
                    risco,
                    COUNT(*) as quantidade
                FROM processos 
                WHERE status = 'Ativo'
                GROUP BY risco
            """)
            
            if not df_processos.empty:
                kpis = df_processos.iloc[0].to_dict()
                
                # Adicionar dados de polo
                polo_dict = dict(zip(df_polo['polo'], df_polo['quantidade'])) if not df_polo.empty else {}
                kpis['polo_ativo'] = polo_dict.get('Ativo', 0)
                kpis['polo_passivo'] = polo_dict.get('Passivo', 0)
                
                # Adicionar dados de risco
                risco_dict = dict(zip(df_risco['risco'], df_risco['quantidade'])) if not df_risco.empty else {}
                kpis['risco_alto'] = risco_dict.get('Alto', 0)
                kpis['risco_medio'] = risco_dict.get('Médio', 0)
                kpis['risco_baixo'] = risco_dict.get('Baixo', 0)
                
                return kpis
                
        except Exception as e:
            logger.error(f"Erro ao obter KPIs reais: {e}")
        
        # Fallback para dados demo
        demo_df = self._generate_demo_data("")
        latest = demo_df.iloc[-1]
        
        return {
            'processos_ativos': int(latest['processos_ativos']),
            'valor_total': float(latest['valor_total']),
            'valor_atualizado': float(latest['valor_atualizado']),
            'coef_trabalhista': float(latest['coeficiente_trabalhista']),
            'num_clientes': int(latest['num_clientes']),
            'polo_ativo': int(latest['polo_ativo']),
            'polo_passivo': int(latest['polo_passivo']),
            'risco_alto': int(latest['risco_alto']),
            'risco_medio': int(latest['risco_medio']),
            'risco_baixo': int(latest['risco_baixo'])
        }
    
    def get_dashboard_data(self, periodo_meses: int = 12) -> pd.DataFrame:
        """Retorna dados para o dashboard executivo"""
        try:
            # Tentar consulta real (SQLite usa strftime ao invés de DATE_FORMAT)
            df = self.query_df(f"""
                SELECT 
                    strftime('%Y-%m', data_cadastro) as mes,
                    COUNT(*) as processos_ativos,
                    SUM(valor_causa) as valor_total,
                    SUM(valor_atualizado) as valor_atualizado,
                    AVG(coeficiente_trabalhista) as coeficiente_trabalhista,
                    COUNT(DISTINCT cliente_id) as num_clientes
                FROM processos 
                WHERE data_cadastro >= date('now', '-{periodo_meses} months')
                GROUP BY strftime('%Y-%m', data_cadastro)
                ORDER BY mes DESC
                LIMIT {periodo_meses}
            """)
            
            if not df.empty:
                # Ordenar por data crescente para o gráfico
                df = df.sort_values('mes')
                return df
                
        except Exception as e:
            logger.error(f"Erro ao obter dados do dashboard: {e}")
        
        # Fallback para dados demo
        demo_df = self._generate_demo_data("")
        return demo_df.tail(periodo_meses)
    
    def close_connections(self):
        """Fecha todas as conexões abertas"""
        for conn in self.connections.values():
            if conn:
                conn.close()
        self.connections.clear()

# Instância global
db_manager = ConsolidatedDB()
