import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
LLM = os.environ.get("OPEN_AI_MODEL")


# Call the openai chat.completions endpoint
def ask_openai(
    user_question: str,
    temperature: float = 1.0,
    top_p: float = 1.0,
    max_tokens: int = 256,
):
    response = client.chat.completions.create(
        model=LLM,
        messages=[
            {"role": "user", "content": user_question},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        stream=True,
    )

    return response


def response_generator(user_question):
    for chunk in ask_openai(user_question):
        if chunk.choices and chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content  # Stream response incrementally


# st.set_page_config(page_title="Chat Application")
st.header("Chat :blue[Application]")

st.chat_message("ai").write("Hello, how can I help you ?")
prompt = st.chat_input("Add your prompt...")
# st.chat_message("user").write("How are you ?")
if prompt:
    st.chat_message("human").write(prompt)

    # non -streaming
    # response = ask_openai(prompt)
    # llm_output = response.choices[0].message.content
    # st.chat_message("ai").write(llm_output)

    # Streaming

    # st.write_stream(
    #         chunk.choices[0].delta.content
    #         for chunk in ask_openai(prompt)
    #         if chunk.choices and chunk.choices[0].delta.content
    #     )
    with st.chat_message("ai"):
        st.write_stream(response_generator(prompt))

    # st.write_stream(response_generator(prompt))
