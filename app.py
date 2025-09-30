"""
Fusione Core System - Sistema Jurídico Consolidado
Aplicação principal com tema Vipal
"""

import streamlit as st
from utils.theme import apply_theme

# Configuração da página
st.set_page_config(
    page_title="Fusione - Sistema Consolidado",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Aplicar tema personalizado
apply_theme()

# Logo e branding
st.logo("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Circle-icons-briefcase.svg/120px-Circle-icons-briefcase.svg.png")

# Sidebar
st.sidebar.title("🧭 Fusione")
st.sidebar.caption("Sistema Jurídico Consolidado — Vipal")

# Páginas disponíveis
pages = {
    "📊 Dashboard": [
        st.Page("pages/00_Dashboard_Executivo.py", title="📊 Dashboard Executivo", icon="📊"),
    ]
}

# Navegação
pg = st.navigation(pages)
pg.run()

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    <div style='text-align: center; color: #94a3b8; font-size: 0.8rem;'>
        <p>Fusione Core System v2.0</p>
        <p>Desenvolvido para Vipal</p>
    </div>
    """, 
    unsafe_allow_html=True
)
