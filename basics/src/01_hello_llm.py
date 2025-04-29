import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
LLM = os.environ.get("OPEN_AI_MODEL")

client.chat.completions.create(
    model=LLM,
    messages=[
        {"role": "user", "content": "what teams are playing in this image?"},
        {
            "role": "user",
            "content": [
                {
                    "type": "input_image",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3b/LeBron_James_Layup_%28Cleveland_vs_Brooklyn_2018%29.jpg"
                }
            ]
        }
    ]
)