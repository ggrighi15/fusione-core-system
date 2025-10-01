# 🛠️ Configuração do VS Code - Fusione Core System

## 📋 Visão Geral

Este guia configura o **Visual Studio Code** para desenvolvimento otimizado do Fusione Core System, incluindo integração com bancos de dados, debugging e tema personalizado da Vipal.

## 🚀 Configuração Rápida

### 1. **Abrir o Projeto**
```bash
# Clonar o repositório
git clone https://github.com/ggrighi15/fusione-core-system.git
cd fusione-core-system

# Abrir no VS Code
code fusione-core-system.code-workspace
```

### 2. **Instalar Extensões Recomendadas**
O VS Code automaticamente sugerirá as extensões necessárias. Clique em **"Install All"** quando aparecer a notificação.

**Extensões Principais:**
- **Python** - Suporte completo ao Python
- **Python Debugger** - Debug avançado
- **Jupyter** - Notebooks integrados
- **SQLTools** - Gerenciamento de bancos
- **GitHub Copilot** - IA para desenvolvimento
- **Markdown** - Documentação

### 3. **Configurar Ambiente Python**
```bash
# Criar ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt
```

## 🎨 Tema Vipal Configurado

### **Cores Aplicadas**
- **Activity Bar:** Azul Vipal (#003A70)
- **Status Bar:** Azul Vipal (#003A70)
- **Title Bar:** Azul Vipal (#003A70)
- **Tema Base:** Deep Blue (escuro elegante)

### **Personalização Adicional**
As cores podem ser ajustadas em `.vscode/settings.json`:
```json
"workbench.colorCustomizations": {
    "activityBar.background": "#003A70",
    "statusBar.background": "#003A70",
    "titleBar.activeBackground": "#003A70"
}
```

## 🗄️ Conexões de Banco Configuradas

### **SQLite (Desenvolvimento)**
- **Contencioso:** `./sql/contencioso.sqlite`
- **Geral:** `./sql/geral.sqlite`
- **Clientes:** `./sql/clientes.sqlite`

### **Bancos Consolidados (Produção)**
- **Contencioso:** `c:\consolidados\fusione_contencioso_consolidado.db`
- **Pessoas:** `c:\consolidados\pessoas.db`
- **Contratos:** `c:\consolidados\contratos.db`
- **Requisições:** `c:\consolidados\requisicoes.sqlite`

### **MariaDB (Produção)**
- **Host:** localhost:3306
- **Database:** fusione
- **Usuário:** root

## ⚡ Tarefas Configuradas

### **Executar via Command Palette (Ctrl+Shift+P)**

#### **🚀 Run Streamlit App**
- **Comando:** `Tasks: Run Task` → `🚀 Run Streamlit App`
- **Função:** Inicia o Dashboard Executivo
- **URL:** http://localhost:8501

#### **📦 Install Dependencies**
- **Comando:** `Tasks: Run Task` → `📦 Install Dependencies`
- **Função:** Instala todas as dependências

#### **🗄️ Create Demo Databases**
- **Comando:** `Tasks: Run Task` → `🗄️ Create Demo Databases`
- **Função:** Cria bancos SQLite com dados demo

#### **🧪 Run Tests**
- **Comando:** `Tasks: Run Task` → `🧪 Run Tests`
- **Função:** Executa testes automatizados

#### **📊 Open Dashboard**
- **Comando:** `Tasks: Run Task` → `📊 Open Dashboard`
- **Função:** Abre o dashboard no navegador

## 🐛 Configurações de Debug

### **Configurações Disponíveis**

#### **🐛 Debug Streamlit App**
- Debug completo da aplicação principal
- Breakpoints em qualquer arquivo
- Console integrado

#### **📊 Debug Dashboard**
- Debug específico do Dashboard Executivo
- Ideal para desenvolvimento de KPIs

#### **🗄️ Debug Database Manager**
- Debug do gerenciador de bancos
- Útil para problemas de conexão

#### **🎨 Debug Theme**
- Debug do sistema de temas
- Para ajustes visuais

### **Como Usar o Debug**
1. Abra o arquivo que deseja debugar
2. Coloque breakpoints (F9)
3. Pressione F5 ou vá em **Run → Start Debugging**
4. Escolha a configuração apropriada

## 📁 Estrutura de Arquivos VS Code

```
.vscode/
├── settings.json          # Configurações do workspace
├── tasks.json            # Tarefas automatizadas
├── launch.json           # Configurações de debug
└── extensions.json       # Extensões recomendadas
```

## 🔧 Configurações Avançadas

### **Formatação Automática**
- **Formatter:** Black (Python)
- **Format on Save:** Habilitado
- **Organize Imports:** Automático

### **Linting**
- **Pylint:** Habilitado
- **Verificação em tempo real**
- **Correções automáticas**

### **Auto Save**
- **Delay:** 1 segundo
- **Salva automaticamente** durante digitação

## 🚀 Atalhos Úteis

### **Desenvolvimento**
- **Ctrl+Shift+P:** Command Palette
- **F5:** Start Debugging
- **Ctrl+F5:** Run Without Debugging
- **Ctrl+Shift+`:** Novo Terminal

### **Streamlit**
- **Ctrl+Shift+P → Tasks:** Executar tarefas
- **F1 → SQLTools:** Gerenciar bancos
- **Ctrl+K Ctrl+O:** Abrir workspace

## 🔍 Solução de Problemas

### **Python não encontrado**
1. Instale Python 3.11+
2. Configure o interpretador: **Ctrl+Shift+P → Python: Select Interpreter**
3. Escolha o Python correto

### **Extensões não instaladas**
1. **Ctrl+Shift+X** para abrir Extensions
2. Procure por "Python" e instale
3. Reinicie o VS Code

### **Bancos não conectam**
1. Verifique se os arquivos SQLite existem
2. Execute a tarefa **Create Demo Databases**
3. Teste conexão via SQLTools

### **Streamlit não inicia**
1. Verifique se está instalado: `pip install streamlit`
2. Execute via terminal: `streamlit run app.py`
3. Verifique a porta 8501

## 📚 Recursos Adicionais

### **Documentação**
- [Python no VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [SQLTools Extension](https://vscode-sqltools.mteixeira.dev/)
- [Streamlit Docs](https://docs.streamlit.io/)

### **Shortcuts Personalizados**
Adicione em **File → Preferences → Keyboard Shortcuts**:
```json
{
    "key": "ctrl+alt+s",
    "command": "workbench.action.tasks.runTask",
    "args": "🚀 Run Streamlit App"
}
```

---

**VS Code Setup** - Fusione Core System v2.0  
**Desenvolvido para:** Vipal  
**Última atualização:** Setembro 2025
