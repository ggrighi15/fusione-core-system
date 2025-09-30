"""
Componente de Card KPI para o Dashboard Executivo
"""

import streamlit as st
from typing import Union, Optional

def kpi_card(
    label: str, 
    value: Union[str, int, float], 
    delta: Optional[float] = None,
    delta_label: str = "",
    format_value: bool = True,
    prefix: str = "",
    suffix: str = ""
):
    """
    Renderiza um card KPI estilizado
    
    Args:
        label: Rótulo do KPI
        value: Valor principal
        delta: Variação percentual (opcional)
        delta_label: Rótulo da variação
        format_value: Se deve formatar números
        prefix: Prefixo do valor (ex: "R$")
        suffix: Sufixo do valor (ex: "%")
    """
    
    # Formatação do valor
    if format_value and isinstance(value, (int, float)):
        if value >= 1000000:
            formatted_value = f"{prefix}{value/1000000:.1f}M{suffix}"
        elif value >= 1000:
            formatted_value = f"{prefix}{value/1000:.1f}K{suffix}"
        else:
            formatted_value = f"{prefix}{value:,.0f}{suffix}".replace(",", ".")
    else:
        formatted_value = f"{prefix}{value}{suffix}"
    
    # Formatação do delta
    delta_html = ""
    if delta is not None:
        arrow = "↑" if delta >= 0 else "↓"
        delta_class = "up" if delta >= 0 else "down"
        delta_text = f"{abs(delta):.1f}%"
        if delta_label:
            delta_text += f" {delta_label}"
        delta_html = f'<div class="kpi-delta {delta_class}">{arrow} {delta_text}</div>'
    
    # HTML do card
    card_html = f"""
    <div class="kpi-card fade-in">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{formatted_value}</div>
        {delta_html}
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)

def kpi_row(kpis: list):
    """
    Renderiza uma linha de KPIs
    
    Args:
        kpis: Lista de dicionários com dados dos KPIs
              Cada dict deve ter: label, value, delta (opcional)
    """
    cols = st.columns(len(kpis))
    
    for i, kpi in enumerate(kpis):
        with cols[i]:
            kpi_card(**kpi)

def metric_comparison_card(
    title: str,
    current_value: Union[int, float],
    previous_value: Union[int, float],
    format_as_currency: bool = False,
    format_as_percentage: bool = False
):
    """
    Card de comparação de métricas com período anterior
    """
    
    # Calcular variação
    if previous_value != 0:
        delta = ((current_value - previous_value) / previous_value) * 100
    else:
        delta = 0
    
    # Formatação
    prefix = ""
    suffix = ""
    
    if format_as_currency:
        prefix = "R$ "
    elif format_as_percentage:
        suffix = "%"
    
    kpi_card(
        label=title,
        value=current_value,
        delta=delta,
        delta_label="vs mês anterior",
        prefix=prefix,
        suffix=suffix
    )

def status_badge(text: str, status: str = "default"):
    """
    Renderiza um badge de status
    
    Args:
        text: Texto do badge
        status: Tipo do status (default, primary, secondary, success, warning, error)
    """
    
    badge_html = f'<span class="badge {status}">{text}</span>'
    st.markdown(badge_html, unsafe_allow_html=True)

def progress_card(
    title: str,
    current: int,
    total: int,
    color: str = "primary"
):
    """
    Card com barra de progresso
    """
    
    percentage = (current / total * 100) if total > 0 else 0
    
    progress_html = f"""
    <div class="kpi-card">
        <div class="kpi-label">{title}</div>
        <div class="kpi-value">{current} / {total}</div>
        <div style="background: rgba(255,255,255,0.1); border-radius: 10px; height: 8px; margin-top: 8px;">
            <div style="background: var(--vipal-{color}); height: 100%; border-radius: 10px; width: {percentage}%; transition: width 0.3s ease;"></div>
        </div>
        <div style="font-size: 0.8rem; color: var(--vipal-muted); margin-top: 4px;">{percentage:.1f}% concluído</div>
    </div>
    """
    
    st.markdown(progress_html, unsafe_allow_html=True)
