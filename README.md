# 🧭 Fusione Core System

Sistema Jurídico Consolidado desenvolvido para a **Vipal** com Dashboard Executivo moderno e KPIs em tempo real.

## 🚀 Características Principais

### Dashboard Executivo
- **KPIs Principais**: Processos Ativos, Valor Atualizado, Coeficiente Trabalhista, Número de Clientes
- **Distribuição por Polo**: Ativo/Passivo com visualizações interativas
- **Gestão de Risco**: Classificação Alto/Médio/Baixo
- **Análise Temporal**: Gráficos evolutivos dos últimos 12 meses
- **Filtros Avançados**: Por Polo, Categoria, Situação e Período

### Tema Vipal
- **Cores Corporativas**: Azul #003A70 e Vermelho #E2001A
- **Design Moderno**: Cards com gradientes e animações suaves
- **Interface Responsiva**: Adaptável a diferentes tamanhos de tela
- **UX Otimizada**: Navegação intuitiva e componentes elegantes

### Arquitetura de Dados
- **Bancos SQLite**: Contencioso, Geral e Clientes
- **Fallback Automático**: Dados demo quando bancos não disponíveis
- **Consultas Otimizadas**: Performance melhorada para grandes volumes
- **Pool de Conexões**: Gerenciamento eficiente de recursos

## 📦 Instalação

### Pré-requisitos
- Python 3.11+
- pip

### Instalação Rápida
```bash
# Clonar o repositório
git clone https://github.com/ggrighi15/fusione-core-system.git
cd fusione-core-system

# Instalar dependências
pip install -r requirements.txt

# Criar bancos de demonstração (opcional)
python sql/create_demo_databases.py

# Executar aplicação
streamlit run app.py
```

### Acesso
- **URL Local**: http://localhost:8501
- **Dashboard**: Acesse "Dashboard Executivo" na navegação lateral

## 🗂️ Estrutura do Projeto

```
fusione-core-system/
├── app.py                              # Aplicação principal Streamlit
├── pages/
│   └── 00_Dashboard_Executivo.py       # Dashboard principal
├── utils/
│   ├── theme.py                        # Tema personalizado Vipal
│   └── consolidated_db.py              # Gerenciador de banco consolidado
├── components/
│   └── kpi_card.py                     # Componentes de KPI
├── sql/
│   ├── contencioso.sqlite              # Banco de processos
│   ├── geral.sqlite                    # Banco geral do sistema
│   ├── clientes.sqlite                 # Banco de clientes
│   └── create_demo_databases.py        # Script para dados demo
├── .streamlit/
│   └── config.toml                     # Configuração do tema
└── requirements.txt                    # Dependências Python
```

## 📊 KPIs Implementados

### Principais Métricas
- **Processos Ativos**: Contagem total de processos em andamento
- **Valor Atualizado**: Soma dos valores atualizados dos processos (R$)
- **Coeficiente Trabalhista**: Média percentual dos coeficientes
- **Número de Clientes**: Contagem de clientes únicos

### Distribuições
- **Por Polo**: Ativo vs Passivo
- **Por Risco**: Alto, Médio, Baixo
- **Por Categoria**: Trabalhista, Cível, Fiscal, Tributário
- **Por Situação**: Em Andamento, Suspenso, Arquivado, Finalizado

## 🎨 Personalização

### Cores do Tema
As cores podem ser ajustadas em `utils/theme.py`:
```python
VIPAL_COLORS = {
    "primary": "#003A70",      # Azul Vipal
    "secondary": "#E2001A",    # Vermelho Vipal
    "background": "#0B0E14",   # Fundo escuro
    # ... outras cores
}
```

### Caminhos dos Bancos
Configure os caminhos dos bancos SQLite em `utils/consolidated_db.py`:
```python
DEFAULT_SQLITE_PATHS = [
    "/caminho/para/contencioso.sqlite",
    "/caminho/para/geral.sqlite",
    "/caminho/para/clientes.sqlite",
]
```

## 🔧 Desenvolvimento

### Adicionando Novas Páginas
1. Crie o arquivo em `pages/`
2. Adicione a página em `app.py` na seção `pages`
3. Importe os utilitários necessários

### Criando Novos KPIs
1. Adicione a consulta SQL em `consolidated_db.py`
2. Crie o componente visual em `components/`
3. Integre no dashboard principal

## 📈 Performance

### Otimizações Implementadas
- **Cache de Consultas**: Reduz tempo de carregamento
- **Lazy Loading**: Carregamento sob demanda
- **Pool de Conexões**: Gerenciamento eficiente de recursos
- **Fallback Inteligente**: Dados demo quando necessário

## 🛠️ Tecnologias

- **Frontend**: Streamlit 1.50.0
- **Visualização**: Plotly 5.22.0
- **Dados**: Pandas + SQLite
- **Estilo**: CSS customizado
- **Python**: 3.11+

## 📝 Licença

Desenvolvido para **Vipal** - Todos os direitos reservados.

## 🤝 Contribuição

Para contribuir com o projeto:
1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Abra um Pull Request

## 📞 Suporte

Para suporte técnico, entre em contato com a equipe de desenvolvimento.

---

**Fusione Core System v2.0** - Sistema Jurídico Consolidado para Vipal
