import os
import openai
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
RESOURCE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT") 

openai.api_type = "azure"
openai.api_base = RESOURCE_ENDPOINT
openai.api_version = "2022-12-01" # this is the latest version as of 1/29/2023, check the latest version here: https://docs.microsoft.com/en-us/azure/cognitive-services/openai/reference-apis. 
                                  # ou can also look at the Azure OpenAI Playground and check the sample code for the current version of your deployment
openai.api_key = API_KEY

#returns a list of all OpenAI models
models = openai.Model.list()
print(models)