from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
from dotenv import load_dotenv
load_dotenv()

# model setup (Order: Gemini -> Groq -> Mistral)
gemini_llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.1)
groq_llm = ChatGroq(model="llama3-8b-8192", temperature=0.1)
mistral_llm = ChatMistralAI(model="open-mistral-nemo", temperature=0.1)

llm = gemini_llm.with_fallbacks([groq_llm, mistral_llm])
# search agent
def build_search_agent():
    return create_agent(
        model = llm,
        tools = [web_search]
    )

# reader agent
def build_reader_agent():
    return create_agent(
        model = llm,
        tools = [scrape_url]
    )

# writer agent
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Your job is to take a list of extracted articles and produce a coherent, well-structured summary."),
    ("user", """Based on the following research paper summaries, write a concise, well-structured academic summary:{research}
    Main Topic: {topic}
    Structure the report as:
    - Introduction
    - Key Findings (minimum 3 well-explained points)
    - Conclusion
    - Sources (list all URLs found in the research)

    Do not include any conversational filler.
    Use bullet points for key findings and sources.
    Minimum word count: 250 words.
    Be detailed, factual and professional.
        """)
])

writer_chain = writer_prompt | llm | StrOutputParser()

#critic_chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research reviewer. Read the summary provided and critique it strictly for factual accuracy, logical flow, clarity, and missing information. Be honest and specific. Do not hold back."),
    ("user", """Review the research report below and evalutate it strictly:
    Topic: {topic}
    Research Report: {research}
    Respong in this exact format:
    Score: x/10
    
    Strengths:
    - ...
    - ...
    
    Weaknesses:
    - ...
    - ...
    
    Improvements:
    - ...
    - ...
    
    One line verdict:
    ...
        """)
])

critic_chain = critic_prompt | llm | StrOutputParser()