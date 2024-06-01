import streamlit as st

# Inicializar variables de puntaje y nombres de jugadores
if 'player1_name' not in st.session_state:
    st.session_state.player1_name = 'Jugador 1'
if 'player2_name' not in st.session_state:
    st.session_state.player2_name = 'Jugador 2'

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
    return upper_section_total, bonus, lower_section_total, total_score

# Título de la aplicación
st.title("Puntaje del Juego de Yahtzee")

# Campos para ingresar los nombres de los jugadores
col1, col2 = st.columns(2)
with col1:
    st.session_state.player1_name = st.text_input("Nombre del Jugador 1", value=st.session_state.player1_name)
with col2:
    st.session_state.player2_name = st.text_input("Nombre del Jugador 2", value=st.session_state.player2_name)

# Campos de entrada para los puntajes de los jugadores
st.header("Sección Superior")

col1, col2 = st.columns(2)

with col1:
    st.subheader(st.session_state.player1_name)
    st.session_state.player1_scores['ones'] = st.number_input("Unos", min_value=0, max_value=5*1, step=1, value=st.session_state.player1_scores['ones'])
    st.session_state.player1_scores['twos'] = st.number_input("Doses", min_value=0, max_value=5*2, step=1, value=st.session_state.player1_scores['twos'])
    st.session_state.player1_scores['threes'] = st.number_input("Treses", min_value=0, max_value=5*3, step=1, value=st.session_state.player1_scores['threes'])
    st.session_state.player1_scores['fours'] = st.number_input("Cuatros", min_value=0, max_value=5*4, step=1, value=st.session_state.player1_scores['fours'])
    st.session_state.player1_scores['fives'] = st.number_input("Cincos", min_value=0, max_value=5*5, step=1, value=st.session_state.player1_scores['fives'])
    st.session_state.player1_scores['sixes'] = st.number_input("Seises", min_value=0, max_value=5*6, step=1, value=st.session_state.player1_scores['sixes'])
    upper1, bonus1, lower1, total1 = calculate_total_score(st.session_state.player1_scores)
    st.write(f"Total Sección Superior: {upper1}")
    if bonus1 > 0:
        st.write(f"Bonificación: {bonus1}")

with col2:
    st.subheader(st.session_state.player2_name)
    st.session_state.player2_scores['ones'] = st.number_input("Unos", min_value=0, max_value=5*1, step=1, value=st.session_state.player2_scores['ones'])
    st.session_state.player2_scores['twos'] = st.number_input("Doses", min_value=0, max_value=5*2, step=1, value=st.session_state.player2_scores['twos'])
    st.session_state.player2_scores['threes'] = st.number_input("Treses", min_value=0, max_value=5*3, step=1, value=st.session_state.player2_scores['threes'])
    st.session_state.player2_scores['fours'] = st.number_input("Cuatros", min_value=0, max_value=5*4, step=1, value=st.session_state.player2_scores['fours'])
    st.session_state.player2_scores['fives'] = st.number_input("Cincos", min_value=0, max_value=5*5, step=1, value=st.session_state.player2_scores['fives'])
    st.session_state.player2_scores['sixes'] = st.number_input("Seises", min_value=0, max_value=5*6, step=1, value=st.session_state.player2_scores['sixes'])
    upper2, bonus2, lower2, total2 = calculate_total_score(st.session_state.player2_scores)
    st.write(f"Total Sección Superior: {upper2}")
    if bonus2 > 0:
        st.write(f"Bonificación: {bonus2}")

st.header("Sección Inferior")

col1, col2 = st.columns(2)

with col1:
    st.subheader(st.session_state.player1_name)
    st.session_state.player1_scores['three_of_a_kind'] = st.number_input("Trio", min_value=0, step=1, value=st.session_state.player1_scores['three_of_a_kind'])
    st.session_state.player1_scores['four_of_a_kind'] = st.number_input("Póker", min_value=0, step=1, value=st.session_state.player1_scores['four_of_a_kind'])
    st.session_state.player1_scores['full_house'] = st.number_input("Full House", min_value=0, step=1, value=st.session_state.player1_scores['full_house'])
    st.session_state.player1_scores['small_straight'] = st.number_input("Escalera Pequeña", min_value=0, step=1, value=st.session_state.player1_scores['small_straight'])
    st.session_state.player1_scores['large_straight'] = st.number_input("Escalera Grande", min_value=0, step=1, value=st.session_state.player1_scores['large_straight'])
    st.session_state.player1_scores['yahtzee'] = st.number_input("Yahtzee", min_value=0, step=1, value=st.session_state.player1_scores['yahtzee'])
    st.session_state.player1_scores['chance'] = st.number_input("Chance", min_value=0, step=1, value=st.session_state.player1_scores['chance'])
    upper1, bonus1, lower1, total1 = calculate_total_score(st.session_state.player1_scores)
    st.write(f"Total Sección Inferior: {lower1}")
    st.write(f"Total Sección Superior: {upper1}")
    st.write(f"Bonificación: {bonus1}")
    st.write(f"Puntaje Total: {total1}")

with col2:
    st.subheader(st.session_state.player2_name)
    st.session_state.player2_scores['three_of_a_kind'] = st.number_input("Trio", min_value=0, step=1, value=st.session_state.player2_scores['three_of_a_kind'])
    st.session_state.player2_scores['four_of_a_kind'] = st.number_input("Póker", min_value=0, step=1, value=st.session_state.player2_scores['four_of_a_kind'])
    st.session_state.player2_scores['full_house'] = st.number_input("Full House", min_value=0, step=1, value=st.session_state.player2_scores['full_house'])
    st.session_state.player2_scores['small_straight'] = st.number_input("Escalera Pequeña", min_value=0, step=1, value=st.session_state.player2_scores['small_straight'])
    st.session_state.player2_scores['large_straight'] = st.number_input("Escalera Grande", min_value=0, step=1, value=st.session_state.player2_scores['large_straight'])
    st.session_state.player2_scores['yahtzee'] = st.number_input("Yahtzee", min_value=0, step=1, value=st.session_state.player2_scores['yahtzee'])
    st.session_state.player2_scores['chance'] = st.number_input("Chance", min_value=0, step=1, value=st.session_state.player2_scores['chance'])
    upper2, bonus2, lower2, total2 = calculate_total_score(st.session_state.player2_scores)
    st.write(f"Total Sección Inferior: {lower2}")
    st.write(f"Total Sección Superior: {upper2}")
    st.write(f"Bonificación: {bonus2}")
    st.write(f"Puntaje Total: {total2}")
