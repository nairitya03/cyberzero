load the prompts form `prompts/agents/agent_name.md` files for each agent
I want LLM to decide what agent it needs to call or what tools it needs, based on the agent's system prompt. a formatted message will be passed which contains user query, list of agents, list of tools, with prompts of tool usage.

structure it in into different classes:
- `main.py` it the main run class
- all the model loading will go in `models.py`
- different agents will be in `agents/agent_name.py`
- all the tools will in `tools/tool_name.py`
- all the agent prompts and tool prompts will be under `prompts/agents/agent_name.md` and `prompts/tools/tool_name.md`

-------------------------------
here is the list of agents:
- `SOC Manager agent`: he is the manager and overlooks everything. he takes the query from user as input and generate response for it. if he thinks that the task is complex and need help of other agents in the team. he'll divide the task into subtasks and invoke other agents only when needed. all agents report back to `SOC manager agent`. he has access to `sub_agent tool`.

- `Penetration Testing agent`: he is technical agent. SOC manager invokes him when he thinks user wants team to generate linux bash or shell commands for tools or python code. he has access to `web_search tool` to search documents only when he doesn't know the usage for Linux packages, tools or python libraries. he then generate concise response containing working command or python3 code.

- `threat_intelligence agent`: he is an analytical agent. SOC manager invokes him when he thinks user wants team to gather threat Intel about a topic or cyber attack. he has access to `web_search tool` to search for latest news blogs or articles about the topic to gather as much intel as possible. and generate a concise response report on it.

- `incidence_response agent`: he is a response agent. SOC manager invokes him when he think user wants team to create the framework for mapping attacks to responses. he tries to classify information according to `MITRE ATTACK framework`

- `Responder Agent`: he is a editor agent. SOC manager collects responses from all the agents and invokes responder agent to final 
format response. he then returns the response to user.

--------------------------------------
here is the list of tools:
- `sub_agent tool`: it is the tool used by SOC manager to initialize and invoke sub-agents on demand.
- `web_search tool`: it is a web_search tool. this tool is accessible by all the agents, when needed.
- `file_create tool`: it a file create tool. agents can use this tool to create files with desired extensions (like .md/.py/.js/.bat/.sh/.txt) in the "data" directory.

----------------------------------------


This is a complex task lets break it down into steps and target one step at a time. 
- start with llm_model loading from hugging face. 
