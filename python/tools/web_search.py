import pprint
from duckduckgo_search import DDGS, AsyncDDGS
from python.helpers.webscrape import WebScrape
from langchain.tools import tool


# @tool("web_search_tool")
# class WebSearchTool:
#   """A web_search tool for interacting with the DuckDuckGo

#   This class provides methods for initiating chat sessions with the DuckDuckGo AI,
#   both synchronously and asynchronously. It allows you to specify the model and
#   timeout values for the chat sessions.

#   Methods:
#       chat(query: str, model: str = None, timeout: int = None) -> str:
#           Initiates a chat session with the DuckDuckGo AI.
#       achat(query: str, model: str = None, timeout: int = None) -> str:
#           Initiates an asynchronous chat session with the DuckDuckGo AI.
#   """

#   def __init__(self):
#     """Initializes the WebSearchTool instance """
web_scrape = WebScrape()
pprint.pprint("TOOL Initalized: >> web_search_tool")

# @tool("web_search_tool")
def search( query: str, deep_search: bool = False, model: str = "mixtral-8x7b", timeout: int = 60, max_results: int = 5) -> str:
    """ Useful to web_seach_tool to search for information about given query.

    Args:
      query (str): The initial message or question to send to the AI.
      deep_search (bool) : to perfrom deep search. This will ensure that ddg will search the web for webpages and links to retrieve content.
        Default: Fasle
      model (str): The model to use. Defaults to "mixtral-8x7b".
      timeout (int): Timeout value for the HTTP client. Defaults to 30.
      max_results(int): number of websites to scrape. ONLY used when `deep_search = True`
        Default: 5

    Returns:
      str: The response .
    """
    pprint.pprint("TOOL INVOKED: >> web_search_tool")

    if deep_search:
      results = DDGS().text(query, safesearch = "off", max_results = max_results)
      response = web_scrape.scrape(results)
      # print (res)
      # q = f"answer the {query} using the given context {res}"
      # response = DDGS().chat(res, model = model, timeout = timeout)
      # print ("#--#--"*10)
      # return response
    else:
      response = DDGS().chat(query, model = model, timeout = timeout)
      #print (response)

    return response

# @tool("async_web_search_tool")
# async def asearch(query: str,  deep_search: bool = False, model= "mixtral-8x7b", max_result: int = 5) -> str:
#     """Initiates a async chat session with DuckDuckGo AI.

#     Args:
#       query (str): The initial message or question to send to the AI.
#       deep_search (bool) : to perfrom deep search. This will ensure that ddg will search the web for webpages and links to retrieve content.
#         Default: Fasle
#       model (str): The model to use. Defaults to "mixtral-8x7b".
#       max_results(int): number of websites to scrape. ONLY used when `deep_search = True`
#         Default: 5

#     Returns:
#       str: The response from the AI.
#     """
#     pprint.pprint("TOOL INVOKED: >> web_search_tool")

#     async with AsyncDDGS() as ddgs:
#         response = await ddgs.atext(query, safesearch = "off", max_results = max_result) if deep_search else await ddgs.achat(query, model = model)
#         #print(response)
#         return response

# ## EXAMPLE USAGE
# if __name__ == "__main__":
#     print (WebSearchTool().search(
#       query = "documents for namp library in python3",

#       deep_search = True,
#       timeout = 300, max_results=6))