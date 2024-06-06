"""Funcion que descarga y inicializa el modelo Mistral-7B-OpenOrca-GGUF.Q5_K_M
"""
from ctransformers import AutoModelForCausalLM


def main():    
    model_Q5 = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-OpenOrca-GGUF", 
        model_file="mistral-7b-openorca.Q5_K_M.gguf",
        model_type="mistral",
        max_new_tokens=256,
        reset=True,
        gpu_layers=0
    )

if __name__ == '__main__':
    main()