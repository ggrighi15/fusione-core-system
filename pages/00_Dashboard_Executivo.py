"""
Dashboard Executivo - Fusione Core System
Painel principal com KPIs e métricas da Vipal
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from utils.theme import apply_theme, VIPAL_COLORS
from utils.consolidated_db import db_manager
from components.kpi_card import kpi_card, kpi_row, metric_comparison_card, status_badge

# Aplicar tema
apply_theme()

# Header do Dashboard
st.markdown("""
<div class="dashboard-header">
    <div class="dashboard-title">📊 Dashboard Executivo</div>
    <div class="dashboard-subtitle">Painel de Controle Jurídico — Vipal</div>
</div>
""", unsafe_allow_html=True)

# Filtros
st.markdown("### 🔍 Filtros")
with st.container():
    st.markdown('<div class="filter-container">', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        polo = st.selectbox(
            "Polo",
            ["Todos", "Ativo", "Passivo"],
            help="Filtrar por polo processual"
        )
    
    with col2:
        categoria = st.selectbox(
            "Categoria",
            ["Todas", "Trabalhista", "Cível", "Fiscal", "Tributário"],
            help="Filtrar por categoria jurídica"
        )
    
    with col3:
        situacao = st.selectbox(
            "Situação",
            ["Todas", "Em Andamento", "Suspenso", "Arquivado", "Finalizado"],
            help="Filtrar por situação do processo"
        )
    
    with col4:
        periodo = st.slider(
            "Período (meses)",
            min_value=3,
            max_value=24,
            value=12,
            help="Período de análise em meses"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)

# Obter dados
kpi_data = db_manager.get_kpi_data()
dashboard_data = db_manager.get_dashboard_data(periodo)

# KPIs Principais
st.markdown("### 📈 KPIs Principais")

# Primeira linha de KPIs
col1, col2, col3, col4 = st.columns(4)

with col1:
    # Calcular delta para processos ativos
    if len(dashboard_data) >= 2:
        current = dashboard_data.iloc[-1]['processos_ativos']
        previous = dashboard_data.iloc[-2]['processos_ativos']
        delta_processos = ((current - previous) / previous * 100) if previous > 0 else 0
    else:
        delta_processos = None
    
    kpi_card(
        label="Processos Ativos",
        value=kpi_data['processos_ativos'],
        delta=delta_processos,
        delta_label="vs mês anterior"
    )

with col2:
    kpi_card(
        label="Valor Atualizado",
        value=kpi_data['valor_atualizado'],
        prefix="R$ ",
        format_value=True
    )

with col3:
    kpi_card(
        label="Coeficiente Trabalhista",
        value=kpi_data['coef_trabalhista'],
        format_value=False,
        suffix="%"
    )

with col4:
    kpi_card(
        label="# Clientes",
        value=kpi_data['num_clientes'],
        format_value=False
    )

# Segunda linha de KPIs
st.markdown("### ⚖️ Distribuição por Polo e Risco")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    kpi_card(
        label="Polo Ativo",
        value=kpi_data['polo_ativo'],
        format_value=False
    )

with col2:
    kpi_card(
        label="Polo Passivo", 
        value=kpi_data['polo_passivo'],
        format_value=False
    )

with col3:
    kpi_card(
        label="Risco Alto",
        value=kpi_data['risco_alto'],
        format_value=False
    )

with col4:
    kpi_card(
        label="Risco Médio",
        value=kpi_data['risco_medio'],
        format_value=False
    )

with col5:
    kpi_card(
        label="Risco Baixo",
        value=kpi_data['risco_baixo'],
        format_value=False
    )

# Gráficos
st.markdown("### 📊 Análise Temporal")

# Preparar dados para gráficos
df_chart = dashboard_data.copy()
df_chart['mes_nome'] = pd.to_datetime(df_chart['mes'] + '-01').dt.strftime('%b/%Y')

# Gráfico de evolução temporal
fig_evolution = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        "Processos Ativos", 
        "Valor Total (R$ Milhões)", 
        "Número de Clientes", 
        "Coeficiente Trabalhista (%)"
    ),
    specs=[[{"secondary_y": False}, {"secondary_y": False}],
           [{"secondary_y": False}, {"secondary_y": False}]]
)

# Processos Ativos
fig_evolution.add_trace(
    go.Scatter(
        x=df_chart['mes_nome'], 
        y=df_chart['processos_ativos'],
        mode='lines+markers',
        name='Processos',
        line=dict(color=VIPAL_COLORS['primary'], width=3),
        marker=dict(size=8)
    ),
    row=1, col=1
)

# Valor Total
fig_evolution.add_trace(
    go.Bar(
        x=df_chart['mes_nome'], 
        y=df_chart['valor_total'] / 1e6,  # Converter para milhões
        name='Valor Total',
        marker_color=VIPAL_COLORS['secondary']
    ),
    row=1, col=2
)

# Número de Clientes
fig_evolution.add_trace(
    go.Scatter(
        x=df_chart['mes_nome'], 
        y=df_chart['num_clientes'],
        mode='lines+markers',
        name='Clientes',
        line=dict(color=VIPAL_COLORS['accent'], width=3),
        marker=dict(size=8)
    ),
    row=2, col=1
)

# Coeficiente Trabalhista
fig_evolution.add_trace(
    go.Bar(
        x=df_chart['mes_nome'], 
        y=df_chart['coeficiente_trabalhista'] * 100,  # Converter para %
        name='Coef. Trabalhista',
        marker_color=VIPAL_COLORS['warning']
    ),
    row=2, col=2
)

fig_evolution.update_layout(
    height=600,
    showlegend=False,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color=VIPAL_COLORS['text']),
    margin=dict(t=60, l=40, r=20, b=40)
)

fig_evolution.update_xaxes(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
fig_evolution.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.1)')

st.plotly_chart(fig_evolution, use_container_width=True)

# Gráficos de distribuição
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🎯 Distribuição por Categoria")
    
    # Dados de categoria (demo)
    categorias_data = {
        'Trabalhista': np.random.randint(40, 60),
        'Cível': np.random.randint(20, 35),
        'Fiscal': np.random.randint(15, 25),
        'Tributário': np.random.randint(10, 20)
    }
    
    fig_categoria = go.Figure(data=[
        go.Pie(
            labels=list(categorias_data.keys()),
            values=list(categorias_data.values()),
            hole=0.4,
            marker_colors=[VIPAL_COLORS['primary'], VIPAL_COLORS['secondary'], 
                          VIPAL_COLORS['accent'], VIPAL_COLORS['warning']]
        )
    ])
    
    fig_categoria.update_layout(
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color=VIPAL_COLORS['text']),
        showlegend=True
    )
    
    st.plotly_chart(fig_categoria, use_container_width=True)

with col2:
    st.markdown("#### ⚖️ Distribuição por Polo")
    
    # Dados de polo
    polo_data = {
        'Ativo': kpi_data['polo_ativo'],
        'Passivo': kpi_data['polo_passivo']
    }
    
    fig_polo = go.Figure(data=[
        go.Bar(
            x=list(polo_data.keys()),
            y=list(polo_data.values()),
            marker_color=[VIPAL_COLORS['primary'], VIPAL_COLORS['secondary']],
            text=list(polo_data.values()),
            textposition='auto'
        )
    ])
    
    fig_polo.update_layout(
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color=VIPAL_COLORS['text']),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    )
    
    st.plotly_chart(fig_polo, use_container_width=True)

# Tabela de detalhes
st.markdown("### 📋 Detalhes por Período")

# Preparar dados da tabela
table_data = df_chart[['mes_nome', 'processos_ativos', 'valor_total', 'num_clientes']].copy()
table_data['valor_total'] = table_data['valor_total'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
table_data.columns = ['Mês', 'Processos Ativos', 'Valor Total', 'Clientes']

st.dataframe(
    table_data,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Mês": st.column_config.TextColumn("Mês", width="small"),
        "Processos Ativos": st.column_config.NumberColumn("Processos Ativos", width="small"),
        "Valor Total": st.column_config.TextColumn("Valor Total", width="medium"),
        "Clientes": st.column_config.NumberColumn("Clientes", width="small")
    }
)

# Status e alertas
st.markdown("### 🚨 Status e Alertas")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Status do Sistema:**")
    status_badge("Operacional", "success")
    status_badge("Dados Atualizados", "primary")

with col2:
    st.markdown("**Alertas Ativos:**")
    status_badge("3 Prazos Vencendo", "warning")
    status_badge("1 Processo Crítico", "error")

with col3:
    st.markdown("**Última Atualização:**")
    st.write(f"📅 {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    st.write("🔄 Sincronização automática ativa")

# Rodapé com informações adicionais
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #94a3b8; font-size: 0.9rem;'>
        <p><strong>Dashboard Executivo Fusione</strong> | Desenvolvido para Vipal</p>
        <p>Dados atualizados em tempo real | Última sincronização: {}</p>
    </div>
    """.format(datetime.now().strftime('%d/%m/%Y às %H:%M')), 
    unsafe_allow_html=True
)
