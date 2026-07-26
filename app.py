import streamlit as st
from pipeline import run_research_pipiline

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Agentic Scholar",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Dark gradient background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        min-height: 100vh;
    }

    /* Hero section */
    .hero-container {
        text-align: center;
        padding: 3rem 1rem 2rem 1rem;
    }

    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #a78bfa, #60a5fa, #34d399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }

    .hero-subtitle {
        font-size: 1.1rem;
        color: #9ca3af;
        margin-bottom: 2rem;
        font-weight: 300;
    }

    /* Pill badges for agents */
    .agent-pills {
        display: flex;
        justify-content: center;
        gap: 0.75rem;
        flex-wrap: wrap;
        margin-bottom: 2.5rem;
    }

    .pill {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 999px;
        padding: 0.35rem 1rem;
        font-size: 0.8rem;
        color: #d1d5db;
        backdrop-filter: blur(8px);
    }

    /* Glass card */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1.5rem;
        backdrop-filter: blur(10px);
        margin-bottom: 1.5rem;
    }

    .card-title {
        font-size: 0.9rem;
        font-weight: 600;
        color: #a78bfa;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }

    .card-content {
        color: #e5e7eb;
        font-size: 0.95rem;
        line-height: 1.7;
        white-space: pre-wrap;
    }

    /* Score badge */
    .score-badge {
        display: inline-block;
        background: linear-gradient(135deg, #a78bfa, #60a5fa);
        color: white;
        font-weight: 700;
        font-size: 1.4rem;
        padding: 0.5rem 1.5rem;
        border-radius: 999px;
        margin-bottom: 1rem;
    }

    /* Step progress */
    .step-indicator {
        background: rgba(167, 139, 250, 0.12);
        border: 1px solid rgba(167, 139, 250, 0.3);
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        color: #a78bfa;
        font-size: 0.9rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }

    /* Input override */
    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.07) !important;
        border: 1px solid rgba(167,139,250,0.4) !important;
        border-radius: 12px !important;
        color: white !important;
        font-size: 1rem !important;
        padding: 0.75rem 1rem !important;
    }

    /* Button override */
    .stButton > button {
        background: linear-gradient(135deg, #7c3aed, #2563eb) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(124, 58, 237, 0.4) !important;
    }

    /* Divider */
    .section-divider {
        border: none;
        border-top: 1px solid rgba(255,255,255,0.08);
        margin: 2rem 0;
    }

    /* Hide streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ─── Hero Section ────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-container">
    <div class="hero-title">🎓 Agentic Scholar</div>
    <div class="hero-subtitle">Multi-Agent AI Research System powered by LangChain & Mistral</div>
    <div class="agent-pills">
        <span class="pill">🔍 Search Agent</span>
        <span class="pill">📖 Reader Agent</span>
        <span class="pill">✍️ Writer Agent</span>
        <span class="pill">🧐 Critic Agent</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── Input ───────────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    topic = st.text_input(
        label="Research Topic",
        placeholder="e.g. Impact of AI in Healthcare, Quantum Computing trends...",
        label_visibility="collapsed",
    )
    run_btn = st.button("🚀 Run Research Pipeline", use_container_width=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# ─── Pipeline Execution ──────────────────────────────────────────────────────
if run_btn:
    if not topic.strip():
        st.warning("⚠️ Please enter a research topic before running.")
    else:
        st.markdown("""
        <div class="glass-card">
            <div class="card-title">⚙️ Pipeline Status</div>
        </div>
        """, unsafe_allow_html=True)

        status_area = st.empty()

        # Step indicators
        steps_placeholder = st.empty()

        with st.spinner(""):
            def update_progress(msg):
                steps_placeholder.markdown(f'<div class="step-indicator">{msg}</div>', unsafe_allow_html=True)
            
            try:
                result = run_research_pipiline(topic, progress_callback=update_progress)
            except Exception as e:
                st.error(f"❌ An error occurred during the pipeline: {str(e)}")
                st.stop()

        steps_placeholder.markdown('<div class="step-indicator">✅ All 4 agents completed successfully!</div>', unsafe_allow_html=True)

        st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

        # ─── Results Layout ───────────────────────────────────────────────────
        st.markdown("### 📊 Research Results")
        st.markdown("")

        tab1, tab2, tab3, tab4 = st.tabs(["🔍 Search Results", "📖 Scraped Content", "✍️ Research Report", "🧐 Critic Review"])

        with tab1:
            st.markdown(f"""
            <div class="glass-card">
                <div class="card-title">🔍 Search Agent Results</div>
                <div class="card-content">{result.get('search_results', 'No results found.')}</div>
            </div>
            """, unsafe_allow_html=True)

        with tab2:
            st.markdown(f"""
            <div class="glass-card">
                <div class="card-title">📖 Reader Agent — Scraped Content</div>
                <div class="card-content">{result.get('scraped_content', 'No content scraped.')}</div>
            </div>
            """, unsafe_allow_html=True)

        with tab3:
            report = result.get("report", "No report generated.")
            st.markdown(f"""
            <div class="glass-card">
                <div class="card-title">✍️ Writer Agent — Research Report</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(report)

            # Download button
            st.download_button(
                label="⬇️ Download Report as Markdown",
                data=report,
                file_name=f"{topic.replace(' ', '_')}_report.md",
                mime="text/markdown",
            )

        with tab4:
            critique = result.get("critique", "No critique generated.")

            # Try to extract score for the badge
            score_line = ""
            for line in critique.split("\n"):
                if "score" in line.lower() and "/" in line:
                    score_line = line.strip()
                    break

            if score_line:
                st.markdown(f'<div class="score-badge">{score_line}</div>', unsafe_allow_html=True)

            st.markdown(f"""
            <div class="glass-card">
                <div class="card-title">🧐 Critic Agent — Peer Review</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(critique)

# ─── Empty state hint ────────────────────────────────────────────────────────
else:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="glass-card">
            <div class="card-title">🔍 Search Agent</div>
            <div class="card-content">Searches the web using Tavily API, returning the top 3 most relevant articles with URLs and snippets.</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="glass-card">
            <div class="card-title">📖 Reader Agent</div>
            <div class="card-content">Picks the most relevant URL, scrapes it using BeautifulSoup, and extracts detailed key findings and summaries.</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="glass-card">
            <div class="card-title">✍️ Writer + 🧐 Critic</div>
            <div class="card-content">Writer synthesizes a structured academic report. The Critic evaluates it with a score, strengths, weaknesses, and actionable improvements.</div>
        </div>
        """, unsafe_allow_html=True)
