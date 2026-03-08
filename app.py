import re
import ast
import gradio as gr
import autopep8
import black
from transformers import pipeline
from reportlab.pdfgen import canvas


class ChatbotConfig:
    MODEL_NAME = "gpt2"
    DEFAULT_TEMP = 0.7
    DEFAULT_MAX_TOKENS = 100
    DEFAULT_TOP_P = 0.95

model = pipeline(
    "text-generation",
    model=ChatbotConfig.MODEL_NAME
)

conversation_history = []

def detect_python_code(text):

    patterns = [
        r'def\s+\w+\s*\(',
        r'class\s+\w+',
        r'import\s+\w+',
        r'from\s+\w+\s+import',
        r'if\s+.*:',
        r'for\s+.*\s+in\s+',
        r'while\s+.*:'
    ]

    for p in patterns:
        if re.search(p, text):
            return True

    return False


def check_syntax(code):

    try:
        ast.parse(code)
        return True, "No syntax errors"

    except SyntaxError as e:
        return False, f"Syntax Error line {e.lineno}: {e.msg}"


def fix_python_code(code):

    try:
        fixed = autopep8.fix_code(code)

        try:
            fixed = black.format_str(fixed, mode=black.FileMode())
        except:
            pass

        return fixed

    except:
        return code


def generate_response(message, temperature, max_tokens, top_p):

    output = model(
        message,
        max_new_tokens=int(max_tokens),
        temperature=temperature,
        do_sample=True,
        top_p=top_p
    )

    reply = output[0]["generated_text"]

    return reply


def chatbot(message, history, temperature, max_tokens, top_p):

    if detect_python_code(message):

        ok, err = check_syntax(message)

        if not ok:
            fixed = fix_python_code(message)
            history.append((message, f"Fixed Code:\n{fixed}\n\nError: {err}"))
            return history

    reply = generate_response(message, temperature, max_tokens, top_p)

    history.append((message, reply))

    return history


with gr.Blocks() as demo:

    gr.Markdown("# Syntax Surgeon - AI Code Fixer")

    chatbot_ui = gr.Chatbot(height=400)

    msg = gr.Textbox(label="Enter Message")

    send = gr.Button("Send")

    temp = gr.Slider(0.1,1,value=0.7,label="Temperature")
    tokens = gr.Slider(50,200,value=100,label="Max Tokens")
    top_p = gr.Slider(0.1,1,value=0.95,label="Top-P")

    send.click(
        chatbot,
        inputs=[msg, chatbot_ui, temp, tokens, top_p],
        outputs=chatbot_ui
    )

demo.launch(share=True)