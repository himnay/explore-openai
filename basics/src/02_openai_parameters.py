import os
from urllib import response

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion

load_dotenv()

LLM = os.environ.get("OPEN_AI_MODEL")
API_KEY = os.environ.get("OPEN_AI_API_KEY")

client = OpenAI(api_key=API_KEY)


# Call the openai chat.completions endpoint
def ask_openai(
        user_question: str,
) -> ChatCompletion:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": user_question},
        ],
    )

    print(f"response  type : {type(response)}")
    return response


if __name__ == "__main__":
    # temperature
    # 0.2 -> Deterministic
    # 1 and above  -> non deterministic
    user_question = """
        Can you complete the sentence ?

        My dog is playful and love to
        """


    # top_p
    # Start with 1, -> run around in the park, chasing after balls and playing with other dogs.
    #  0.5-> My dog is playful and loves to chase after balls in the park.
    #  0.2-> My dog is playful and loves to chase after balls in the park.
    def ask_openai(prompt: str, top_p: float = 1.0):
        response = openai.ChatCompletion.create(
            model=LLM,
            messages=[{"role": "user", "content": prompt}],
            top_p=top_p
        )
        return response


    print(f"response type : {type(response)}")
