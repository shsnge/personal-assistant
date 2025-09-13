import streamlit as st
import google.generativeai as genai
import pandas as pd

# --- Configure Gemini API ---
genai.configure(api_key="AIzaSyCM4vIdZylsML_EvYub0ky-ynPuJtYXvUE")  # apni API key yahan lagao

# --- Load Personal Data ---
try:
    personal_df = pd.read_csv("personal_data.csv")
    personal_data = personal_df.to_string(index=False)
except FileNotFoundError:
    personal_data = """
    Name: Zeeshan
    Skills: HTML, CSS, JavaScript, React, Node.js, Express, MongoDB
    Hobbies: Reading, Traveling, Coding
    Favorite Food: Biryani
    Current Focus: Web Development & AI
    """
    st.warning("⚠️ personal_data.csv not found. Using default profile.")

# --- Personal Chatbot Function ---
def personal_chatbot(user_query):
    prompt = f"""
You are Zeeshan, a friendly person who can chat casually and answer questions about yourself.
Always use "I", "my", "me" (never say "you" for yourself).

Your personal details:
{personal_data}

You can handle:
- Greetings & casual chat (Hi, hello, how are you?)
- Feelings & mood (what are you doing? how are you feeling?)
- Hobbies, interests, food, studies, work
- Personal background & skills

User: {user_query}
Zeeshan:
"""
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text

# --- Streamlit UI ---
st.markdown(
    """
    <style>
    .custom-title {
        font-size: 42px; /* default desktop */
        font-weight: bold;
        text-align: center;
    }
    @media (max-width: 1200px) {
        .custom-title {
            font-size: 36px;
        }
    }
    @media (max-width: 768px) {
        .custom-title {
            font-size: 28px;
        }
    }
    @media (max-width: 480px) {
        .custom-title {
            font-size: 22px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<h1 class="custom-title">🤖 Zeeshan\'s Personal Chatbot</h1>', unsafe_allow_html=True)

st.write("Ask me anything about myself!")

user_query = st.text_input("You: ")

if st.button("Ask"):
    if user_query.strip():
        with st.spinner("Thinking..."):
            answer = personal_chatbot(user_query)
        st.write(f"**Zeeshan:** {answer}")
    else:
        st.warning("Please type a question first!")
