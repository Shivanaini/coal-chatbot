from agents.coal_agent import CoalAgent
from agents.retriever import RetrieverAgent
from agents.summarizer import SummarizerAgent


class RouterAgent:
    def __init__(self):
        self.coal_agent = CoalAgent()
        self.retriever = RetrieverAgent()
        self.summarizer = SummarizerAgent()

    def route(self, query):
        query_lower = query.lower()

        if any(word in query_lower for word in ["coal", "reserve", "sccl", "district"]):
            return self.coal_agent.process(query)

        elif any(word in query_lower for word in ["document", "search", "pdf"]):
            return self.retriever.process(query)

        elif any(word in query_lower for word in ["summary", "summarize"]):
            return self.summarizer.process(query)

        return "Router Agent: Sorry, I couldn't determine which agent to use."