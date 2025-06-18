import streamlit as st
import pandas as pd

# ========== CONFIG ==========
st.set_page_config(page_title="Motocycles Data App", layout="wide")

# ========== DARK MODE STYLE ==========
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #ffffff;
    }
    .title {
        font-size: 36px;
        color: #ffffff;
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .description {
        font-size: 18px;
        color: #dcdcdc;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        font-size: 14px;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        margin: 5px 0px;
        transition: 0.3s;
        border: none;
    }
    .stButton>button:hover {
        background-color: #166ca0;
    }
    .stSidebar {
        background-color: #1e1e1e;
    }
    hr {
        margin-top: 50px;
        border-color: #444;
    }
    </style>
""", unsafe_allow_html=True)

# ========== TITRE ET DESCRIPTION ==========
st.markdown("<div class='title'>🏍️ MY DATA APP</div>", unsafe_allow_html=True)
st.markdown("<div class='description'>Explore motorcycle listings scraped from Expat-Dakar</div>", unsafe_allow_html=True)

# ========== SIDEBAR ==========
with st.sidebar:
    st.image("https://www.expat-dakar.com/assets/logo.png", width=150)
    st.markdown("## 📂 Choisissez un dataset")
    st.write("Cliquez sur un bouton pour afficher les données.")
    st.markdown("---")
    st.markdown("### 🛠️ Technologies utilisées")
    st.markdown("""
    * 📦 **Librairies Python**: base64, pandas, streamlit  
    * 🌐 **Source**: [Expat-Dakar](https://www.expat-dakar.com/)
    """)

# ========== FONCTION D'AFFICHAGE ==========
def load_(dataframe, title, key):
    if st.button(title, key):
        with st.expander(f"🔍 Aperçu de {title}"):
            st.write(f"**Dimensions**: {dataframe.shape[0]} lignes × {dataframe.shape[1]} colonnes")
            st.dataframe(dataframe)

# ========== AFFICHAGE EN 2 COLONNES ==========
col1, col2 = st.columns(2)

with col1:
    load_(pd.read_csv('data/motos_scooters1.csv'), '📄 Motocycles data 1', '1')
    load_(pd.read_csv('data/motos_scooters3.csv'), '📄 Motocycles data 3', '3')
    load_(pd.read_csv('data/motos_scooters5.csv'), '📄 Motocycles data 5', '5')

with col2:
    load_(pd.read_csv('data/motos_scooters2.csv'), '📄 Motocycles data 2', '2')
    load_(pd.read_csv('data/motos_scooters4.csv'), '📄 Motocycles data 4', '4')

# ========== FOOTER ==========
st.markdown("""<hr>
<div style='text-align: center; color: #aaaaaa; font-size: 14px;'>
    Made with ❤️ by Alioune Mbodji – Powered by Streamlit
</div>
""", unsafe_allow_html=True)
#Test de webhook
