class IncidenceResponseAgent:
    def __init__(self, llm):
        self.llm = llm

    def process(self, query: str) -> str:
        """Develops an incident response plan based on the given query."""
        prompt = f"""As an Incident Response expert, analyze the following query and provide a comprehensive incident response plan:

Query: {query}

Your incident response plan should include:
1. Initial assessment of the incident
2. Containment strategies
3. Eradication steps
4. Recovery procedures
5. Lessons learned and recommendations for future prevention

Provide a concise yet detailed incident response plan addressing the query.
"""
        return self.llm.generate_response(prompt)