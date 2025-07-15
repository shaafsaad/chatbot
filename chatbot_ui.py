import streamlit as st
import ollama

st.set_page_config(page_title="Ollama Chatbot", page_icon="🤖")

st.title("🤖 Ollama Chatbot")
st.write("Chat with your local LLM (Ollama).")

# Always initialize history as a list
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", key="user_input")

if st.button("Send") and user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    try:
        response = ollama.chat(model="llama3:8b", messages=st.session_state.history)
        reply = response.get("message", {}).get("content", "[No response]")
    except Exception as e:
        reply = f"[Error: {e}]"
    st.session_state.history.append({"role": "assistant", "content": reply})
    st.rerun()

# Display chat history
for msg in st.session_state.history:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")

# Option to clear chat
if st.button("Clear Chat"):
    st.session_state.history.clear()
    st.rerun()