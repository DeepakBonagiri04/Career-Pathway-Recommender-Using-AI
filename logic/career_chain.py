import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# Configure LangChain to use OpenRouter
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

# --- Prompt Templates ---

# Full recommendation prompt
recommendation_prompt = ChatPromptTemplate.from_template("""
You are a career counselor. Based on the student's interests, hobbies, and academic strengths, suggest 3 ideal career paths.
Include a short explanation (2-3 sentences) for each.

Subjects: {subjects}
Hobbies: {hobbies}
Academic Strengths: {scores}

Return the results as:
1. Career: ...
   Explanation: ...
2. Career: ...
   Explanation: ...
3. Career: ...
   Explanation: ...
""")

# Clarification prompt
clarify_prompt = ChatPromptTemplate.from_template("""
The student's input is not detailed enough. Politely ask the following:
1. Favorite subject(s) in school or college
2. Hobbies or things they enjoy outside academics
3. Academic strengths or scores

Student Input:
{raw_input}

Your Task:
Generate 3 clarifying questions.
""")

# Output parser
parser = StrOutputParser()

# Runnable chains
recommend_chain: Runnable = recommendation_prompt | llm | parser
clarify_chain: Runnable = clarify_prompt | llm | parser

# Main callable function
def generate_recommendation(subjects, hobbies, scores):
    if not subjects or not hobbies or not scores:
        raw_input = f"{subjects}, {hobbies}, {scores}"
        return clarify_chain.invoke({"raw_input": raw_input})
    
    return recommend_chain.invoke({
        "subjects": subjects,
        "hobbies": hobbies,
        "scores": scores
    })
