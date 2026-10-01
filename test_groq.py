from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.3
)

response = model.invoke("Explain dependency injection in Spring Boot in simple words.")

print(response.content)