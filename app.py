import streamlit as st

# Inicializar variables de puntaje
if 'player1_scores' not in st.session_state:
    st.session_state.player1_scores = {
        'ones': 0,
        'twos': 0,
        'threes': 0,
        'fours': 0,
        'fives': 0,
        'sixes': 0,
        'three_of_a_kind': 0,
        'four_of_a_kind': 0,
        'full_house': 0,
        'small_straight': 0,
        'large_straight': 0,
        'yahtzee': 0,
        'chance': 0,
    }

if 'player2_scores' not in st.session_state:
    st.session_state.player2_scores = {
        'ones': 0,
        'twos': 0,
        'threes': 0,
        'fours': 0,
        'fives': 0,
        'sixes': 0,
        'three_of_a_kind': 0,
        'four_of_a_kind': 0,
        'full_house': 0,
        'small_straight': 0,
        'large_straight': 0,
        'yahtzee': 0,
        'chance': 0,
    }

def calculate_total_score(scores):
    upper_section_total = sum(scores[category] for category in ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes'])
    bonus = 35 if upper_section_total >= 63 else 0
    lower_section_total = sum(scores[category] for category in ['three_of_a_kind', 'four_of_a_kind', 'full_house', 'small_straight', 'large_straight', 'yahtzee', 'chance'])
    total_score = upper_section_total + bonus + lower_section_total
    return total_score, bonus

# Título de la aplicación
st.title("Puntaje del Juego de Yahtzee")

# Campos de entrada para los puntajes de los jugadores
st.header("Jugador 1")
st.session_state.player1_scores['ones'] = st.number_input("Unos (Jugador 1)", min_value=0, max_value=5*1, step=1, value=st.session_state.player1_scores['ones'])
st.session_state.player1_scores['twos'] = st.number_input("Doses (Jugador 1)", min_value=0, max_value=5*2, step=1, value=st.session_state.player1_scores['twos'])
st.session_state.player1_scores['threes'] = st.number_input("Treses (Jugador 1)", min_value=0, max_value=5*3, step=1, value=st.session_state.player1_scores['threes'])
st.session_state.player1_scores['fours'] = st.number_input("Cuatros (Jugador 1)", min_value=0, max_value=5*4, step=1, value=st.session_state.player1_scores['fours'])
st.session_state.player1_scores['fives'] = st.number_input("Cincos (Jugador 1)", min_value=0, max_value=5*5, step=1, value=st.session_state.player1_scores['fives'])
st.session_state.player1_scores['sixes'] = st.number_input("Seises (Jugador 1)", min_value=0, max_value=5*6, step=1, value=st.session_state.player1_scores['sixes'])

st.header("Jugador 2")
st.session_state.player2_scores['ones'] = st.number_input("Unos (Jugador 2)", min_value=0, max_value=5*1, step=1, value=st.session_state.player2_scores['ones'])
st.session_state.player2_scores['twos'] = st.number_input("Doses (Jugador 2)", min_value=0, max_value=5*2, step=1, value=st.session_state.player2_scores['twos'])
st.session_state.player2_scores['threes'] = st.number_input("Treses (Jugador 2)", min_value=0, max_value=5*3, step=1, value=st.session_state.player2_scores['threes'])
st.session_state.player2_scores['fours'] = st.number_input("Cuatros (Jugador 2)", min_value=0, max_value=5*4, step=1, value=st.session_state.player2_scores['fours'])
st.session_state.player2_scores['fives'] = st.number_input("Cincos (Jugador 2)", min_value=0, max_value=5*5, step=1, value=st.session_state.player2_scores['fives'])
st.session_state.player2_scores['sixes'] = st.number_input("Seises (Jugador 2)", min_value=0, max_value=5*6, step=1, value=st.session_state.player2_scores['sixes'])

# Campos de entrada para la sección inferior de los jugadores
st.header("Sección Inferior")

st.subheader("Jugador 1")
st.session_state.player1_scores['three_of_a_kind'] = st.number_input("Trio (Jugador 1)", min_value=0, step=1, value=st.session_state.player1_scores['three_of_a_kind'])
st.session_state.player1_scores['four_of_a_kind'] = st.number_input("Póker (Jugador 1)", min_value=0, step=1, value=st.session_state.player1_scores['four_of_a_kind'])
st.session_state.player1_scores['full_house'] = st.number_input("Full House (Jugador 1)", min_value=0, step=1, value=st.session_state.player1_scores['full_house'])
st.session_state.player1_scores['small_straight'] = st.number_input("Escalera Pequeña (Jugador 1)", min_value=0, step=1, value=st.session_state.player1_scores['small_straight'])
st.session_state.player1_scores['large_straight'] = st.number_input("Escalera Grande (Jugador 1)", min_value=0, step=1, value=st.session_state.player1_scores['large_straight'])
st.session_state.player1_scores['yahtzee'] = st.number_input("Yahtzee (Jugador 1)", min_value=0, step=1, value=st.session_state.player1_scores['yahtzee'])
st.session_state.player1_scores['chance'] = st.number_input("Chance (Jugador 1)", min_value=0, step=1, value=st.session_state.player1_scores['chance'])

st.subheader("Jugador 2")
st.session_state.player2_scores['three_of_a_kind'] = st.number_input("Trio (Jugador 2)", min_value=0, step=1, value=st.session_state.player2_scores['three_of_a_kind'])
st.session_state.player2_scores['four_of_a_kind'] = st.number_input("Póker (Jugador 2)", min_value=0, step=1, value=st.session_state.player2_scores['four_of_a_kind'])
st.session_state.player2_scores['full_house'] = st.number_input("Full House (Jugador 2)", min_value=0, step=1, value=st.session_state.player2_scores['full_house'])
st.session_state.player2_scores['small_straight'] = st.number_input("Escalera Pequeña (Jugador 2)", min_value=0, step=1, value=st.session_state.player2_scores['small_straight'])
st.session_state.player2_scores['large_straight'] = st.number_input("Escalera Grande (Jugador 2)", min_value=0, step=1, value=st.session_state.player2_scores['large_straight'])
st.session_state.player2_scores['yahtzee'] = st.number_input("Yahtzee (Jugador 2)", min_value=0, step=1, value=st.session_state.player2_scores['yahtzee'])
st.session_state.player2_scores['chance'] = st.number_input("Chance (Jugador 2)", min_value=0, step=1, value=st.session_state.player2_scores['chance'])

# Calcular el puntaje total para cada jugador
player1_total_score, player1_bonus = calculate_total_score(st.session_state.player1_scores)
player2_total_score, player2_bonus = calculate_total_score(st.session_state.player2_scores)

# Mostrar el puntaje total y la bonificación para cada jugador
st.header("Puntaje Total")
st.subheader("Jugador 1")
st.write(f"Bonificación: {player1_bonus}")
st.write(f"Puntaje Total: {player1_total_score}")

st.subheader("Jugador 2")
st.write(f"Bonificación: {player2_bonus}")
st.write(f"Puntaje Total: {player2_total_score}")
