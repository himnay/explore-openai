import os

import requests
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.images_response import ImagesResponse

load_dotenv()

LLM = os.environ.get("OPEN_AI_MODEL")
API_KEY = os.environ.get("OPEN_AI_API_KEY")

client = OpenAI(api_key=API_KEY)


# Call the openai chat.completions endpoint
def ask_openai(user_question: str, size="1024x1024") -> ImagesResponse:
    print(f"LLM : {LLM}")

    response = client.images.generate(
        model="dall-e-3",
        prompt=user_question,
        size=size,
        quality="standard",
        n=1,
    )

    print(f"response  type : {type(response)}")
    return response


if __name__ == "__main__":
    # Step 1:
    user_question = "A dog and cat ridding a motorcycle. cat is sitting on the side kart attached to the bycycle"  # ✅ correct prompt
    size = "1024x1024"  # ✅ correct size value

    response: ImagesResponse = ask_openai(user_question, size=size)

    # Pretty print the entire response
    image_url = response.data[0].url
    print("Generated Image URL:", image_url)

    image_data = requests.get(image_url).content
    with open("src/resources/generated_image.png", "wb") as f:
        f.write(image_data)

    print("Image successfully downloaded and saved as 'generated_image.png'")

