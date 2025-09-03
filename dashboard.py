import streamlit as st
import pandas as pd
import plotly.express as px
#Importação dos Módulo que geram os gráficos
from src import info_pessoais, equipa_eletro, trabalho, use_tech, midia, interesses, motivacoes, dreams

# Função para carregar os dados
@st.cache(allow_output_mutation=True)
def load_data(file):
    return pd.read_excel(file)


# Função principal
def dashboard():
    st.sidebar.image("public/logo.png", width=220)
    st.sidebar.title("Menu")
    
    # Ícones para cada página
    icons = {
        "Home": "🏠",
        "Informações Pessoais": "👤",
        "Equipamentos Eletrônicos": "💻",
        "Trabalho": "💼",
        "Uso de Tecnologia e Informática": "🖥️",
        "Mídia e Leitura": "📚",
        "Interesses Culturais": "🎭",
        "Motivações para Estudo na FATEC Franca": "🎓",
        "Sobre a Pessoa": "❔"
    }

    # Selecionar página na sidebar
    page = st.sidebar.selectbox("Selecione uma página", list(icons.keys()), format_func=lambda x: f"{icons[x]} {x}")

    if page == "Home":
        st.title('Dashboard de Dados - EasyPSE 1.0')
        st.title("Bem-vindo ao seu Dashboard! 👋")
        uploaded_file = st.file_uploader("Escolha um arquivo .xlsx", type="xlsx")
        if uploaded_file is not None:
            st.session_state.data = load_data(uploaded_file)
            st.success("Arquivo carregado com sucesso! Selecione uma página para visualizar os dados.")

        #Explicação de como utilizar a página
        st.markdown("""
        ### Como Utilizar o EasyPSE:

        **1. Página Inicial (Home):**
        - Ao acessar o dashboard, você será direcionado para a página inicial.
        - Nessa página, você verá um botão com a opção "Escolha um arquivo .xlsx".
        - Clique nesse botão para fazer upload de um arquivo Excel (.xlsx) contendo os dados que deseja analisar.

        **2. Navegação:**
        - **Menu Lateral:**
            - No menu lateral esquerdo, você encontrará as diferentes páginas disponíveis para análise.
            - As opções incluem "Informações Pessoais", "Equipamentos Eletrônicos", "Trabalho", "Uso de Tecnologia e Informática", "Mídia e Leitura", "Interesses Culturais", "Motivações para Estudo na FATEC Franca" e "Sobre a Pessoa".
            - Selecione uma dessas páginas para visualizar os dados e gráficos relacionados ao respectivo tópico.

        **3. Visualização de Dados:**
        - Cada página de análise exibirá gráficos e visualizações interativas com base nos dados carregados.
        - Os gráficos podem incluir gráficos de pizza, gráficos de barra, gráficos de dispersão e outros tipos de visualizações.
        - Explore os diferentes gráficos para entender melhor os padrões e tendências nos dados.

        **4. Interatividade:**
        - Muitos dos gráficos oferecem funcionalidades interativas, como zoom, seleção de dados e filtros.
        - Utilize essas opções interativas para explorar os dados de maneira mais detalhada e dinâmica.

        **5. Atualização de Dados:**
        - Se desejar atualizar os dados para análise, você pode retornar à página inicial clicando em "Home" no menu lateral.
        - Faça upload de um novo arquivo Excel para substituir os dados existentes pelos novos dados carregados.
        """)


    if page != "Home":
        st.title(page)

        if page == "Informações Pessoais":
            if 'data' in st.session_state:
                df = st.session_state.data
                info_pessoais.render_info_pessoais(df)
            

        elif page == "Equipamentos Eletrônicos":

            if 'data' in st.session_state:
                df = st.session_state.data
                equipa_eletro.render_equipamentos(df)
                

        elif page == "Trabalho":

            if 'data' in st.session_state:
                df = st.session_state.data
                trabalho.render_trabalho(df)

        elif page == "Uso de Tecnologia e Informática":

            if 'data' in st.session_state:
                df = st.session_state.data
                use_tech.render_user_tech(df)
                
            
        elif page == "Mídia e Leitura":
        
            if 'data' in st.session_state:
                df = st.session_state.data
                midia.render_midia(df)

        elif page == "Interesses Culturais":

            if 'data' in st.session_state:
                df = st.session_state.data
                interesses.render_interesses(df)


        elif page == "Motivações para Estudo na FATEC Franca":

            if 'data' in st.session_state:
                df = st.session_state.data
                motivacoes.render_motivacoes(df)
        else:

            if 'data' in st.session_state:
                df = st.session_state.data
                dreams.render_dreams(df)

            
    st.markdown("---")
    st.write("&copy; 2024 EasyPSE - All rights reserved", unsafe_allow_html=True)


    page_bg_img =  f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://static.vecteezy.com/system/resources/previews/026/867/188/original/blue-wave-footer-free-png.png");
    background-size: 100% 5%;
    background-position: left bottom;
    background-repeat: no-repeat;
    background-attachment: local, scroll;
    }}
    </style>
    """
    st.sidebar.markdown(page_bg_img, unsafe_allow_html=True)

if __name__ == "__main__":
    dashboard()
