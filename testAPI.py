from dotenv import load_dotenv
import os
load_dotenv()

print("GROQ API Key:", os.getenv("GROQ_API_KEY"))
