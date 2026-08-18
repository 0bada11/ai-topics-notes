from dotenv import load_dotenv
from google import genai
import os
import time
from chromadb.utils import embedding_functions
import chromadb


# loading .env file
load_dotenv()

# set the GOOGLE_API_KEY
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY is not set in the environment")

# set the LLM Model
client = genai.Client(api_key=api_key)

models = client.models.list(config={"page_size": 50, "query_base": True})
gemini_models = [model.name for model in models if "gemini" in model.name]
if not gemini_models:
    raise RuntimeError("No supported Gemini models were found for generate_content")

preferred_models = [
    "models/gemini-2.5-flash",
    "models/gemini-2.1",
    "models/gemini-1.5",
]

candidate_models = [m for m in preferred_models if m in gemini_models] + [m for m in gemini_models if m not in preferred_models]

response = None
for model_name in candidate_models:
    for attempt in range(3):
        try:
            print(f"Trying model: {model_name} (attempt {attempt + 1})")
            response = client.models.generate_content(
                model=model_name,
                contents="Hello"
            )
            print("Using model:", model_name)
            break
        except genai.errors.ServerError as err:
            print(f"Model {model_name} unavailable: {err}. retrying...")
            time.sleep(2)
            continue
    if response is not None:
        break

if response is None:
    raise RuntimeError("All Gemini models were unavailable. Please try again later.")

print(response.text)

chroma_client = chromadb.PersistentClient(path="chroma_persistent_storage")
collection_name = "document_qa_collection"