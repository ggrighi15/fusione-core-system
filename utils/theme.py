"""
Tema personalizado para o Fusione Core System
Baseado nas cores da Vipal
"""

VIPAL_COLORS = {
    "primary": "#003A70",      # Azul Vipal
    "secondary": "#E2001A",    # Vermelho Vipal
    "background": "#0B0E14",   # Fundo escuro
    "surface": "#111827",      # Superfície
    "text": "#e5e7eb",         # Texto claro
    "muted": "#94a3b8",        # Texto secundário
    "accent": "#1E90FF",       # Azul de destaque
    "success": "#16a34a",      # Verde sucesso
    "warning": "#f59e0b",      # Amarelo aviso
    "error": "#ef4444"         # Vermelho erro
}

CSS = f"""
<style>
:root {{
  --vipal-primary: {VIPAL_COLORS['primary']};
  --vipal-secondary: {VIPAL_COLORS['secondary']};
  --vipal-surface: {VIPAL_COLORS['surface']};
  --vipal-text: {VIPAL_COLORS['text']};
  --vipal-muted: {VIPAL_COLORS['muted']};
  --vipal-accent: {VIPAL_COLORS['accent']};
  --vipal-success: {VIPAL_COLORS['success']};
  --vipal-warning: {VIPAL_COLORS['warning']};
  --vipal-error: {VIPAL_COLORS['error']};
}}

/* Cards KPI */
.kpi-card {{
  background: linear-gradient(180deg, rgba(0,0,0,0.25), rgba(0,0,0,0.05));
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 16px;
  padding: 16px 18px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.25);
  transition: all 0.3s ease;
}}

.kpi-card:hover {{
  transform: translateY(-2px);
  box-shadow: 0 15px 40px rgba(0,0,0,0.35);
}}

.kpi-label {{
  font-size: 0.9rem; 
  color: var(--vipal-muted); 
  margin-bottom: 6px;
  font-weight: 500;
}}

.kpi-value {{
  font-size: 1.8rem; 
  font-weight: 700; 
  color: var(--vipal-text);
  margin-bottom: 4px;
}}

.kpi-delta.up {{ 
  color: var(--vipal-success); 
  font-weight: 600; 
}}

.kpi-delta.down {{ 
  color: var(--vipal-error); 
  font-weight: 600; 
}}

/* Badges */
.badge {{
  display: inline-flex; 
  align-items: center; 
  gap: 8px;
  background: rgba(30, 144, 255, 0.12);
  border: 1px solid rgba(30, 144, 255, 0.35);
  color: #cfe8ff; 
  padding: 6px 10px; 
  border-radius: 999px; 
  font-size: 0.8rem;
  font-weight: 500;
}}

.badge.primary {{
  background: rgba(0, 58, 112, 0.12);
  border-color: rgba(0, 58, 112, 0.35);
  color: var(--vipal-primary);
}}

.badge.secondary {{
  background: rgba(226, 0, 26, 0.12);
  border-color: rgba(226, 0, 26, 0.35);
  color: var(--vipal-secondary);
}}

/* Títulos de seção */
.section-title {{ 
  font-size: 1.1rem; 
  color: var(--vipal-muted); 
  margin: 8px 0 4px;
  font-weight: 600;
}}

/* Dashboard específico */
.dashboard-header {{
  background: linear-gradient(135deg, var(--vipal-primary), var(--vipal-accent));
  color: white;
  padding: 20px;
  border-radius: 12px;
  margin-bottom: 20px;
}}

.dashboard-title {{
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 8px;
}}

.dashboard-subtitle {{
  font-size: 1rem;
  opacity: 0.9;
}}

/* Filtros */
.filter-container {{
  background: var(--vipal-surface);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 12px;
  padding: 16px;
  margin-bottom: 20px;
}}

/* Animações */
@keyframes fadeIn {{
  from {{ opacity: 0; transform: translateY(20px); }}
  to {{ opacity: 1; transform: translateY(0); }}
}}

.fade-in {{
  animation: fadeIn 0.6s ease-out;
}}

/* Responsividade */
@media (max-width: 768px) {{
  .kpi-card {{
    padding: 12px 14px;
  }}
  
  .kpi-value {{
    font-size: 1.4rem;
  }}
  
  .dashboard-title {{
    font-size: 1.5rem;
  }}
}}
</style>
"""

def apply_theme():
    """Aplica o tema personalizado da Vipal"""
    import streamlit as st
    st.markdown(CSS, unsafe_allow_html=True)

def get_color(color_name: str) -> str:
    """Retorna uma cor específica do tema"""
    return VIPAL_COLORS.get(color_name, "#000000")
