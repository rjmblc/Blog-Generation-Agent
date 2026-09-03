import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self):
        load_dotenv()


    def get_llm(self):
        try:

            self.GROQ_API_KEY=os.getenv("GROQ_API_KEY")
            llm=ChatGroq(
                api_key=self.GROQ_API_KEY,
                model="openai/gpt-oss-20b"
            )
            return llm

        except Exception as e:
            raise ValueError(f"Error occured with exception {e}")