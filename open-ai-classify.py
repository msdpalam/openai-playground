#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
RESOURCE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT") 

openai.api_type = "azure"
openai.api_base = RESOURCE_ENDPOINT
openai.api_version = "2022-06-01-preview"
openai.api_key = API_KEY

response = openai.Completion.create(
  engine="openai-davinci-demo",
  prompt="Classify the sentiment in these tweets:\n\n1. \"I can't stand homework\"\n2. \"This sucks. I'm bored 😠\"\n3. \"I can't wait for Halloween!!!\"\n4. \"My cat is adorable ❤️❤️\"\n5. \"I hate chocolate\"\n\nTweet sentiment ratings:",
  temperature=0,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)

print(response)