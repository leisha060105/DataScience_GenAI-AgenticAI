import streamlit as st
from ollama import Client

client = Client(host="http://localhost:11434")

st.title("Ollama Chat")

prompt = st.text_area("Enter your prompt")

if st.button("Generate Response"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating..."):
            response = client.chat(
                model="deepseek-r1:1.5b",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            st.success("Done!")
            st.write(response.message.content)