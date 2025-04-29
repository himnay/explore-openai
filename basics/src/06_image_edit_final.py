import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.images_response import ImagesResponse  # ✅ correct import

load_dotenv()

LLM = os.environ.get("OPEN_AI_MODEL")
API_KEY = os.environ.get("OPEN_AI_API_KEY")

client = OpenAI(api_key=API_KEY)


def ask_openai(user_question: str, size="1024x1024") -> ImagesResponse:
    print(f"LLM : {LLM}")

    response = client.images.edit(
        model="dall-e-2",
        image=open("../explore-open-ai/generated_image.png", "rb"),
        mask=open("../explore-open-ai/mask.png", "rb"),
        prompt=user_question,
        size=size,
    )

    print(f"response type: {type(response)}")
    return response


if __name__ == "__main__":
    user_question = "Dog and a cat in the forest background."

    response = ask_openai(user_question)

    image_url = response.data[0].url
    print("Generated Image URL:", image_url)

    image_data = requests.get(image_url).content
    file_name = "generated_image_edited.png"
    with open(file_name, "wb") as f:
        f.write(image_data)

    print(f"Image successfully downloaded and saved as {file_name}")
