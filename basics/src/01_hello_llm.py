import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

LLM = os.environ.get("OPEN_AI_MODEL")
API_KEY = os.environ.get("OPEN_AI_API_KEY")

client = OpenAI(api_key=API_KEY)

response = client.chat.completions.create(
    model=LLM,
    messages=[
        {"role": "user", "content": "what teams are playing in this image?"},
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3b/LeBron_James_Layup_%28Cleveland_vs_Brooklyn_2018%29.jpg"}
                }
            ]
        }
    ]
)

print(f"response type : {type(response)}")

response_dict = response.to_dict()
print(json.dumps(response_dict, indent=4))

print(f"response_content : {response.choices[0].message.content}")
