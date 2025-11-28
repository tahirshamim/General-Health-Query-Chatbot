import streamlit as st
from google import genai

# Google Gemini Client
client = genai.Client(api_key="AIzaSyBrsUDZOXeUpQax0rIRLcnEs1CZRy9i9vw")

# System Prompt
SYSTEM_PROMPT = """
You are a friendly, helpful medical assistant.
You can give simple, general health information.

SAFETY RULES — YOU MUST NOT:
- Give diagnoses.
- Give medication doses.
- Tell users what treatment they should follow.
- Give emergency medical instructions.
- Give instructions for children, infants, pregnant women.
- Encourage self-treatment.

If the user asks for medical or dosage advice, respond with:
"I cannot give personal medical advice, but I can share general health information."

Always encourage consulting a licensed doctor.
"""

# Safety Keywords
UNSAFE_KEYWORDS = [
    "dose", "mg", "how much", "prescribe", "medicine for me",
    "my symptoms", "overdose", "emergency", "my child", "infant",
    "is it safe if I take", "treatment", "what should i take"
]


def is_unsafe(question: str) -> bool:
    q = question.lower()
    return any(word in q for word in UNSAFE_KEYWORDS)


def ask_health_bot(question):
    # 1. Safety filter
    if is_unsafe(question):
        return (
            "I can't give specific medical or dosage advice. "
            "Please consult a healthcare professional. "
            "But I can share general health information if you'd like!"
        )

    # 2. Call Gemini API
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=SYSTEM_PROMPT + "\nUser: " + question
    )

    return response.text


# Streamlit UI
st.set_page_config(page_title="Medical Assistant Bot", page_icon="💊", layout="wide")

st.title("💊 Medical Assistant Chatbot (Safe Mode)")
st.write("Ask general health-related questions. Unsafe medical questions are filtered.")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Chat input
user_input = st.chat_input("Ask a health question...")

if user_input:
    # Get bot answer
    bot_response = ask_health_bot(user_input)

    # Save to history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))


# Display chat history
for role, message in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")

