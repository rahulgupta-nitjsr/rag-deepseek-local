import ollama

def generate_response(prompt, model_name='deepseek-r1:8b'):
    try:
        response = ollama.generate(model=model_name, prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Error generating response: {str(e)}"

def chat_with_model(messages, model_name='deepseek-r1:8b'):
    try:
        response = ollama.chat(model=model_name, messages=messages)
        return response['message']['content']
    except Exception as e:
        return f"Error in chat: {str(e)}"
