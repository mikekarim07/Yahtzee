import streamlit as st

# Inicializar variables de puntaje
if 'scores' not in st.session_state:
    st.session_state.scores = {
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

# Campos de entrada para los puntajes
st.header("Sección Superior")
st.session_state.scores['ones'] = st.number_input("Unos", min_value=0, max_value=5*1, step=1, value=st.session_state.scores['ones'])
st.session_state.scores['twos'] = st.number_input("Doses", min_value=0, max_value=5*2, step=1, value=st.session_state.scores['twos'])
st.session_state.scores['threes'] = st.number_input("Treses", min_value=0, max_value=5*3, step=1, value=st.session_state.scores['threes'])
st.session_state.scores['fours'] = st.number_input("Cuatros", min_value=0, max_value=5*4, step=1, value=st.session_state.scores['fours'])
st.session_state.scores['fives'] = st.number_input("Cincos", min_value=0, max_value=5*5, step=1, value=st.session_state.scores['fives'])
st.session_state.scores['sixes'] = st.number_input("Seises", min_value=0, max_value=5*6, step=1, value=st.session_state.scores['sixes'])

st.header("Sección Inferior")
st.session_state.scores['three_of_a_kind'] = st.number_input("Trio", min_value=0, step=1, value=st.session_state.scores['three_of_a_kind'])
st.session_state.scores['four_of_a_kind'] = st.number_input("Póker", min_value=0, step=1, value=st.session_state.scores['four_of_a_kind'])
st.session_state.scores['full_house'] = st.number_input("Full House", min_value=0, step=1, value=st.session_state.scores['full_house'])
st.session_state.scores['small_straight'] = st.number_input("Escalera Pequeña", min_value=0, step=1, value=st.session_state.scores['small_straight'])
st.session_state.scores['large_straight'] = st.number_input("Escalera Grande", min_value=0, step=1, value=st.session_state.scores['large_straight'])
st.session_state.scores['yahtzee'] = st.number_input("Yahtzee", min_value=0, step=1, value=st.session_state.scores['yahtzee'])
st.session_state.scores['chance'] = st.number_input("Chance", min_value=0, step=1, value=st.session_state.scores['chance'])

# Calcular el puntaje total
total_score, bonus = calculate_total_score(st.session_state.scores)

# Mostrar el puntaje total y la bonificación
st.header("Puntaje Total")
st.write(f"Bonificación: {bonus}")
st.write(f"Puntaje Total: {total_score}")
