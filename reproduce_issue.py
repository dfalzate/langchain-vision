
import ollama
import inspect
from langchain_ollama import ChatOllama

try:
    print(f"Ollama version: {getattr(ollama, '__version__', 'unknown')}")
except Exception:
    print("Ollama version: unknown")

try:
    sig = inspect.signature(ollama.Client.chat)
    print(f"ollama.Client.chat signature: {sig}")
except Exception as e:
    print(f"Could not get signature: {e}")

client = ollama.Client(host="http://localhost:11434")

messages = [{'role': 'user', 'content': 'What is 2+2?'}]
tools = [{
    'type': 'function',
    'function': {
        'name': 'add',
        'description': 'Add two numbers',
        'parameters': {
            'type': 'object',
            'properties': {
                'a': {'type': 'integer'},
                'b': {'type': 'integer'}
            },
            'required': ['a', 'b']
        }
    }
}]

print("\nAttempting chat with tools...")
try:
    # Mimic what langchain-ollama does
    response = client.chat(
        model='qwen3:8b', # Assuming this model exists locally, or use a tiny one
        messages=messages,
        tools=tools,
        stream=True
    )
    print("Chat generator created successfully.")
    for chunk in response:
        print(f"Chunk: {chunk}")
        break
except TypeError as e:
    print(f"CAUGHT EXPECTED ERROR: TypeError: {e}")
except Exception as e:
    print(f"Caught other error: {type(e)}: {e}")

print("\nChecking ChatOllama integration...")
try:
    llm = ChatOllama(model="qwen3:8b", base_url="http://localhost:11434")
    llm_with_tools = llm.bind_tools(tools, parallel_tool_calls=False)
    res = llm_with_tools.invoke("What is 2+2?")
    print("ChatOllama invoke success")
except Exception as e:
    print(f"ChatOllama invoke failed: {type(e)}: {e}")
