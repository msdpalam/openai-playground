# openai-playground
The goal of this playground is to share how we can interact with OpenAI's GPT Models, leveraging OpenAI Python library which provides convenient access to the OpenAI REST API from any Python 3.7+ applicationsome.

## Prerequisites
 - Install Visual Studio Code, following the documentation from [here](https://code.visualstudio.com/docs/setup/windows)

 - Install Python 3.7.1 or later version if you don’t have installed, from [here](https://github.com/openai/openai-quickstart-python)

 - Install Jupyter Notebook, following the [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) article.
 
 - Recommendation is to install a new python environment so it is isolated for OpenAI library, the python application can run in this environment. There there are few different ways you can create the virtual environments. [Conda](https://docs.conda.io/projects/conda/en/stable/commands/create.html) is the tool is I mostly use for Data Science environment creation, I am using virtualenv tool ([reference](https://learnpython.com/blog/how-to-use-virtualenv-python/)), running the command from the command prompt. 
     
     `
      virtualenv -p python3 myopenenv
     `
     
     `
      source myopenenv/bin/activate
     `
 - Another tool to use is [venv](https://docs.python.org/3/library/venv.html). An example is below:
    `
      python -m venv myopenenv
     `
     
     `
      source myopenenv/bin/activate
     `
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
   
Other references:
 - [How to setup a Jupyter Notebook in VS Code (w/ virtual env & kernels) & install packages.](https://medium.com/@claudia.nikel/how-to-setup-a-jupyter-notebook-in-vs-code-w-virtual-env-kernels-install-packages-884cf643375e)
 - [Jupyter Notebooks in Visual Studio Code](https://opensourceoptions.com/jupyter-notebooks-in-visual-studio-code/)


#### Disclaimer
The content shared in this GitHub repo is solely for learning purposes. The thoughts, opinions, and perspectives expressed on this account are my own and do not reflect those of my employer or any official positions associated with my work. My content is shared in a personal capacity and is not representative of my role or responsibilities as an employee of the federal government.

When I am sharing the examples, I will be searching for examples, all over the web and will running in my environment first to learn from it and then to share it hear as a reference, in case it becomes handy. If I am not quoting the original author, it will be accidental. I deeply respect all the authors and their contribution in the community and if I am sharing, it is purely for learning purposes. I will try my best to share the reference for all contents I review.

