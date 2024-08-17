import threading, time, models, os

from dotenv import load_dotenv
from ansio import application_keypad, mouse_input, raw_input
from ansio.input import InputEvent, get_input_event
from agent import Agent, AgentConfig
from python.helpers.print_style import PrintStyle
from python.helpers.files import read_file
from python.helpers import files
import python.helpers.timed_input as timed_input

input_lock = threading.Lock()

## load env variables...
load_dotenv()

os.chdir(files.get_abs_path("./work_dir")) #change CWD to work_dir
MODEL = os.getenv("model_name8b")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MIXTRAL_API_KEY = os.getenv("MIXTRAL_API_KEY")
OLLAMA_HOST = os.getenv("OLLAMA_HOST")

def initialize():
    
    # main chat model used by agents (smarter, more accurate)
    # chat_llm = models.get_openai_chat(model_name="gpt-4o-mini", temperature=0)
    # chat_llm = models.get_lmstudio_chat(model_name="TheBloke/Mistral-7B-Instruct-v0.2-GGUF", temperature=0)
    # chat_llm = models.get_openrouter(model_name="meta-llama/llama-3-8b-instruct:free")hi
    # chat_llm = models.get_azure_openai_chat(deployment_name="gpt-4o-mini", temperature=0)
    # chat_llm = models.get_anthropic_chat(model_name="claude-3-5-sonnet-20240620", temperature=0)
    # chat_llm = models.get_google_chat(model_name="gemini-1.5-flash", temperature=0)
    # chat_llm = models.get_groq_chat(model_name="llama-3.1-70b-versatile", temperature=0)
    
    # utility model used for helper functions (cheaper, faster)
    # utility_llm = chat_llm # change if you want to use a different utility model

    # embedding model used for memory
    # embedding_llm = models.get_openai_embedding(model_name="text-embedding-3-small")
    # embedding_llm = models.get_ollama_embedding(model_name="nomic-embed-text")
    # embedding_llm = models.get_huggingface_embedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
    # llm = models.get_ollama_chat(model_name=MODEL, base_url=OLLAMA_HOST, temperature=0) # type: ignore

    llm= models.get_groq_chat(api_key=GROQ_API_KEY) # type: ignore
    # llm= models.get_mixtral_model(api_key=MIXTRAL_API_KEY) 


    # agent configuration
    config = AgentConfig(
        chat_model = llm,
        utility_model = llm,
        # embeddings_model = embedding_llm,
        memory_subdir = "",
        auto_memory_count = 0,
        auto_memory_skip = 2,
        rate_limit_seconds = 65,
        rate_limit_requests = 20,
        rate_limit_input_tokens = 100000,
        rate_limit_output_tokens = 0,
        # msgs_keep_max= 25
        # msgs_keep_start = 5
        # msgs_keep_end = 10
        response_timeout_seconds = 60,
        max_tool_response_length = 30000,
        code_exec_docker_enabled = False,
        # code_exec_docker_name = "agent-zero-exe",
        # code_exec_docker_image = "frdel/agent-zero-exe:latest",
        # code_exec_docker_ports = { "22/tcp": 50022 }
        # code_exec_docker_volumes = { files.get_abs_path("work_dir"): {"bind": "/root", "mode": "rw"} }
        code_exec_ssh_enabled = False,
        # code_exec_ssh_addr = "localhost",
        # code_exec_ssh_port = 50022,
        # code_exec_ssh_user = "root",
        # code_exec_ssh_pass = "toor",
        # additional = {},
    )
    
    # create the first agent
    agent0 = Agent( agent= "0", config = config )

    # start the chat loop
    chat(agent0)


# Main conversation loop
def chat(agent:Agent):
    
    # start the conversation loop  
    while True:
        # ask user for message
        with input_lock:
            timeout = agent.get_data("timeout") # how long the agent is willing to wait
            if not timeout: # if agent wants to wait for user input forever
                PrintStyle(background_color="#6C3483", font_color="white", bold=True, padding=True).print(f"User message ('e' to leave):")        
                import readline # this fixes arrow keys in terminal
                user_input = input("> ")
                PrintStyle(font_color="white", padding=False, log_only=True).print(f"> {user_input}") 
                
            else: # otherwise wait for user input with a timeout
                PrintStyle(background_color="#6C3483", font_color="white", bold=True, padding=True).print(f"User message ({timeout}s timeout, 'w' to wait, 'e' to leave):")        
                import readline # this fixes arrow keys in terminal
                # user_input = timed_input("> ", timeout=timeout)
                user_input = timeout_input("> ", timeout=timeout)
                                    
                if not user_input:
                    user_input = read_file("prompts/fw.msg_timeout.md")
                    PrintStyle(font_color="white", padding=False).stream(f"{user_input}")        
                else:
                    user_input = user_input.strip()
                    if user_input.lower()=="w": # the user needs more time
                        user_input = input("> ").strip()
                    PrintStyle(font_color="white", padding=False, log_only=True).print(f"> {user_input}")        
                    
                    

        # exit the conversation when the user types 'exit'
        if user_input.lower() == 'e': break

        # send message to agent0, 
        assistant_response = agent.message_loop(user_input)
        
        # print agent0 response
        PrintStyle(font_color="white",background_color="#1D8348", bold=True, padding=True).print(f"{agent.agent_name}: reponse:")        
        PrintStyle(font_color="white").print(f"{assistant_response}")        
                        

# User intervention during agent streaming
def intervention():
    if Agent.streaming_agent and not Agent.paused:
        Agent.paused = True # stop agent streaming
        PrintStyle(background_color="#6C3483", font_color="white", bold=True, padding=True).print(f"User intervention ('e' to leave, empty to continue):")        

        import readline # this fixes arrow keys in terminal
        user_input = input("> ").strip()
        PrintStyle(font_color="white", padding=False, log_only=True).print(f"> {user_input}")        
        
        if user_input.lower() == 'e': os._exit(0) # exit the conversation when the user types 'exit'
        if user_input: Agent.streaming_agent.intervention_message = user_input # set intervention message if non-empty
        Agent.paused = False # continue agent streaming 
    

# Capture keyboard input to trigger user intervention
def capture_keys():
        global input_lock
        intervent=False            
        while True:
            if intervent: intervention()
            intervent = False
            time.sleep(0.1)
            
            if Agent.streaming_agent:
                # with raw_input, application_keypad, mouse_input:
                with input_lock, raw_input, application_keypad:
                    event: InputEvent | None = get_input_event(timeout=0.1)
                    if event and (event.shortcut.isalpha() or event.shortcut.isspace()):
                        intervent=True
                        continue

# User input with timeout
def timeout_input(prompt, timeout=10):
    return timed_input.timeout_input(prompt=prompt, timeout=timeout)

if __name__ == "__main__":
    print("Initializing framework...")
    # OLLAMA_HOST = "https://e3b0-34-125-97-215.ngrok-free.app" #input("enter OLLAMA_HOST_URL: >> ")
    # MODEL = "tale/godseye-neo-v0.1.gguf" #input ("enter OLLAMA_MODEL_NAME: >>")
    # Start the key capture thread for user intervention during agent streaming
    threading.Thread(target=capture_keys, daemon=True).start()

    # Start the chat
    initialize()