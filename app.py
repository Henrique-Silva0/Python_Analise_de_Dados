import streamlit as st
import streamlit.components.v1 as components

# Configurações da página
st.set_page_config(page_title="Portfólio | Henrique Silva", page_icon="🚀", layout="wide")

# Custom CSS para um visual ultra-moderno
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    /* Esconde o label do multiselect */
.stMultiSelect label {
    display: none;
}

/* Texto das opções do dropdown */
div[data-baseweb="menu"] span {
    font-size: 20px !important;
    color: white;
}

/* Fundo principal */
section[data-testid="stAppViewContainer"] {
    background-color: #badea6;
}

/* Multiselect */
div[data-testid="stMultiSelect"] > div {
    background-color: #388D2B;
    border: 2px solid #388D2B;
    border-radius: 18px;
    padding: 6px;
}

/* Hover */
div[data-testid="stMultiSelect"]:hover > div {
    background-color: #2f7a24;
}

/* Tags selecionadas do multiselect */
div[data-testid="stMultiSelect"] span[data-baseweb="tag"] {
    background-color: #28991f !important;  /* VERDE */
    color: white !important;
    border-radius: 12px;
    padding: 10px 28px;
    font-weight: 500;
}

/* Botões */
.stButton > button,
.stDownloadButton > button {
    width: 100%;
    height: 3em;
    border-radius: 6px;
    background-color: #28991f;
    color: white;
}

/* Botões da sidebar */
div[data-testid="stSidebar"] .stButton > button {
    background-color: #dc3545;
    color: white;
    border-radius: 6px;
    border: none;
}

