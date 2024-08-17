# Cyber Zero
This is a Cybersecurity focused agentic Implementation of [Agent Zero AI framework](https://github.com/frdel/agent-zero). To Leverage full potential of this framework, use uncensored model with GPU.

## Know Issuses
- Does not work well with llama3.1 model.
- When working with with uncensored model, sometimes get into infinte loop of AI-Human conversation.

## NOTE:
This is for Eductaion and Research purpose only. Use at your own risk.

## Setup
1. **Required API keys:**
- At the moment, the only recommended API key is for https://www.perplexity.ai/ API. Perplexity is used as a convenient web search tool and has not yet been replaced by an open-source alternative. If you do not have an API key for Perplexity, leave it empty in the .env file and Perplexity will not be used.
- Chat models and embedding models can be executed locally via Ollama and HuggingFace or via API as well.

2. **Enter your API keys:**
- You can enter your API keys into the **.env** file, which you can copy from **example.env**
- Or you can export your API keys in the terminal session:
~~~bash
export API_KEY_PERPLEXITY="your-api-key-here"
export API_KEY_OPENAI="your-api-key-here"
~~~

3. **Install dependencies with the following terminal command:**
~~~bash
pip install -r requirements.txt
~~~

3. **Choose your chat, utility and embeddings model:**
- In the **main.py** file, right at the start of the **chat()** function, you can see how the chat model and embedding model are set.
- You can choose between online models (OpenAI, Anthropic, Groq) or offline (Ollama, HuggingFace) for both.

4. **run Docker:**
- Easiest way is to install Docker Desktop application and just run it. The rest will be handled by the framework itself.

## Run the program
- Just run the **main.py** file in Python:
~~~bash
python main.py
~~~
- Or run it in debug mode in VS Code using the **debug** button in the top right corner of the editor. I have provided config files for VS Code for this purpose.
