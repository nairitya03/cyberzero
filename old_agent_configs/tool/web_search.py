from duckduckgo_search import DDGS

class WebSearchTool:
    
    def __init__(self):
        return self
    

def search(query: str, results = 5, time="y") -> list[str]:
    """
    Searches DuckDuckGo for the given query and returns a list of results.

    Args:
    query: The search query.
    results: The number of results to return.
    time: The time limit for the search.

    Returns:
    A list of search results.
    """

    ddgs = DDGS()
    src = ddgs.text(
        query,
        safesearch="off",  # SafeSearch setting
        timelimit=time,  # Time limit (y = past year)
        max_results=results  # Number of results to return
    )
    results = []
    for s in src:
        results.append(str(s))
    return results