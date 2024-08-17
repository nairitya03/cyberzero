class ResponderAgent:
    def __init__(self, llm: object) -> None:
        """
        Initialize the ResponderAgent with a language model instance.
        
        Args:
        llm (object): An instance of a language model class.
        """
        self.llm = llm
        self.prompt = """As a Responder Agent, your task is to create a well-structured and coherent final response based on the following summaries from different agents: 
        {summary}
        
        #########
        Please format the response in the following way:
        1. Start with a brief overview of the situation.
        2. Present the key findings or actions from each agent.
        3. Provide a conclusion or recommended next steps.
        4. If there are any conflicting pieces of information, highlight them and provide your assessment.

        Ensure the response is clear, concise, and actionable for the SOC team."""

    def format_response(self, responses: dict) -> str:
        """
        Generate a formatted response using the LLM.
        
        Args:
        responses (dict): A dictionary of agent responses, where each key is an agent name and each value is a string response.
        
        Returns:
        str: The formatted response.
        """
        
        summary = self.prepare_summary(responses)
        try:
            return self.llm.generate_response(self.prompt.format(summary=summary))
        except Exception as e:
            # Handle errors and exceptions
            print(f"Error generating response: {e}")
            return ""

    def prepare_summary(self, responses: dict) -> str:
        """
        Prepare a summary of all responses.
        
        Args:
        responses (dict): A dictionary of agent responses, where each key is an agent name and each value is a string response.
        
        Returns:
        str: The summary string.
        """
        summary = []
        for agent, response in responses.items():
            summary.append(f"{agent.capitalize()} Agent's findings:\n{response}\n\n")
        return "".join(summary)