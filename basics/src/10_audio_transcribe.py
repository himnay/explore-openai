import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

LLM = os.environ.get("OPEN_AI_MODEL")
API_KEY = os.environ.get("OPEN_AI_API_KEY")

client = OpenAI(api_key=API_KEY)

# Call the openai chat.completions endpoint
def ask_openai(
) :  
    print(f"LLM : {LLM}")
    transcription = ""

    return transcription


if __name__ == "__main__":
    
    # audio_path = "src/resources/RAG.mp3"
        # YT_Link -> https://www.youtube.com/watch?v=T-D1OfcDW1M&t=20s
    # audio_path = "src/resources/Taylor_Swift_Delicate.mp3"
    audio_path = "src/resources/RAG.mp3"
        
    # prompt = "This audio explains the concepts about RAG"
