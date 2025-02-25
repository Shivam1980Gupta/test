from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.schema import HumanMessage
messages = [
  HumanMessage(content="write a thousand word essay about the sky"),
]
gateway_base_url = "https://5c43bfvqiq.us-east-2.awsapprunner.com"
gateway_api_key = "sk-1a80c7c1638344e5a850c4"
model = "anthropic.claude-v3.5-sonnet-AI_Team"

llm = ChatOpenAI(
  model_name=model,
  temperature=0.1,
  max_tokens=4096,
  openai_api_base=gateway_base_url, # openai_api_base represents the endpoint the Langchain object will make a call to when invoked
  openai_api_key=gateway_api_key,
)
print(llm.invoke(messages).content)