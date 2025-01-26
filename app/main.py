from .pdf_processor import extract_text_from_pdf
from .vector_store import VectorStore
from .llm_interface import generate_response, chat_with_model
import os

vector_store = VectorStore()

def process_and_add_pdf(file_path):
    if os.path.exists(file_path):
        extracted_text = extract_text_from_pdf(file_path)
        vector_store.add_text(extracted_text)
        return f"Text from {file_path} has been added to the vector store."
    else:
        return f"File {file_path} does not exist."

def query_system(user_query):
    context = vector_store.search(user_query)
    prompt = f"Context: {context}\nQuestion: {user_query}\nAnswer:"
    response = generate_response(prompt)
    return response

if __name__ == "__main__":
    # Test PDF processing and vector store
    sample_pdf_path = "../data/test_sample.pdf"
    print(process_and_add_pdf(sample_pdf_path))

    # Test querying the system
    user_query = "What is the main topic of the PDF?"
    print(f"User Query: {user_query}")
    print(f"System Response: {query_system(user_query)}")

    # Test chat functionality
    messages = [
        {"role": "user", "content": "Hello, can you summarize the content of the PDF?"}
    ]
    print(f"Chat Response: {chat_with_model(messages)}")

