# SOC TEAM OF LLM POWERED AI AGENTS

- There are the 3 AI agents (`SOC MANAGER AGENT`, `PENTESTER AGENT` and `THREAT_INTEL AGENT`) in the team each powered by llama3.1

EXAMPLE USE-CASE: 1
~~~
- User gives query to `SOC MANAGER AGENT`.
## EXAMPLE
```
{
	"user"	: "DDOS attacks mitigation"
}
```

- `SOC MANAGER AGENT` analyze the query using LLM and try to generate response for it. If he thinks he need the help of other agents he will invoke them by function calling. 

## EXAMPLE:
``` 
{
	"thoughts" : [
		"user is requesting a for mitigations against DDOS attacks.",
		"I don't have any knowledge about it."
		"Let me call the `THREAT_INTEL AGENT` to help me get more information."
	],
	"action" : {
		"fuction_call" : TRUE
		"function" : "`THREAT_INTEL AGENT`"
		"task" : "fetch the information about DDOS attack mitigation strategies"
	}
	"response":""
}
```
- `THREAT_INTEL AGENT` will take the `task` from `SOC MANAGER AGENT`. He will start with analysis and will generate response. IF he thinks he needs latest information for the task. he will call the the `WEB_SERACH TOOL` by function calling.
## EXAMPLE
```
{
	"thoughts" : [
		"user is requesting information about DDOS attacks mitigation strategies.",
		"My Knowledge is about DDOS attacks is not up-to date."
		"Let me call the `WEB_SEARCH TOOL` to help me fetch latest information from internet."
	],
	"action" : {
		"fuction_call" : TRUE
		"function" : "`WEB_SERACH TOOL`"
		"task" : "mitigation strategies for DDOS attacks"
	}
	"response":""
}
```
- `WEB_SEARCH TOOL` will make the query the internet and fetch latest information. it will return the response content to `THREAT_INTEL AGENT`. 
- `THREAT_INTEL AGENT` will summarize it and return response to `SOC MANAGET AGENT`.
## EXAMPLE
```
{
	"thoughts" : [
		"user is requesting information about DDOS attacks mitigation strategies.",
		"My Knowledge is about DDOS attacks is not up-to date."
		"Let me call the `WEB_SEARCH TOOL` to help me fetch latest information from internet."
	],
	"action" : {
		"fuction_call" : FALSE
		"function" : ""
		"task" : ""
	}
	"response":["here is the summary about the mitigation strategies to follow against DDOS attack...
				- Rate-limiting: using rate limiting can help reduse the unwanted traffic...
				- ......."]
}
```
- `SOC MANAGER AGENT` will consume the response returned from the other agents and format it to a readable format. once it thinks the answer is good enough it will return it to user.
## EXAMPLE
```
{
	"user"	: "DDOS attacks mitigation"
	"agent" : "best mitigation strategies to defend against DDOS attack:
			- Rate-limiting: using rate limiting can help reduse the unwanted traffic...
			- ......."
}
```
~~~

EXAMPLE USE-CASE: 2
~~~
- User gives query to `SOC MANAGER AGENT`.
## EXAMPLE
```
{
	"user"	: "scan the network for available hosts"
}
```

- `SOC MANAGER AGENT` analyze the query and try to generate response for it. If he thinks he need the help of other agents he will invoke them by function calling. 

## EXAMPLE:
``` 
{
	"thoughts" : [
		"user is requesting a for commands to scan the network for available hosts.",
		"I don't have any knowledge about it."
		"Let me call the `PENTESTER ANGET` to help me get more information."
	],
	"action" : {
		"fuction_call" : TRUE
		"function" : "`PENTESTER ANGET`"
		"task" : "perform the network scan for available hosts."
	}
	"response":""
}
```
- `PENTESTER ANGET` will take the `task` from `SOC MANAGER AGENT`. He will start with analysis and will generate response. IF he thinks he needs latest information for the task. he will call the the `WEB_SERACH TOOL` by function calling.
## EXAMPLE
```
{
	"thoughts" : [
		"user wants to perform the network scan for available hosts.",
		"nmap tool can be used to perform network scanning"
		"let me write a nmap command to perform the network scan for available hosts"
	],
	"action" : {
		"fuction_call" : FALSE
		"function" : ""
		"task" : ""
	}
	"response":"`nmap -T4 -SV {IP-ADDRESS-TO-SCAN}`"
}
```
- `PENTESTER ANGET` will generate and return response to `SOC MANAGET AGENT`.
## EXAMPLE
```
{
	"thoughts" : [
		"user wants to perform the network scan for available hosts.",
		"nmap tool can be used to perform network scanning"
		"let me write a nmap command to perform the network scan for available hosts"
	],
	"action" : {
		"fuction_call" : FALSE
		"function" : ""
		"task" : ""
	}
	"response":"`nmap -T4 -SV {IP-ADDRESS-TO-SCAN}`"
}
```
- `SOC MANAGER AGENT` will consume the response returned from the other agents and format it to a readable format. once it thinks the answer is good enough it will return it to user.
## EXAMPLE
```
{
	"user"	: "scan the network for available hosts"
	"agent" : "`nmap -T4 -SV {IP-ADDRESS-TO-SCAN}`"
}
```
~~~
