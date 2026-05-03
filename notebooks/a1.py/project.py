from langchain_google_genai import ChatGoogleGenerativeAI
import os

# API key
os.environ["GOOGLE_API_KEY"] = "gen-lang-client-0588294063"

# Correct model name
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    temperature=0.5
)

question = "What are the three main components of a well-structured prompt?"

print("Question:", question)

response = llm.invoke(question)

print("Answer:", response.content)