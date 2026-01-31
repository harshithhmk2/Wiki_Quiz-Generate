import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0.3
)

PROMPT = """
You are an educational quiz generator.

From the following Wikipedia content, generate STRICTLY VALID JSON with:
- summary (2–3 lines)
- key_entities:
  - people
  - organizations
  - locations
- quiz (5–10 items), each with:
  question
  options (array of 4)
  answer
  difficulty (easy | medium | hard)
  explanation
- related_topics (array)

Return ONLY JSON. No markdown. No extra text.

Wikipedia Content:
{content}
"""

def generate_quiz(content: str, retries: int = 2):
    prompt = PromptTemplate(
        input_variables=["content"],
        template=PROMPT
    )

    for _ in range(retries):
        response = llm.invoke(prompt.format(content=content))
        try:
            return json.loads(response.content)
        except json.JSONDecodeError:
            continue

    raise ValueError("LLM failed to return valid JSON")
