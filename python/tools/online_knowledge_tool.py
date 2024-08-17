from agent import Agent
from python.tools import web_search
from python.helpers.tool import Tool, Response

class OnlineKnowledge(Tool):
    def execute(self,**kwargs):
        return Response(
            message=process_question(self.args["question"]),
            break_loop=False,
        )

def process_question(question):
    return str(web_search.search(question))