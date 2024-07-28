from llama_index.llms.groq import Groq
import os 

Groq_key = os.environ.get("GROQ_KEY")
llm = Groq(model="llama3-8b-8192", api_key=Groq_key)

# Basic complete
response = llm.complete("What is the capital of France?")
print(response)

# Stream Complete
response = llm.stream_complete("What is Machine Learning? in 250 words",)
for r in response:
    print(r.delta, end="")


# Chat Complete
from llama_index.core.llms import ChatMessage

messages = [
    ChatMessage(role="system", content="You are joke person"),
    ChatMessage(role="user", content="What is your name"),
    ]
resp = llm.chat(messages)
print(resp)

# Stream Chat
from llama_index.core.llms import ChatMessage

messages = [
    ChatMessage(role="system", content="You are joke person"),
    ChatMessage(role="user", content="What is your name"),
    ]
resp = llm.stream_chat(messages)
for r in resp:
    print(r.delta, end="")