div[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #a71d2a;
}

    /* Reset e Fonte Global */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #ffffff;
    }
    
    /* Fundo Gradiente Animado */
    .stApp {
        background: linear-gradient(-45deg, #0f172a, #1e293b, #334155, #1e1b4b);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Glassmorphism Containers */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    /* Header Styling */
    .header-container {
        text-align: center;
        padding: 3rem 1rem;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 3rem;
    }
    
    .name-title {
        background: linear-gradient(to right, #60a5fa, #a78bfa, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 800;
        letter-spacing: -0.05em;
        margin-bottom: 0.5rem;
    }
    
    .sub-title {
        color: #94a3b8;
        font-size: 1.4rem;
        font-weight: 400;
        letter-spacing: 0.1em;
        text-transform: uppercase;
    }
    
    /* Section Titles */
    .section-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .section-title::after {
        content: "";
        height: 2px;
        flex-grow: 1;
        background: linear-gradient(to right, #3b82f6, transparent);
        margin-left: 15px;
    }
    
    /* Project Cards */
    .project-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 1.5rem;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        height: 100%;
    }
    
    .project-card:hover {
        transform: translateY(-10px) scale(1.02);
        background: rgba(255, 255, 255, 0.07);
        border-color: rgba(59, 130, 246, 0.5);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
    }
    
    .project-tag {
        display: inline-block;
        background: rgba(59, 130, 246, 0.2);
        color: #60a5fa;
        padding: 0.3rem 0.8rem;
        border-radius: 8px;
        font-size: 0.7rem;
        font-weight: 600;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
        border: 1px solid rgba(59, 130, 246, 0.3);
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.95);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    /* Custom Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton>button:hover {
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.6);
        transform: scale(1.02);
    }

    /* Links */
    a {
        color: #60a5fa !important;
        text-decoration: none;
        transition: 0.3s;
    }
    
    a:hover {
        color: #93c5fd !important;
        text-shadow: 0 0 10px rgba(96, 165, 250, 0.5);
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 255, 255, 0.03);
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        color: #94a3b8;
    }

    .stTabs [aria-selected="true"] {
        background-color: rgba(59, 130, 246, 0.1) !important;
        color: #60a5fa !important;
        border-bottom: 2px solid #3b82f6 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar - Informações de Contato
with st.sidebar:
    st.markdown("<div style='text-align: center; padding: 1rem;'>", unsafe_allow_html=True)
    st.image("https://api.dicebear.com/7.x/avataaars/svg?seed=Henrique", width=120)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("### 📱 Contato")
    st.markdown("📍 Pacajus – CE")
    st.markdown("📞 (85) 9.9272-4490")
    st.markdown("📧 [hssoares0123@gmail.com](mailto:hssoares0123@gmail.com)")
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/henrique-silva-4395ab298/)")
    
    st.markdown("---")
    st.markdown("### 🛠️ Habilidades")
    st.markdown("**Hard Skills:**")
    st.markdown("`Power BI` `SQL` `Python` `Excel` `SketchUp` `PDI` `ETL`")
    
    st.markdown("**Soft Skills:**")
    st.write("✨ Comunicação Clara\n✨ Organização\n✨ Trabalho em Equipe\n✨ Raciocínio Lógico")

# Header Principal
st.markdown("""
    <div class="header-container">
        <h1 class="name-title">José Henrique Soares da Silva</h1>
        <p class="sub-title">Analista de Dados & BI Junior</p>
        <div style="margin-top: 1.5rem;">
            <span style="background: rgba(255,255,255,0.1); padding: 5px 15px; border-radius: 20px; font-size: 0.9rem; color: #cbd5e1;">
                🚀 Transformando dados em decisões estratégicas
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Layout Principal
col1, col2 = st.columns([1.6, 1])

with col1:
    st.markdown("""
        <div class="glass-card">
            <h2 class="section-title">👤 Sobre Mim</h2>
            <p style="color: #FFFFFF; line-height: 1.6; font-size: 1.1rem;">
                Profissional proativo com forte raciocínio lógico e alta capacidade de adaptação. 
                Especialista em aplicar soluções de <b>Business Intelligence</b> no setor logístico, 
                focando na otimização de processos e controle inteligente de ativos. 
                Atualmente cursando ADS e focado em evoluir na stack de dados.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glass-card">
            <h2 class="section-title">💼 Experiência</h2>
            <div style="border-left: 2px solid #3b82f6; padding-left: 20px; margin-left: 10px;">
                <h4 style="margin-bottom: 5px; color: #f8fafc;">Vectra Work – Conferente Logístico</h4>
                <p style="color: #60a5fa; font-size: 0.9rem; font-weight: 600;">Abril 2023 – Presente</p>
                <ul style="color: #94a3b8; font-size: 0.95rem;">
                    <li>Criação de Dashboards estratégicos para controle de PCM.</li>
                    <li>Automação de fluxos de estoque com Power Query e Excel.</li>
                    <li>Inovação com modelagem 3D integrada ao Power BI (3DBI).</li>
                    <li>Redução significativa de erros operacionais no recebimento.</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="glass-card">
            <h2 class="section-title">🎓 Formação</h2>
            <div style="margin-bottom: 1.5rem;">
                <p style="color: #f8fafc; font-weight: 600; margin-bottom: 0;">Análise e Desenv. de Sistemas</p>
                <p style="color: #94a3b8; font-size: 0.9rem;">Uniasselvi | 4º Semestre</p>
            </div>
            <div style="margin-bottom: 1.5rem;">
                <p style="color: #f8fafc; font-weight: 600; margin-bottom: 0;">Data Analytics</p>
                <p style="color: #94a3b8; font-size: 0.9rem;">Digital College | 2025</p>
            </div>
            <div>
                <p style="color: #f8fafc; font-weight: 600; margin-bottom: 0;">Power BI para BI e Data Science</p>
                <p style="color: #94a3b8; font-size: 0.9rem;">Data Science Academy</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Seção de Projetos
st.markdown('<h2 class="section-title">🚀 Projetos em Destaque</h2>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📊 Dashboards Power BI", "🐍 Scripts Python"])

with tab1:
    p1_col1, p1_col2 = st.columns(2)
    
    with p1_col1:
        st.markdown("""
            <div class="project-card">
                <h3 style="color: #f8fafc; margin-top: 0;">Gestão de Manutenção (PCM)</h3>
                <div style="margin-bottom: 1rem;">
                    <span class="project-tag">Power BI</span>
                    <span class="project-tag">DAX</span>
                    <span class="project-tag">Logística</span>
                </div>
                <p style="color: #94a3b8; font-size: 0.9rem;">Dashboard interativo para monitoramento de ordens de serviço, KPIs de manutenção e produtividade da equipe.</p>
            </div>
            """, unsafe_allow_html=True)
        st.button("Visualizar Dashboard", key="p1")

    with p1_col2:
        st.markdown("""
            <div class="project-card">
                <h3 style="color: #f8fafc; margin-top: 0;">Estoque Inteligente 3D</h3>
                <div style="margin-bottom: 1rem;">
                    <span class="project-tag">3DBI</span>
                    <span class="project-tag">SketchUp</span>
                    <span class="project-tag">Power BI</span>
                </div>
                <p style="color: #94a3b8; font-size: 0.9rem;">Projeto inovador que une modelagem espacial 3D com dados reais de endereçamento para gestão visual de armazéns.</p>
            </div>
            """, unsafe_allow_html=True)
        st.button("Ver Modelo 3D", key="p2")

with tab2:
    p2_col1, p2_col2 = st.columns(2)
    
    with p2_col1:
        st.markdown("""
            <div class="project-card">
                <h3 style="color: #f8fafc; margin-top: 0;">ETL & Automação Logística</h3>
                <div style="margin-bottom: 1rem;">
                    <span class="project-tag">Python</span>
                    <span class="project-tag">Pandas</span>
                    <span class="project-tag">SQL</span>
                </div>
                <p style="color: #94a3b8; font-size: 0.9rem;">Scripts para extração automática de dados do ERP, limpeza e carregamento em bases de dados otimizadas.</p>
            </div>
            """, unsafe_allow_html=True)
        with st.expander("Ver Snippet de Código"):
            st.code("""
import pandas as pd

def process_logistics_data(file_path):
    df = pd.read_csv(file_path)
    # Lógica de limpeza e transformação
    return df.groupby('status').count()
            """, language='python')

    with p2_col2:
        st.markdown("""
            <div class="project-card">
                <h3 style="color: #f8fafc; margin-top: 0;">Análise de Produtividade</h3>
                <div style="margin-bottom: 1rem;">
                    <span class="project-tag">Python</span>
                    <span class="project-tag">Plotly</span>
                    <span class="project-tag">Data Science</span>
                </div>
                <p style="color: #94a3b8; font-size: 0.9rem;">Análise estatística para identificar gargalos operacionais e sugerir melhorias baseadas em dados históricos.</p>
            </div>
            """, unsafe_allow_html=True)
        st.button("Ver Repositório GitHub", key="p4")

# Rodapé
st.markdown("""
    <div style="text-align: center; color: #64748b; font-size: 0.85rem; padding: 4rem 0 2rem 0;">
        © 2026 • José Henrique Silva • Desenvolvido com Streamlit & ❤️
    </div>
    """, unsafe_allow_html=True)