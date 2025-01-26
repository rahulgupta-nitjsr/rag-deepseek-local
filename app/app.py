import reflex as rx

class State(rx.State):
    chat_history: list = []

    def add_message(self, user_message: str):
        self.chat_history.append(("User", user_message))
        # Placeholder for AI response
        self.chat_history.append(("AI", "This is a placeholder response."))

def index():
    return rx.vstack(
        rx.heading("RAG AI Chatbot"),
        rx.box(
            rx.foreach(
                State.chat_history,
                lambda message: rx.text(f"{message[0]}: {message[1]}")
            ),
            padding="1em",
            border="1px solid #eaeaea",
        ),
        rx.input(placeholder="Type your message here...", on_blur=State.add_message),
        rx.button("Send", on_click=State.add_message),
    )

app = rx.App()
app.add_page(index)
