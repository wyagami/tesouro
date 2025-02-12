import streamlit as st
import random

# Configurar o layout e título da página
st.set_page_config(page_title="Advinhe o Numero", layout="centered")
st.title("Advinhe o Numero")
st.sidebar.header("Instruções")
st.sidebar.write("""
- Um jogo chamado "Caça ao Tesouro" . O objetivo do jogador é encontrar um tesouro escondido em uma grade 5x5. Cada vez que o jogador escolhe uma posição, o jogo informa se ele está "quente" (próximo) ou "frio" (distante) do tesouro.
- Boa sorte!
- Caso tenha alguma idéia para publicarmos, envie uma mensagem para: 11-990000425 (Willian)
- Contribua com qualquer valor para mantermos a pagina no ar. PIX (wpyagami@gmail.com)
""")

# Função principal do jogo
def caça_ao_tesouro():
    st.title("🗺️ Caça ao Tesouro 🗺️")

    # Inicializa o estado da sessão
    if 'tesouro' not in st.session_state:
        st.session_state.tesouro = (random.randint(0, 4), random.randint(0, 4))  # Posição do tesouro
        st.session_state.tentativas = 0
        st.session_state.encontrado = False

    # Exibe instruções
    st.write("Encontre o tesouro escondido na grade 5x5!")
    st.write("Cada vez que você escolher uma posição, o jogo dirá se você está 'quente' ou 'frio'.")

    # Grade de escolha
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("Escolher (0, 0)"):
            verificar_tesouro(0, 0)
    with col2:
        if st.button("Escolher (0, 1)"):
            verificar_tesouro(0, 1)
    with col3:
        if st.button("Escolher (0, 2)"):
            verificar_tesouro(0, 2)
    with col4:
        if st.button("Escolher (0, 3)"):
            verificar_tesouro(0, 3)
    with col5:
        if st.button("Escolher (0, 4)"):
            verificar_tesouro(0, 4)

    with col1:
        if st.button("Escolher (1, 0)"):
            verificar_tesouro(1, 0)
    with col2:
        if st.button("Escolher (1, 1)"):
            verificar_tesouro(1, 1)
    with col3:
        if st.button("Escolher (1, 2)"):
            verificar_tesouro(1, 2)
    with col4:
        if st.button("Escolher (1, 3)"):
            verificar_tesouro(1, 3)
    with col5:
        if st.button("Escolher (1, 4)"):
            verificar_tesouro(1, 4)

    with col1:
        if st.button("Escolher (2, 0)"):
            verificar_tesouro(2, 0)
    with col2:
        if st.button("Escolher (2, 1)"):
            verificar_tesouro(2, 1)
    with col3:
        if st.button("Escolher (2, 2)"):
            verificar_tesouro(2, 2)
    with col4:
        if st.button("Escolher (2, 3)"):
            verificar_tesouro(2, 3)
    with col5:
        if st.button("Escolher (2, 4)"):
            verificar_tesouro(2, 4)

    with col1:
        if st.button("Escolher (3, 0)"):
            verificar_tesouro(3, 0)
    with col2:
        if st.button("Escolher (3, 1)"):
            verificar_tesouro(3, 1)
    with col3:
        if st.button("Escolher (3, 2)"):
            verificar_tesouro(3, 2)
    with col4:
        if st.button("Escolher (3, 3)"):
            verificar_tesouro(3, 3)
    with col5:
        if st.button("Escolher (3, 4)"):
            verificar_tesouro(3, 4)

    with col1:
        if st.button("Escolher (4, 0)"):
            verificar_tesouro(4, 0)
    with col2:
        if st.button("Escolher (4, 1)"):
            verificar_tesouro(4, 1)
    with col3:
        if st.button("Escolher (4, 2)"):
            verificar_tesouro(4, 2)
    with col4:
        if st.button("Escolher (4, 3)"):
            verificar_tesouro(4, 3)
    with col5:
        if st.button("Escolher (4, 4)"):
            verificar_tesouro(4, 4)

    # Exibe a pontuação e o status
    st.write(f"Tentativas: {st.session_state.tentativas}")
    if st.session_state.encontrado:
        st.success("🎉 Parabéns! Você encontrou o tesouro! 🎉")
        if st.button("Reiniciar Jogo"):
            reiniciar_jogo()

# Função para verificar a posição escolhida
def verificar_tesouro(x, y):
    st.session_state.tentativas += 1
    tesouro_x, tesouro_y = st.session_state.tesouro

    if (x, y) == (tesouro_x, tesouro_y):
        st.session_state.encontrado = True
    else:
        distancia = abs(x - tesouro_x) + abs(y - tesouro_y)
        if distancia <= 2:
            st.info("🔥 Você está quente!")
        else:
            st.info("❄️ Você está frio!")

# Função para reiniciar o jogo
def reiniciar_jogo():
    st.session_state.tesouro = (random.randint(0, 4), random.randint(0, 4))
    st.session_state.tentativas = 0
    st.session_state.encontrado = False
    st.rerun()

# Executa o jogo
if __name__ == "__main__":
    caça_ao_tesouro()