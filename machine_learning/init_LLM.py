from ctransformers import AutoModelForCausalLM

model_Q5 = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-OpenOrca-GGUF", 
                                        model_file="mistral-7b-openorca.Q5_K_M.gguf",
                                        model_type="mistral",
                                        max_new_tokens=256,
                                        reset=True,
                                        gpu_layers=0
                                        )

model_Q5('Who are you?')