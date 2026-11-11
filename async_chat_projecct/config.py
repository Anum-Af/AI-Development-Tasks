import os

from openai import AsyncOpenAI


api_key=os.getenv("GEMINI_API_KEY"),
base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
MODEL_ID = "gemini-3.5-flash-lite"


# client = AsyncOpenAI(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

