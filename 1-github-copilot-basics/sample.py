# /help for general help or you can have a prompt

# Create code by using comments
# Comment/Prompt:  Create a Python function that converts fahrenheit to celsius




# Start with def add



# Create code by using Chat
# Prompt:  Write a program that converts fahrenheit to celsius
# Note:  in the chat input box, you can see chat history with up arrow.

# @ sign is used to call an agent
# Help with the terminal
# Insert it into the terminal
# Prompt:  @terminal What is the command to list the files in a directory?

# Help with VSCode
# @vscode How do I open the Command Palette?
# @vscode How do I change the theme?
# @vscode How do I install extensions?

# Working with context
# When prompting, what are you refering to?
# #editor is the context for the active file
# #file the file where your cursor is
# #selection is what you have highlighted in the active file

# @workspace 
# Refers to the Visual Studio Code workspace
# Can't look at everything because of the limits of the LLM's context window 
# Code bases can be massive
# so will evaluate:
# 1. file system structure
# 2. relevant code snippets (class, methods, comments)
# does not have access to git history
# Cannot handle prompts like:
# "Fix all the bugs in this project" (too vague and expansive)
# "How many JS files does this project have?" (LLMs not good at counting; besides can use VS Code for this)


# Example:  my-python-project
# Prompt:  @workspace what is todo-app?
# Fuzzy search
# Prompt:  What code adds a task?
# Click the references

# /explain provide details about the code
# In-line Chat
# ctrl + i for Windows
# cmd + i for Mac

def add(a, b):
    return a + b

# /doc to add comments and documentation

# /clear
# Clear the Chat
# Can be more than about making things more tidy
# Can be helpful if you are going to focus on another topic

# Can create a Notebook
# @workspace /newNotebook Python to load a CSV dataset







