import pynecone as pc

class SimpleState(pc.State):
    message: str = "Hello, world!"

    def change_message(self):
        self.message = "You clicked the button!"

def index():
    return pc.vstack(
        pc.text(SimpleState.message, size="large"),
        pc.button("Click me", on_click=SimpleState.change_message),
    )

app = pc.App(state=SimpleState)
app.add_page(index, route="/")
app.compile()

if __name__ == "__main__":
    app.run()
