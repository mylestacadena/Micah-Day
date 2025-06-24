import streamlit as st

# Page config
st.set_page_config(page_title="Birthday Surprise", layout="centered")

# Session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

# CSS styling
st.markdown("""
    <style>
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        h1, p {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Content container
st.markdown('<div class="center">', unsafe_allow_html=True)

if not st.session_state.clicked:
    # Center the button using columns
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎁 Click Me!", key="gift"):
            st.session_state.clicked = True
            st.balloons()
            st.snow()

# After clicking
if st.session_state.clicked:
    st.markdown("""
        <h1 style='color: #ff4b4b;'>🎉 Happy 21st Bornday! 🎂</h1>
        <p style='font-size: 20px;'>Wishing you a day filled with joy and surprises!</p>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
