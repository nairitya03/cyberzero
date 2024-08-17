import json
from typing import List, Dict, Any

class SOCManager:
    """
    A class to manage a Security Operations Center (SOC) team.

    Attributes:
    llm (LLMModel): The language model used to generate responses.
    tools (Dict[str, Any]): A dictionary of tools available to the SOC team.
    conversation_history (List[str]): A list of previous interactions with the user.
    """
    def __init__(self, llm, tools: Dict[str, Any]):
        """
        Initializes the SOCManager instance.

        Args:
        llm (LLMModel): The language model used to generate responses.
        tools (Dict[str, Any]): A dictionary of tools available to the SOC team.
        """
        self.llm = llm
        self.tools = tools
        self.conversation_history = []

    def process_query(self, query: str) -> str:
        """
        Processes a user query and generates a response.

        Args:
        query (str): The user's query.

        Returns:
        str: The final response to the user.
        """
        self.conversation_history.append(f"User: {query}")        
        while True:
            response = self.get_llm_response(query)
            
            if response.get("action") == "Final Response":
                final_response = self.format_final_response(response.get("action_input", "No final response generated."))
                self.conversation_history.append(f"Assistant: {final_response}")
                return final_response
            
            tool_name = response.get("action")
            tool_input = response.get("action_input")
            
            if tool_name in self.tools:
                tool_output = self.tools[tool_name](tool_input)
                self.conversation_history.append(f"Tool ({tool_name}): {tool_output}")
            else:
                tool_output = f"Error: Tool '{tool_name}' not found."
                self.conversation_history.append(f"System: {tool_output}")

    def get_llm_response(self, query: str) -> Dict[str, Any]:
        prompt = self.create_prompt(query)
        llm_output = self.llm.generate_response(prompt)
        return self.parse_llm_output(llm_output)

    def create_prompt(self, query: str) -> str:
        tool_descriptions = "\n".join([f"- {name}: {tool.__doc__}" for name, tool in self.tools.items()])
        
        prompt = f"""You are an AI assistant managing a SOC (Security Operations Center) team. Your task is to process the following query and decide on the next action. You can use the following tools: 
        {tool_descriptions}
        Conversation history:
        {self.format_conversation_history()}

        Current query: {query}

        Respond in the following JSON format:
        {
        "thought": "Your reasoning about what to do next",
        "action": "The name of the tool to use or 'Final Response' if you're ready to respond to the user",
        "action_input": "The input to the tool or the final response to the user"
        }

        Ensure your response only contains a JSON object and CAN be parsed as valid JSON. 
        It should NOT contain any extra text before or after json object."""
        return prompt

    def format_conversation_history(self) -> str:
        if self.conversation_history!= None:
            # Show last interactions
            return "\n".join(self.conversation_history[-1:])  
        else: return ""

    def parse_llm_output(self, llm_output: str) -> Dict[str, Any]:
        try:
            return json.loads(llm_output)
        except json.JSONDecodeError:
            return {
                "thought": "Error parsing LLM output",
                "action": "Final Response",
                "action_input": "I apologize, but I encountered an error while processing your request. Could you please rephrase your query?"
            }
        

    def format_final_response(self, response: str) -> str:
        prompt = f"""As the SOC Team Responder, your task is to format the following response into a clear, professional, and actionable message for the user:

{response}

Please format the response in the following way:
1. Start with a brief overview of the situation or query.
2. Present the key findings, recommendations, or actions.
3. If applicable, provide a conclusion or next steps.
4. Ensure the language is clear, concise, and appropriate for a cybersecurity context.

Formatted response:
"""
        return self.llm.generate_response(prompt)






# Example usage:
# llm = LLMModel()
# tools = {
#     "web_search": web_search_tool.search,
#     "create_file": file_create_tool.create_file,
#     "penetration_testing": penetration_testing_agent.process,
#     "threat_intelligence": threat_intelligence_agent.process,
#     "incidence_response": incidence_response_agent.process
# }
# soc_manager = SOCManager(llm, tools)
# response = soc_manager.process_query("Analyze the recent Log4j vulnerability")