import streamlit as st

# Page config
st.set_page_config(page_title="Birthday Surprise", layout="centered")

# Heart animation using HTML + CSS
def falling_hearts():
    st.markdown("""
    <style>
    .hearts {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      overflow: hidden;
      z-index: 999;
      pointer-events: none;
    }

    .heart {
      position: absolute;
      width: 30px;
      height: 30px;
      background-color: pink;
      transform: rotate(45deg);
      animation: float 6s infinite ease-in;
    }

    .heart::before,
    .heart::after {
      content: "";
      position: absolute;
      width: 30px;
      height: 30px;
      background-color: pink;
      border-radius: 50%;
    }

    .heart::before {
      top: -15px;
      left: 0;
    }

    .heart::after {
      left: -15px;
      top: 0;
    }

    @keyframes float {
      0% {
        transform: translateY(0) rotate(45deg);
        opacity: 1;
      }
      100% {
        transform: translateY(800px) rotate(45deg);
        opacity: 0;
      }
    }
    </style>

    <div class="hearts">
      {% for i in range(30) %}
      <div class="heart" style="
        left: {{ (i * 3) % 100 }}%;
        animation-delay: {{ (i * 0.2) % 5 }}s;
      "></div>
      {% endfor %}
    </div>
    """, unsafe_allow_html=True)

# HTML templating fallback (since Streamlit doesn't support Jinja directly)
def generate_hearts_html(n=30):
    hearts_html = '<div class="hearts">'
    for i in range(n):
        left = (i * 3) % 100
        delay = (i * 0.2) % 5
        hearts_html += f'''
            <div class="heart" style="
                left: {left}%;
                animation-delay: {delay}s;
            "></div>
        '''
    hearts_html += '</div>'
    return hearts_html

# Inject CSS
st.markdown("""
    <style>
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="center">', unsafe_allow_html=True)

# State for button click
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

# Button
if not st.session_state.clicked:
    if st.button("🎁 Click Me!", key="gift"):
        st.session_state.clicked = True
        st.balloons()

# After click
if st.session_state.clicked:
    # Show hearts
    st.components.v1.html(f"""
        <style>
        .hearts {{
          position: fixed;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          overflow: hidden;
          z-index: 999;
          pointer-events: none;
        }}
        .heart {{
          position: absolute;
          width: 30px;
          height: 30px;
          background-color: pink;
          transform: rotate(45deg);
          animation: float 6s infinite ease-in;
        }}
        .heart::before,
        .heart::after {{
          content: "";
          position: absolute;
          width: 30px;
          height: 30px;
          background-color: pink;
          border-radius: 50%;
        }}
        .heart::before {{
          top: -15px;
          left: 0;
        }}
        .heart::after {{
          left: -15px;
          top: 0;
        }}
        @keyframes float {{
          0% {{
            transform: translateY(0) rotate(45deg);
            opacity: 1;
          }}
          100% {{
            transform: translateY(800px) rotate(45deg);
            opacity: 0;
          }}
        }}
        </style>
        {generate_hearts_html()}
    """, height=0)

    # Message
    st.markdown("""
        <h1 style='text-align: center; color: #ff4b4b;'>💖 Happy Birthday! 🎂</h1>
        <p style='text-align: center; font-size: 20px;'>Wishing you a day full of love and joy!</p>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
