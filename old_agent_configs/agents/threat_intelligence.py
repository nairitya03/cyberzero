class ThreatIntelligenceAgent:
    def __init__(self, llm, web_search_tool):
        self.llm = llm
        self.web_search_tool = web_search_tool

    def process(self, query: str) -> str:
        """Gathers and analyzes threat intelligence based on the given query."""
        prompt = f"""As a Threat Intelligence expert, analyze the following query and provide a comprehensive threat intelligence report:

Query: {query}

Your report should include:
1. An overview of the threat landscape related to the query
2. Identification of potential threat actors or groups
3. Analysis of tactics, techniques, and procedures (TTPs)
4. Relevant indicators of compromise (IoCs)
5. Recommended mitigation strategies

If you need to search for additional information, use the web_search tool.

Provide a concise yet informative threat intelligence report addressing the query.
"""
        response = self.llm.generate_response(prompt)
        
        # Check if web search is needed
        if "web_search" in response.lower():
            search_results = self.web_search_tool.search(query)
            prompt += f"\n\nAdditional information from web search:\n{search_results}\n\nPlease update your report based on this new information."
            response = self.llm.generate_response(prompt)
        
        return response