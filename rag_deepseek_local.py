import reflex as rx
from app.pdf_processor import extract_text_from_pdf
from app.vector_store import VectorStore
from app.llm_interface import generate_response
import os

# Create uploads directory if it doesn't exist
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# Create a global instance of VectorStore
vector_store = VectorStore()


class State(rx.State):
    chat_history: list = []

    def process_pdf(self, file: rx.UploadFile):
        file_path = f"uploads/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        text = extract_text_from_pdf(file_path)
        vector_store.add_text(text)
        self.chat_history.append(("System", f"Processed PDF: {file.filename}"))

    def add_message(self, user_message: str):
        if not user_message:
            return
        self.chat_history.append(("User", user_message))
        context = vector_store.search(user_message)
        prompt = f"Context: {context}\nQuestion: {user_message}\nAnswer:"
        ai_response = generate_response(prompt)
        self.chat_history.append(("AI", ai_response))


def index():
    return rx.center(
        rx.vstack(
            rx.heading("RAG AI Chatbot", size="lg"),
            rx.box(
                rx.vstack(
                    rx.upload(
                        rx.text("Drag and drop your PDF files here or click to select"),
                        border="1px dashed",
                        padding="2em",
                        on_upload=State.process_pdf,
                    ),
                    rx.box(
                        rx.foreach(
                            State.chat_history,
                            lambda message: rx.hstack(
                                rx.text(f"{message[0]}:", font_weight="bold"),
                                rx.text(message[1]),
                                width="100%",
                                padding="1em",
                            )
                        ),
                        height="400px",
                        overflow="auto",
                        border="1px solid #eaeaea",
                        padding="1em",
                        width="100%",
                    ),
                    rx.hstack(
                        rx.input(
                            placeholder="Type your message here...",
                            id="message",
                            width="100%",
                        ),
                        rx.button(
                            "Send",
                            on_click=lambda: State.add_message(
                                rx.get_value("message")
                            ),
                        ),
                    ),
                ),
                width="800px",
            ),
            padding="2em",
            spacing="2em",
        ),
    )


app = rx.App()
app.add_page(index)
