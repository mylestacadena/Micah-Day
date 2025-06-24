import streamlit as st

# Page config
st.set_page_config(page_title="Birthday Surprise", layout="centered")

# Set up session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

# CSS for centering and styling
st.markdown("""
    <style>
        .center-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80vh;
            flex-direction: column;
            text-align: center;
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
        button[kind="secondary"] {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# Centered content container
st.markdown('<div class="center-container">', unsafe_allow_html=True)

if not st.session_state.clicked:
    # Centered gift box button
    if st.button("🎁 Click to Open Your Gift!"):
        st.session_state.clicked = True
        st.balloons()
else:
    # Birthday message only
    st.markdown("""
        <h1 style='color: #ff4b4b;'>🎉 Happy Birthday! 🎂</h1>
        <p style='font-size: 20px;'>Wishing you a day filled with joy and surprises!</p>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
