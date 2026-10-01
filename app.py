import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(
    page_title = "AI Interview Coach",
    page_icon = "🧠"
)

st.title("🧠 AI Interview Coach")
st.caption("Practice technical interviews with Langchain + Groq")

model = ChatGroq(
    model = "openai/gpt-oss-20b",
    temperature = 0.3
)

role = st.selectbox(
    "Select your role",
    [
        "Java Backend Developer",
        "Python Developer",
        "Full Stack Developer",
        "Software Engineer"
    ]
)

topic = st.selectbox(
    "Select the topic",
    [
        "Java",
        "Python",
        "FastAPI",
        "Langchain",
        "Spring Boot",
        "DSA",
        "System Design",
        "SQL",
        "Microservices",
        "Others"
    ]
)


experience = st.selectbox(
    "Experience level",
    [
        "Fresher",
        "1-2 years",
        "2-4 years"
    ]
)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an expert technical interviewer.

        Conduct a realistic technical interview.

        The candidate is applying for:
        Role: {role}
        Topic: {topic}
        Experience: {experience}

        Evaluate the candidate's answer fairly.

        Your response must contain:

        1. Score out of 10
        2. What was correct
        3. What was missing or incorrect
        4. An improved answer
        5. One follow-up interview question
        """
    ),
    (
        "human",
        "{question}"
    )
])

chain = prompt | model


st.subheader("🎯 Your Interview Question")

question = st.text_area(
    "Enter the interview question",
    placeholder = "Example: What is dependency injection in Spring Boot?"
)

answer = st.text_area(
    "Your answer",
    placeholder = "Type your interview answer here..."
)


if st.button("Evaluate answer 🚀"):
    if not question or not answer:
        st.warning("Please enter both the question and your answer.")
    else:
        with st.spinner("AI interviewer is evaluating your answer..."):
            
            response = chain.invoke(
                {
                    "role" : role,
                    "topic" : topic,
                    "experience" : experience,
                    "question" :  question + "\n\nCandidate Answer:\n" + answer
                }
            )

        st.subheader("🤖 AI Evaluation")
        st.markdown(response.content)   



