import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain
from rich import print


def run_research_pipiline(topic: str, progress_callback=None) -> dict:
    state = {}

    # Step 1: search agent working
    if progress_callback: progress_callback("🔍 Step 1 — Search Agent is scouring the web...")
    print("\n---")
    print("Step 1 - Search agent is working ...")
    print("\n---")
    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages" : [("user", f"Search the web for the latest information on: {topic}. You MUST include the exact URLs for all sources in your final response so they can be scraped later.")]
    })
    state["search_results"] = search_result["messages"][-1].content
    print("\n---search result---\n")
    print(state["search_results"])
    print("\n---")

    # Step 2: reader agent working
    if progress_callback: progress_callback("📖 Step 2 — Reader Agent is scraping top resources...")
    print("\n---")
    print("Step 2 - Reader agent is scraping top resources...")
    print("\n---")
    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [
            ("user", f"""Based on the following search results about '{topic}':
            Read and extract detailed summaries from these URLs:
            {state['search_results'][:800]}
            Pick the most relevant URL and scrapte it for detailed information, provide a detailed, clean summary.
            Extract all key points, findings, and important information.
            Provide the name of the source website/publication.
            Keep summary detailed but concise.""")
        ]
    })
    state["scraped_content"] = reader_result["messages"][-1].content
    print("\n---scraped content---\n")
    print(state["scraped_content"])
    print("\n---")

    # Step 3: writing chain
    if progress_callback: progress_callback("✍️ Step 3 — Writer is drafting the research report...")
    print("\n---")
    print("Step 3 - Writer is drafting the report...")
    print("\n---")

    research_combined = (
        f"SEARCH RESULTS : \n {state['search_results']}\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })
    print("\n---Report---\n")
    print(state["report"])
    print("\n---")

    # Step 4: critic chain
    if progress_callback: progress_callback("🧐 Step 4 — Critic is peer-reviewing the report...")
    print("\n---")
    print("Step 4 - Critic is reviewing the report...")
    print("\n---")

    state["critique"] = critic_chain.invoke({
        "topic": topic,
        "research": state["report"]
    })
    print("\n---Critique---\n")
    print(state["critique"])
    print("\n---")

    return state

if __name__ == "__main__":
    topic = input("\nEnter Topic: ")
    final_report = run_research_pipiline(topic)
    