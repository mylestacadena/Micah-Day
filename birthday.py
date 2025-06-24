import streamlit as st

# Page config
st.set_page_config(page_title="Birthday Surprise", layout="centered")

# Centering with CSS
st.markdown("""
    <style>
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .gift-button {
            background-color: #ff4b4b;
            color: white;
            padding: 20px 40px;
            font-size: 24px;
            border-radius: 12px;
            border: none;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="center">', unsafe_allow_html=True)

# Display gift box
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if not st.session_state.clicked:
    if st.button("🎁 Click Me!", key="gift"):
        st.session_state.clicked = True
        st.balloons()
        st.snow()

# After clicking
if st.session_state.clicked:
    st.markdown("""
        <h1 style='text-align: center; color: #ff4b4b;'> Happy 21st bornday!</h1>
        <p style='text-align: center; font-size: 20px;'>Wishing you a day filled with joy and surprises!</p>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
