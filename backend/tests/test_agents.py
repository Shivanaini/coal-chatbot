from agents.router import RouterAgent


def test_coal_agent():
    router = RouterAgent()
    response = router.route("What are coal reserves?")
    assert "coal" in response.lower() or "reserves" in response.lower()


def test_retriever_agent():
    router = RouterAgent()
    response = router.route("Search PDF document")
    assert "retriever" in response.lower()


def test_summarizer_agent():
    router = RouterAgent()
    response = router.route("Summarize this report")
    assert "summary" in response.lower()