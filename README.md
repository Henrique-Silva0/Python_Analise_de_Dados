# 📊 Dashboard de Vendas

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly"/>
</p>

## 📋 Sobre o Projeto
Este projeto foi desenvolvido com o objetivo de colocar em prática meus conhecimentos em Python e Análise de Dados.

Dashboard interativo desenvolvido em **Streamlit** para análise de dados de vendas entre 2012 e 2015. O painel permite explorar indicadores de desempenho comercial através de filtros dinâmicos e visualizações intuitivas.

---

## ✨ Funcionalidades

### 🎯 KPIs Principais
| Indicador | Descrição |
|-----------|-----------|
| **Faturamento** | Total de vendas em R$ |
| **Qtde_Vendas** | Número total de transações |
| **Ticket_Médio** | Valor médio por venda |
| **Qtde_Produtos** | Variedade de produtos vendidos |

### 🔍 Filtros Disponíveis
- 📅 **Período**: Data inicial e final
- 🗺️ **Estado**: Filtro por região
- 📦 **Categoria**: Segmentação por tipo de produto
- 📆 **Ano e Mês**: Análise temporal detalhada

### 📈 Visualizações

| Gráfico | Tipo | Descrição |
|---------|------|-----------|
| Faturamento por Segmento | Pizza | Distribuição entre Doméstico, Corporativo e Industrial |
| Faturamento por Mês | Barras | Evolução mensal das vendas |
| Faturamento por Vendedor | Barras Horizontais | Ranking de performance dos vendedores |
| Quantidade por Loja | Barras | Volume de vendas por código de loja |
| Correlação entre Variáveis | Matriz Heatmap | Relação entre indicadores |
| Tendência das Variáveis | Linha | Evolução temporal das métricas |

---

## 🚀 Como Executar

### Pré-requisitos

```bash
Python 3.8+
pip
```

### Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/dashboard-vendas.git
cd dashboard-vendas
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute o dashboard**
```bash
streamlit run app.py
```

---

## 📦 Dependências

```txt
streamlit
pandas
plotly
numpy
```

---

## 📊 Insights do Dashboard

### Resumo Executivo

> Entre 2012 e 2015, houve aumento no volume de vendas, porém queda no ticket médio. O segmento **Corporativo** lidera o faturamento, e os vendedores **Artur Moreira** e **Josias Silva** se destacam como os mais produtivos.

### Principais Descobertas

- 📈 **Segmento Corporativo**: Representa 67,6% do faturamento total
- 👤 **Top Vendedor**: Artur Moreira com R$ 913.187,89
- 🏪 **Loja Destaque**: SP8822 com 98 vendas
- 📉 **Correlação Negativa**: Ano x Ticket Médio (-0.92)

---

## 🗂️ Estrutura do Projeto

```
dashboard-vendas/
├── 📄 app.py              # Aplicação principal
├── 📁 data/
│   └── vendas.csv         # Base de dados
├── 📁 components/
│   ├── filters.py         # Componentes de filtros
│   └── charts.py          # Componentes de gráficos
├── 📄 requirements.txt    # Dependências
└── 📄 README.md           # Documentação
```

---

## 🖼️ Screenshots

## 🖼️ Screenshots

<p align="center">
  <img src="https://github.com/Henrique-Silva0/Python_Analise_de_Dados/blob/main/Captura%20de%20tela%202026-01-30%20234708.png?raw=true" 
       alt="Visão Geral" width="80%"/>
</p>

<p align="center">
  <img src="https://github.com/Henrique-Silva0/Python_Analise_de_Dados/blob/main/Captura%20de%20tela%202026-01-30%20234721.png?raw=true" 
       alt="Análises" width="80%"/>
</p>

---


## 🛠️ Tecnologias Utilizadas

- **[Streamlit](https://streamlit.io/)** - Framework para criação de dashboards
- **[Pandas](https://pandas.pydata.org/)** - Manipulação de dados
- **[Plotly](https://plotly.com/)** - Visualizações interativas
- **[NumPy](https://numpy.org/)** - Computação numérica

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

Desenvolvido com ❤️ 

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/seu-perfil)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/seu-usuario)

---

<p align="center">
  ⭐ Se este projeto foi útil, considere dar uma estrela!
</p>
