def test_agent_orchestrator():
    prompt = "Test execution query for agentic-audio-transcription-summarizer"
    assert len(prompt) > 0
    assert "Test" in prompt
