import reflex as rx
from ctransformers import AutoModelForCausalLM

model_Q5 = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-OpenOrca-GGUF",
                                                model_file="mistral-7b-openorca.Q5_K_M.gguf",
                                                model_type="mistral",
                                                gpu_layers=0
                                               )

class State(rx.State):
    """The app state."""

    review = ""
    respuesta = ""
    processing = False
    complete = False

    def get_respuesta(self):
        """Get the response from the prompt."""
        if self.review == "":
            return rx.window_alert("Review Empty")

        self.processing, self.complete = True, False
        yield
        self.prompt = f"""
        You are a restaurant humble restaurant manager that uses casual language.
        You are talking to a customer.
        Repli with a short one sentence to this Yelp review: {self.review}
        """
        response = model_Q5(self.prompt)
        self.respuesta = response
        self.processing, self.complete = False, True

def index():
    return rx.center(
        rx.vstack(
            rx.heading("Mistral-7B-OpenOrca", font_size="1.5em"),
            rx.input(
                placeholder="Enter a review..",
                on_blur=State.set_review,
                width="25em",
            ),
            rx.button(
                "Generate Response", 
                on_click=State.get_respuesta,
                width="25em",
                loading=State.processing
            ),
            rx.cond(
                State.complete,
                rx.text(State.respuesta),
            ),
            align="center",
        ),
        width="100%",
        height="100vh",
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index, title="Reflex:Mistral-7B")