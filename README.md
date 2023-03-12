# openai-playground
Azure OpenAI Service is now [General Availability](https://azure.microsoft.com/en-us/blog/general-availability-of-azure-openai-service-expands-access-to-large-advanced-ai-models-with-added-enterprise-benefits/). The goal of this playground is to share some of the example scripts, hoping it will help getting up to speed with Azure OpenAI Service to and then build build powerful solutions on top of Azure OpenAI Service

## Prerequisites
  - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services)

  - Access granted to the Azure OpenAI service in the desired Azure subscription

    Currently, access to this service is granted only by application. You can apply for access to the Azure OpenAI service by completing the form at https://aka.ms/oai/access. Open an issue on this repo to contact us if you have an issue.

 - Install Python 3.7.1 or later version if you don’t have installed, from [here](https://github.com/openai/openai-quickstart-python)
 
 - Recommendation is to install a new python environment so it is isolated for OpenAI library, the python application can run in this environment. There there are few different ways you can create the virtual environments. I am using virtualenv tool ([reference](https://learnpython.com/blog/how-to-use-virtualenv-python/))
 
    ` virtualenv -p python3 myopenenv
    
    ` source myopenenv/bin/activate
    
 - The following Python libraries: os, requests, json
 - Install OpenAI client library
 
    `pip install openai`
    
    `
     pip install --upgrade openai (if you would like to upgrade to the latest)
    ` 
 - If you would like to use .env file to load the environment information from
 
   `
   pip install python-dotenv
   `
 - Create an environment variables file
 
   In VSCode, create new file called .env. I already have one environment file created. You can copy it and add your own environment variables if needed.
   
   
