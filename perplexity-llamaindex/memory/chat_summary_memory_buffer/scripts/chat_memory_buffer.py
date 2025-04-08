from llama_index.core.memory import ChatSummaryMemoryBuffer
from llama_index.core.llms import ChatMessage
from llama_index.llms.openai import OpenAI as LlamaOpenAI
from openai import OpenAI as PerplexityClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure LLM for memory summarization
llm = LlamaOpenAI(
    model="gpt-4o-2024-08-06",
    api_key=os.getenv("PERPLEXITY_API_KEY"),
    base_url="https://api.openai.com/v1/chat/completions"
)

# Initialize memory with token-aware summarization
memory = ChatSummaryMemoryBuffer.from_defaults(
    token_limit=3000,
    llm=llm
)

# Add system prompt using ChatMessage
memory.put(ChatMessage(
    role="system",
    content="You're an AI assistant providing detailed, accurate answers"
))

# Create API client
sonar_client = PerplexityClient(
    api_key=os.getenv("PERPLEXITY_API_KEY"),
    base_url="https://api.perplexity.ai"
)

def chat_with_memory(user_query: str):
    memory.put(ChatMessage(role="user", content=user_query))
    messages = memory.get()
    
    messages_dict = [
        {"role": m.role, "content": m.content}
        for m in messages
    ]
    
    response = sonar_client.chat.completions.create(
        model="sonar-pro",
        messages=messages_dict,
        temperature=0.3
    )
    
    assistant_response = response.choices[0].message.content
    memory.put(ChatMessage(
        role="assistant",
        content=assistant_response
    ))
    
    return assistant_response
