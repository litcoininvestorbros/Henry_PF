import reflex as rx
from ctransformers import AutoModelForCausalLM

model_Q5 = AutoModelForCausalLM.from_pretrained(
    "TheBloke/Mistral-7B-OpenOrca-GGUF",
    model_file="mistral-7b-openorca.Q5_K_M.gguf",
    model_type="mistral",
    gpu_layers=0
)

class State(rx.State):
    """Estado de la aplicación."""
    review = ""
    respuesta = ""
    processing = False
    complete = False

    def get_respuesta(self):
        """Obtener la respuesta del prompt."""
        if self.review == "":
            return rx.window_alert("Review Empty")

        self.processing, self.complete = True, False
        yield
        prompt = f"""
        You are a humble restaurant manager that uses casual language.
        You are talking to a customer.
        Reply with a short one sentence to this Yelp review (posted by customer ): {self.review}
        """
        response = model_Q5(prompt)
        self.respuesta = response
        self.processing, self.complete = False, True

    def reset_respuesta(self):
        """Restablecer la respuesta."""
        self.respuesta = ""
        self.complete = False

def welcome():
    """Pantalla de bienvenida."""
    return rx.center(
        rx.vstack(
            rx.heading("Welcome to Mistral-7B-OpenOrca", font_size="2.5em", color="#FFFFFF"),
            rx.text(
                "Your AI assistant for generating restaurant review responses.",
                font_size="1.5em",
                color="#FFFFFF",
                margin_bottom="20px"
            ),
            rx.button(
                "Get Started",
                on_click=lambda: rx.redirect("index"),
                padding="15px",
                border_radius="5px",
                background_color="#007bff",
                color="#FFFFFF",
                font_size="1.2em"
            ),
            align="center",
            spacing="5"
        ),
        width="100%",
        height="100vh",
        background_color="#13274A"
    )

def index():
    """Pantalla principal para generar respuestas."""
    return rx.center(
        rx.vstack(
            rx.heading("Share your experience with us", font_size="1.5em", color="#0d0900"),
            rx.box(
                rx.input(
                    placeholder="Enter a review...",
                    on_blur=State.set_review,
                    width="100%",
                    padding="2px",
                    border_radius="10px",
                    margin_bottom="20px",
                    font_size="1.1em",
                    background_color="#FFFFFF",
                    color="#000000",
                    style={
                        "resize": "none",  # Desactiva el redimensionamiento manual
                        "overflow": "hidden",  # Ajuste automático del tamaño
                        "height": "auto",  # Ajusta la altura automáticamente
                        "box-sizing": "border-box"
                    }
                ),
                rx.button(
                    "Generate Response",
                    on_click=State.get_respuesta,
                    width="100%",
                    padding="15px",
                    border_radius="10px",
                    background_color="#800900",
                    color="#FFFFFF",
                    font_size="1.1em",
                    loading=State.processing
                ),
                width="100%",
                padding="22px",
                border_radius="10px",
                box_shadow="0 4px 8px rgba(0, 0, 0, 0.2)",
                background_color="#ffffff"
            ),
            rx.cond(
                State.complete,
                rx.vstack(
                    rx.box(
                        rx.text(State.respuesta, font_size="1.2em", color="#21130d"),
                        padding="20px",
                        border_radius="10px",
                        background_color="#FFFFFF",
                        margin_top="0px"
                    ),
                    rx.button(
                        "Close Response",
                        on_click=State.reset_respuesta,
                        padding="10px",
                        border_radius="5px",
                        background_color="#800900",
                        color="#FFFFFF",
                        font_size="1em",
                        margin_top="20px"
                    )
                )
            ),
            align="center",
            spacing="5"
        ),
        width="100%",
        height="100vh",
        background_image="url('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.seekingalpha.com%2Fuploads%2F2017%2F7%2F27%2F19219231-15011543111264696_origin.png&f=1&nofb=1&ipt=bab70aa4ffa937feebdd6615966f9dab15843b1a9fc8f3ee26b0f9f1a69b40a5&ipo=images')",
        # style={"background-size": "cover"}
    )

app = rx.App()
app.add_page(welcome, title="Welcome")
app.add_page(index, title="Darden Customer Experience")


