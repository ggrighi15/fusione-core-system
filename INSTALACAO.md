# 🚀 Guia de Instalação - Fusione Core System

## Instalação Rápida (Recomendada)

### 1. Clonar o Repositório
```bash
git clone https://github.com/ggrighi15/fusione-core-system.git
cd fusione-core-system
```

### 2. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 3. Executar o Sistema
```bash
streamlit run app.py
```

### 4. Acessar o Dashboard
- Abra o navegador em: http://localhost:8501
- Clique em "Dashboard Executivo" na barra lateral

## 🗄️ Configuração dos Bancos de Dados

### Opção 1: Usar Dados Demo (Padrão)
Os bancos SQLite com dados de demonstração já estão incluídos em `/sql/`:
- `contencioso.sqlite` - 200 processos demo
- `geral.sqlite` - Usuários e configurações
- `clientes.sqlite` - 50 clientes e 100 contratos

### Opção 2: Conectar seus Bancos Reais
Edite o arquivo `utils/consolidated_db.py` e ajuste os caminhos:

```python
DEFAULT_SQLITE_PATHS = [
    r"C:\Users\Gustavo_ri\fusione-core-system\sql\contencioso.sqlite",
    r"C:\Users\Gustavo_ri\fusione-core-system\sql\geral.sqlite",
    r"C:\Users\Gustavo_ri\fusione-core-system\sql\clientes.sqlite",
    # Adicione seus caminhos aqui
]
```

### Opção 3: Recriar Dados Demo
```bash
python sql/create_demo_databases.py
```

## 🎯 KPIs Disponíveis

### Principais Métricas
- **Processos Ativos**: Contagem de processos em andamento
- **Valor Atualizado**: Soma dos valores atualizados (R$)
- **Coeficiente Trabalhista**: Média percentual
- **Número de Clientes**: Clientes únicos

### Distribuições
- **Por Polo**: Ativo vs Passivo
- **Por Risco**: Alto, Médio, Baixo
- **Por Categoria**: Trabalhista, Cível, Fiscal, Tributário

## 🎨 Personalização do Tema

### Cores da Vipal (Já Configuradas)
- **Azul Primário**: #003A70
- **Vermelho Secundário**: #E2001A
- **Fundo Escuro**: #0B0E14

### Para Alterar Cores
Edite `utils/theme.py`:
```python
VIPAL_COLORS = {
    "primary": "#003A70",      # Sua cor primária
    "secondary": "#E2001A",    # Sua cor secundária
    # ... outras cores
}
```

## 🔧 Solução de Problemas

### Erro: "Unable to create Page"
- Certifique-se de que todos os arquivos estão no local correto
- Verifique se as dependências foram instaladas

### Erro: "No module named 'streamlit'"
```bash
pip install streamlit pandas plotly numpy
```

### Bancos não encontrados
- O sistema automaticamente usa dados demo
- Verifique os caminhos em `consolidated_db.py`

### Porta 8501 ocupada
```bash
streamlit run app.py --server.port 8502
```

## 📱 Acesso Remoto

### Para acessar de outros dispositivos na rede:
```bash
streamlit run app.py --server.address 0.0.0.0
```

### Para deploy em produção:
- Use um servidor web (nginx)
- Configure SSL/HTTPS
- Use um gerenciador de processos (PM2, systemd)

## 🔄 Atualizações

### Para atualizar o sistema:
```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

## 📞 Suporte

- **Repositório**: https://github.com/ggrighi15/fusione-core-system
- **Issues**: Reporte problemas no GitHub
- **Documentação**: README.md

---

**Fusione Core System** - Desenvolvido para Vipal
