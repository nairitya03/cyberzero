# from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

# def search(query: str, results = 5, region = "wt-wt", time="y") -> str:
#     # Create an instance with custom parameters
#     api = DuckDuckGoSearchAPIWrapper(
#         region=region,  # Set the region for search results
#         safesearch="off",  # Set safesearch level (options: strict, moderate, off)
#         time=time,  # Set time range (options: d, w, m, y)
#         max_results=results  # Set maximum number of results to return
#     )
#     # Perform a search
#     result = api.run(query)
#     return result

import random
from duckduckgo_search import DDGS
from python.helpers.webscrape import WebScrape 

def search(query: str, results = 5, region = "wt-wt", time="y") -> list[str]:

    ddgs = DDGS()
    src = ddgs.text(
        query,
        region=region,  # Specify region 
        safesearch="off",  # SafeSearch setting
        timelimit=time,  # Time limit (y = past year)
        max_results=results  # Number of results to return
    )
    results = []
    for s in src:
        results.append(str(s))
    return results



# pprint.pprint("TOOL Initalized: >> web_search_tool")

# @tool("web_search_tool")
def deep_search(query: str, deep_search: bool = False, timeout: int = 60, max_results: int = 5) -> str:
    """ Useful to web_seach_tool to search for information about given query.

    Args:
        query (str): The initial message or question to send to the AI.
        deep_search (bool) : to perfrom deep search. This will ensure that ddg will search the web for webpages and links to retrieve content.
            Default: Fasle
        model (str): The model to use. Defaults to "mixtral-8x7b".
        timeout (int): Timeout value for the HTTP client. Defaults to 30.
        max_results(int): number of websites to scrape. ONLY used when `deep_search = True`
        Default: 3

    Returns:
        str: The response .
    """

    # pprint.pprint("TOOL INVOKED: >> web_search_tool")

    if deep_search:
        results = DDGS().text(query, safesearch = "off", max_results = max_results , timelimit = "y" )
        response =  WebScrape().scrape(results)
        # print (res)
        # q = f"answer the {query} using the given context {res}"
        # response = DDGS().chat(res, model = model, timeout = timeout)
        # print ("#--#--"*10)
        # return response
    else:
        model = random.choice(["claude-3-haiku", "mixtral-8x7b", "llama-3-70b"])
        response = DDGS().chat(query, model = model, timeout = timeout)
        #print (response)

    return response