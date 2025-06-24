import streamlit as st

# Page config
st.set_page_config(page_title="Birthday Surprise", layout="centered")

# Session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

# CSS styling for layout and button
st.markdown("""
    <style>
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80vh;
            flex-direction: column;
        }
        .gift-button {
            background-color: #ff4b4b;
            color: white;
            padding: 30px 60px;
            font-size: 32px;
            border-radius: 20px;
            border: none;
            width: 50%;
            max-width: 400px;
            min-width: 250px;
            cursor: pointer;
        }
        .gift-button:hover {
            background-color: #e84343;
        }
    </style>
""", unsafe_allow_html=True)

# Center container
st.markdown('<div class="center">', unsafe_allow_html=True)

# Button behavior
if not st.session_state.clicked:
    # Use custom HTML and Streamlit form to trigger action
    with st.form("gift_form"):
        submitted = st.form_submit_button("🎁 Click Me!", help="Click to reveal your gift")
        if submitted:
            st.session_state.clicked = True
            st.balloons()
            st.snow()

    # Apply the CSS class to the button using JS trick
    st.markdown("""
        <script>
        const btn = window.parent.document.querySelectorAll('button[kind=primary]');
        if (btn.length) btn[0].className += ' gift-button';
        </script>
    """, unsafe_allow_html=True)

# After clicking
if st.session_state.clicked:
    st.markdown("""
        <h1 style='color: #ff4b4b;'>🎉 Happy 21st Bornday! 🎂</h1>
        <p style='font-size: 20px;'>Wishing you a day filled with joy and surprises!</p>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
