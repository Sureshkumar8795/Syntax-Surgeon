# Syntax-Surgeon

Syntax Surgeon is an AI-powered Python code assistant that detects syntax errors and automatically fixes them. The application combines natural language generation with code formatting tools to help developers quickly correct Python code and improve readability.

The system first analyzes the input text to determine whether it contains Python code. If Python code is detected, it performs syntax validation using Python’s AST parser. When syntax errors are found, the tool automatically repairs and reformats the code using auto-formatting libraries. If the input is a normal message instead of code, the AI generates a conversational response.This project provides a simple web interface built with Gradio where users can enter messages or Python code, adjust AI generation settings, and receive responses instantly.

# Features

Automatic Python code detection
Syntax error identification using Python AST
Automatic code correction and formatting
AI-generated conversational responses
Adjustable AI parameters (Temperature, Max Tokens, Top-P)
Interactive web interface using Gradio

# Technologies Used

Python
Gradio
Hugging Face Transformers
GPT-2 language model
Autopep8
Black code formatter
ReportLab

# How It Works

1.User enters a message or Python code.
2.The system checks if the input contains Python syntax.
3.If Python code is detected:
4.If the input is normal text, the AI model generates a response.
5.The result is displayed in the chatbot interface.

# Future Improvements

Support for multiple programming languages
Advanced AI code explanation feature
Code debugging suggestions
Deployment as a cloud web application

