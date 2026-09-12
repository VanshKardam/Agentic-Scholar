# 🎓 Agentic Scholar

**Agentic Scholar** is a fully automated, multi-agent AI research system built with **LangChain**, **Gemini**, **Groq**, and **Mistral AI**. It leverages a coordinated team of specialized AI agents to scour the web, scrape articles, synthesize findings into a comprehensive academic report, and critically review its own work.

The system features a beautiful, glassmorphic **Streamlit** user interface.

## 🚀 Features

The pipeline operates in four distinct steps powered by four specialized agents:

1. 🔍 **Search Agent**: Uses the **Tavily API** to hunt for the most relevant and up-to-date sources based on your research topic.
2. 📖 **Reader Agent**: Autonomously selects the best URLs and uses **BeautifulSoup** to scrape the full-text content of the articles, filtering out noise.
3. ✍️ **Writer Agent**: Synthesizes the scraped knowledge into a structured, comprehensive academic report complete with an Introduction, Key Findings, Conclusion, and Cited Sources.
4. 🧐 **Critic Agent**: Acts as a harsh peer-reviewer. It evaluates the final report, scores it out of 10, and highlights strengths, weaknesses, and actionable improvements.

## 🛠️ Tech Stack

- **Framework**: LangChain (Agents & LCEL)
- **LLM**: Gemini 1.5 Flash (Primary), Groq Llama 3 (Fallback), Mistral (Fallback)
- **Tools**: Tavily Search API, BeautifulSoup4
- **UI**: Streamlit
- **Language**: Python

## ⚙️ Installation

1. Navigate to the project directory:
   ```bash
   cd "Agentic Scholar"
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables. Ensure your `.env` file contains your API keys:
   ```env
   MISTRAL_API_KEY=your_mistral_key_here
   TAVILY_API_KEY=your_tavily_key_here
   GOOGLE_API_KEY=your_google_key_here
   GROQ_API_KEY=your_groq_key_here
   ```

## 🎮 How to Run

To make launching the app as easy as possible, use the provided helper scripts which automatically activate the virtual environment and launch the Streamlit app.

**If using PowerShell:**
```powershell
.\run.ps1
```

**If using Command Prompt:**
```cmd
run.bat
```

Once running, open your browser to `http://localhost:8501`. Enter any research topic and watch the agents go to work!
