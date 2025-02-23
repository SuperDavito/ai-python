import streamlit as st
from utils.openai_client import OpenAIClient

def main():
    st.title("Chat with OpenAI")
    
    openai_client = OpenAIClient()
    
    user_input = st.text_input("You:", "")
    
    if st.button("Send"):
        if user_input:
            response = openai_client.get_response(user_input)
            st.text_area("OpenAI:", response, height=300)
        else:
            st.warning("Please enter a message.")

if __name__ == "__main__":
    main()